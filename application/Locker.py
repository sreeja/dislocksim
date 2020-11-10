from Lock import LockType, Lock


class Locker(object):
    def __init__(self, whoami, zk, oplocks, locktypes, opname, params):
        self.locklist = []
        locks = self.get_lock_list(oplocks, locktypes, opname, params)
        locknames = sorted([(lock.name, lock.mode) for lock in locks])
        # zklocks = []
        for each in locknames:
            if each[1] == "shared":
                lock = zk.ReadLock(each[0], whoami)
            else:
                lock = zk.WriteLock(each[0], whoami)
            # zklocks += [lock]
            self.locklist += [lock]
        flag = False
        for each in self.locklist:
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
        # zklocks = []
        # for each in locknames:
        #     zklocks += [self.locklist.pop(each[0]+'-'+each[1])]
        for each in self.locklist:
            done = each.release()


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
                    paramValues = []
                    for p in t["params"]:
                        paramValues += [params[p]]
                    lockname = "_".join([t["name"]] + paramValues)
                    locktype = LockType(t["name"], t["params"])
                    newlock = Lock(lockname, locktype, r["mode"])
                    locks += [newlock]
        return locks
