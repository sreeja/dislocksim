import os
import time
from datetime import datetime
from kazoo.client import KazooClient

zk = KazooClient(hosts='0.0.0.0:2181')
zk.start()

logs = []

rlock = zk.ReadLock('lock1', 'paris')
for i in range(1000):
    try:
        tic = datetime.now()
        done = rlock.acquire()
        tac = datetime.now() - tic
        logs += ['time to acquire read lock :'+ str(tac)]
    except Exception as e:
        logs += ["ReadLock acquisition failed"+ str(e)]
    if not done:
        logs += ["ReadLock acquisition failed"+ str(e)]
    time.sleep(0.005)
    try:
        tic = datetime.now()
        done = rlock.release()
        tac = datetime.now() - tic
        logs += ['time to release read lock :'+ str(tac)]
    except Exception as e:
        logs += ["ReadLock release failed"+ str(e)]
    if not done:
        logs += ["ReadLock release failed"+ str(e)]

wlock = zk.WriteLock('lock1', 'paris')
for i in range(1000):
    try:
        tic = datetime.now()
        done = wlock.acquire()
        tac = datetime.now() - tic
        logs += ['time to acquire write lock :'+ str(tac)]
    except Exception as e:
        logs += ["WriteLock acquisition failed"+ str(e)]
    if not done:
        logs += ["WriteLock acquisition failed"+ str(e)]
    time.sleep(0.005)
    try:
        tic = datetime.now()
        done = wlock.release()
        tac = datetime.now() - tic
        logs += ['time to release write lock :'+ str(tac)]
    except Exception as e:
        logs += ["WriteLock release failed"+ str(e)]
    if not done:
        logs += ["WriteLock release failed"+ str(e)]


outputfile = os.path.join('/', 'Users', 'snair', 'works', 'dislock-experiments', 'dislocksim', 'log.txt')
with open(outputfile, 'w') as f:
    f.write('\n'.join(logs))

