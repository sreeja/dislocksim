class LockType:
    def __init__(self, name, params):
        self.name = name
        self.params = params


class Lock:
    def __init__(self, name, locktype, mode):
        self.name = name
        self.locktype = locktype
        self.mode = mode
