# exposed through rpc
from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
# import jsonrpc
import json
import os
import time

from Lock import LockType, Lock
from kazoo.client import KazooClient

dirname = os.path.dirname(__file__)
whoami = os.environ.get("WHOAMI")
replicas = ["paris", "tokyo", "singapore", "capetown", "newyork"]

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
          zk.create(child_path, child_value.encode('utf-8'), ephemeral=True)
      except Exception as e:
        logger.exception(e)

time.sleep(30) # for zookeeper to startup
zk = KazooClient(hosts='zookeeper:2181')
zk.start()

zk.add_listener(my_listener)

locklist = {}


def getlocklist(opname, oplocks):
  for l in oplocks:
    if l["op"] == opname:
      return l["locks"]

# support functions
# get required locks for that method
def get_lock_list(appname, opname, params):
  oplocks = {}
  oplock_filename = os.path.join(dirname, appname, 'oplock.json')
  with open(oplock_filename, 'r') as oplock_file:
    # content = oplock_file.Read
    oplocks = json.load(oplock_file)
  
  locktypes = {}
  locktype_filename = os.path.join(dirname, appname, 'locktype.json')
  with open(locktype_filename, 'r') as locktype_file:
    locktypes = json.load(locktype_file)

  locks = []

  requiredLocks = getlocklist(opname, oplocks)

  for r in requiredLocks :
    for t in locktypes:
      if r["name"] == t["name"] :
        paramValues = []
        for p in t["params"]:
          paramValues += [params[p]]
        lockname = "_".join([t["name"]] + paramValues)
        locktype = LockType(t["name"], t["params"], t["category"], t["placement"])
        newlock = Lock(lockname, locktype, r["mode"])
        locks += [newlock]

  # print([l.name for l in locks])
  return locks

# acquire locks
# get all the required locks asynchronously from zookeeper
@dispatcher.add_method
def acquire_locks(appname, opname, params):
  print("inside acquire locks", flush=True)
  locks = get_lock_list(appname, opname, params)
  locknames = sorted([(l.name, l.mode) for l in locks])
  zklocks = []
  for each in locknames:
    if each[1] == "shared":
      lock = zk.ReadLock(each[0])
    else:
      lock = zk.WriteLock(each[0])
    zklocks += [lock]
    locklist[each[0]+'-'+each[1]] = lock
  # TODO: acquire all locks asynchronously
  for each in zklocks:
    done = each.acquire()
    if not done:
      print(each.path + " not acquired")
  # print("all locks acquired", flush=True)
  return locknames

# release locks
# release all locks
@dispatcher.add_method
def release_locks(locknames):
  # print("inside release locks", flush=True)
  zklocks = []
  for each in locknames:
    zklocks += [locklist[each[0]+'-'+each[1]]]
  # TODO: release all locks asynchronously
  for each in zklocks:
    done = each.release()
    # print(done, flush=True)
    if not done:
      print(each.path + " not released")

  # print("all locks released", flush=True)
  return


# TODO: rpc
@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple(whoami, 4001 + replicas.index(whoami[whoami.index('-')+1:]), application)


# get_lock_list('auction', 'placebid', {"auction":"a12", "buyer":"b45"})