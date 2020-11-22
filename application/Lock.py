class LockType:
    def __init__(self, name, params, placement):
        self.name = name
        self.params = params
        self.placement = placement


class Lock:
    def __init__(self, name, locktype, mode):
        self.name = name
        self.locktype = locktype
        self.mode = mode
