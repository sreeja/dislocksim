# exposed through rpc
import os
import time
import json
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from Lock import LockType, Lock
from kazoo.client import KazooClient, KazooState


# this method not actually tested
def my_listener(state):
    global zk
    global child_path
    global child_value

    if state == KazooState.LOST:
        logger.warn("lost connection to zookeeper server")
    elif state == KazooState.SUSPENDED:
        logger.warn("connection has been lost but may be recovered")
    else:
        logger.info("connect/reconnect to zookeeper server")
        if zk is not None and child_path is not None:
            try:
                if not zk.exists(child_path):
                    zk.create(child_path, child_value.encode(
                        'utf-8'), ephemeral=True)
            except Exception as e:
                logger.exception(e)


def get_zookeeper_client():
    time.sleep(15)  # for zookeeper to startup
    placement = os.environ.get("PLACEMENT")
    if placement == "centralised":
        zookeeper_client = 'zoo-paris:2181'
    elif placement == "clustered":
        # get nearest - tokyo - nyc, singapore-paris, rest same
        if replicaname == "singapore":
            zookeeper_client = 'zoo-paris:2181'
        elif replicaname == "tokyo":
            zookeeper_client = 'zoo-newyork:2181'
        else:
            zookeeper_client = 'zoo-' + replicaname + ':2181'
    else:
        zookeeper_client = 'zoo-' + replicaname + ':2181'
    return zookeeper_client


def get_lock_config():
    oplocks = {}
    locktypes = {}
    oplock_filename = os.path.join(
        '/', 'usr', 'config', exp_app, 'granular' + exp_gran, 'oplock' + exp_type + '.json')
    with open(oplock_filename, 'r') as oplock_file:
        oplocks = json.load(oplock_file)

    locktype_filename = os.path.join(
        '/', 'usr', 'config', exp_app, 'granular' + exp_gran, 'locktype.json')
    with open(locktype_filename, 'r') as locktype_file:
        locktypes = json.load(locktype_file)

    return oplocks, locktypes


whoami = os.environ.get("WHOAMI")
replicaname = whoami[whoami.index('-')+1:]
replicas = ["paris", "tokyo", "singapore", "capetown", "newyork"]

exp_app = os.environ.get("APP")
exp_gran = os.environ.get("GRANULARITY")
exp_type = os.environ.get("LOCKTYPE")

zookeeper_client = get_zookeeper_client()
zk = KazooClient(hosts=zookeeper_client)
zk.start()

zk.add_listener(my_listener)

oplocks, locktypes = get_lock_config()

locklist = {}


def getlocks(opname, oplocks):
    for entry in oplocks:
        if entry["op"] == opname:
            return entry["locks"]


# get required locks for that method
def get_lock_list(opname, params):
    locks = []
    requiredLocks = getlocks(opname, oplocks)
    for r in requiredLocks:
        for t in locktypes:
            if r["name"] == t["name"]:
                paramValues = []
                for p in t["params"]:
                    paramValues += [params[p]]
                lockname = "_".join([t["name"]] + paramValues)
                locktype = LockType(t["name"], t["params"])
                newlock = Lock(lockname, locktype, r["mode"])
                locks += [newlock]
    return locks


# get all the required locks from zookeeper
@dispatcher.add_method
def acquire_locks(opname, params):
    print("inside acquire locks", flush=True)
    locks = get_lock_list(opname, params)
    locknames = sorted([(lock.name, lock.mode) for lock in locks])
    zklocks = []
    for each in locknames:
        if each[1] == "shared":
            lock = zk.ReadLock(each[0], whoami)
        else:
            lock = zk.WriteLock(each[0], whoami)
        zklocks += [lock]
        locklist[each[0]+'-'+each[1]] = lock
    flag = False
    for each in zklocks:
        try:
            done = each.acquire(timeout=10)
        except Exception as e:
            print("FAILURELOCK", str(e))
            flag = True
            break
        if not done:
            flag = True
            break
    if flag:
        for each in zklocks:
            each.release()
        print("Lock failed", flush=True)
        raise Exception("Lock failed")
    print("all locks acquired", flush=True)
    return locknames


# release all locks
@dispatcher.add_method
def release_locks(locknames):
    print("inside release locks", flush=True)
    print(locklist, flush=True)
    zklocks = []
    for each in locknames:
        zklocks += [locklist.pop(each[0]+'-'+each[1])]
    for each in zklocks:
        done = each.release()


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple(whoami, 4001 + replicas.index(replicaname), application)
