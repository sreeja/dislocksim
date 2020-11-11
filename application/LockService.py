import os
import json
import time
from kazoo.client import KazooClient, KazooState


class LockService:
    def __init__(self, whoami):
        zookeeper_client = zookeeper_client = 'zoo-' + whoami + ':2181'
        zk = KazooClient(hosts=zookeeper_client)
        zk.start()
        self.zk = zk

    def get_lock_config(self, exp_app, exp_gran, exp_type):
        oplocks = {}
        locktypes = {}
        oplock_filename = os.path.join(
            '/', 'usr', 'config', 'locker', exp_app, 'granular' + exp_gran, 'oplock' + exp_type + '.json')
        with open(oplock_filename, 'r') as oplock_file:
            oplocks = json.load(oplock_file)

        locktype_filename = os.path.join(
            '/', 'usr', 'config', 'locker', exp_app, 'granular' + exp_gran, 'locktype.json')
        with open(locktype_filename, 'r') as locktype_file:
            locktypes = json.load(locktype_file)

        return oplocks, locktypes
