import time
from Lock import LockType, Lock

class Locker(object):
    def __init__(self, whoami, zks, oplocks, locktypes, opname, params):
        self.locklist = []
        self.whoami = whoami
        placement = ['cent', 'clust', 'dist']
        locks = self.get_lock_list(oplocks, locktypes, opname, params)
        locknames = sorted([(lock.name, lock.mode, lock.locktype.placement) for lock in locks])
        for each in locknames:
            if each[1] == "shared":
                lock = zks[placement.index(each[2])].ReadLock(each[0], whoami)
            else:
                lock = zks[placement.index(each[2])].WriteLock(each[0], whoami)
            self.locklist += [lock]
        flag = False
        for each in self.locklist:
            try:
                print('LOCKTIME ASKED: ', whoami, time.time(), flush=True)
                done = each.acquire(timeout=10)
                print('LOCKTIME OBTAINED: ', whoami, time.time(), flush=True)
            except Exception as e:
                print("FAILURELOCK", str(e))
                flag = True
                break
            if not done:
                flag = True
                break
        if flag:
            for each in self.locklist:
                each.release()
            print("Lock failed", flush=True)
            raise Exception("Lock failed")
        print("all locks acquired", flush=True)

    def __enter__(self):
        return self.locklist

    def __exit__(self, type, value, traceback):
        print("inside release locks", flush=True)
        print(self.locklist, flush=True)
        for each in self.locklist:
            print('LOCKTIME RELEASING: ', self.whoami, time.time(), flush=True)
            done = each.release()
            print('LOCKTIME RELEASED: ', self.whoami, time.time(), flush=True)

    def getlocks(self, opname, oplocks):
        for entry in oplocks:
            if entry["op"] == opname:
                return entry["locks"]

    # get required locks for that method

    def get_lock_list(self, oplocks, locktypes, opname, params):
        locks = []
        requiredLocks = self.getlocks(opname, oplocks)
        for r in requiredLocks:
            for t in locktypes:
                if r["name"] == t["name"]:
                    paramValues = [params[t["param"]]]
                    lockname = "_".join([t["name"]] + paramValues)
                    locktype = LockType(t["name"], t["param"], t["placement"])
                    newlock = Lock(lockname, locktype, r["mode"])
                    locks += [newlock]
        return locks
