# exposed through rpc
import jsonrpc
import json
import os

from Lock import LockType, Lock
from kazoo.client import KazooClient

dirname = os.path.dirname(__file__)

zk = KazooClient(hosts='localhost:2181')
zk.start()

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
# @dispatcher.add_method
def acquire_locks(appname, opname, params):
  locks = get_lock_list(appname, opname, params)
  locknames = sorted([(l.name, l.mode) for l in locks])
  zklocks = []
  for each in locknames:
    if each[1] == "shared":
      zklocks += [zk.ReadLock(each[0])]
    else:
      zklocks += [zk.WriteLock(each[0])]
  # acquire all locks asynchronously
  return locknames

# release locks
# release all locks
# @dispatcher.add_method
def release_locks(locknames):
  # release all locks asynchronously
  return


# def application(request):
#     # Dispatcher is dictionary {<method_name>: callable}
#     dispatcher["echo"] = lambda s: s
#     dispatcher["add"] = lambda a, b: a + b

#     response = JSONRPCResponseManager.handle(
#         request.data, dispatcher)
#     return Response(response.json, mimetype='application/json')


# if __name__ == '__main__':
#     run_simple('localhost', 4000, application)


get_lock_list('auction', 'placebid', {"auction":"a12", "buyer":"b45"})