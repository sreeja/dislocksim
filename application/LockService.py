import os
import json
import time
from kazoo.client import KazooClient, KazooState


class LockService:
    def __init__(self, whoami):
        self.zks = []
        replicas = ["paris", "tokyo", "singapore", "capetown", "newyork"]
        client_name = 'zoo-' + whoami
        port = 2181 #+ replicas.index(whoami)
        placement = ['cent', 'clust', 'dist']
        for each in placement:
            zookeeper_client = client_name + '-' + each + ':' + str(port)
            print(zookeeper_client, flush=True)
            zk = KazooClient(hosts=zookeeper_client)
            zk.start()
            self.zks += [zk]


    def get_lock_config(self, exp_app, exp_gran, exp_type, exp_place):
        oplocks = {}
        locktypes = {}
        oplock_filename = os.path.join(
            '/', 'usr', 'config', 'locker', exp_app, 'granular' + exp_gran, 'oplock' + exp_type + '.json')
        with open(oplock_filename, 'r') as oplock_file:
            oplocks = json.load(oplock_file)

        locktype_filename = os.path.join(
            '/', 'usr', 'config', 'locker', exp_app, 'granular' + exp_gran, 'locktype' + exp_place + '.json')
        with open(locktype_filename, 'r') as locktype_file:
            locktypes = json.load(locktype_file)

        return oplocks, locktypes
