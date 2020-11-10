import os
from flask import Flask, request, Response
import time
import requests
import json
from datetime import datetime
from LockService import LockService
from Locker import Locker


def create_app():
    flapp = Flask(__name__)
    return flapp


def get_exec_time(appname):
    exectime_filename = os.path.join('/', 'usr', 'config', 'application', appname+'.json')
    with open(exectime_filename, 'r') as exectime_file:
        exectimejson = json.load(exectime_file)

    exectime = {}
    for each in exectimejson:
        exectime[each["name"]] = each["time"]
    return exectime


time.sleep(20)
flapp = create_app()

whoami = os.environ.get("WHOAMI")
replicas = ["paris", "tokyo", "singapore", "capetown", "newyork"]

exp_app = os.environ.get("APP")
exp_gran = os.environ.get("GRANULARITY")
exp_type = os.environ.get("LOCKTYPE")

exectime = get_exec_time(exp_app)

# locking service initialization
lock_service = LockService(whoami)
oplocks, locktypes = lock_service.get_lock_config(exp_app, exp_gran, exp_type)


def execute(opname, params):
    with Locker(whoami, lock_service, oplocks, locktypes, opname, params):
        time.sleep(exectime[opname] * 0.001)

# def execute(opname, params):
#     url = "http://locker-"+whoami+":400" + \
#         str(replicas.index(whoami)+1)+"/jsonrpc"
#     print("locking rpc request to " + url, flush=True)
#     # ACQUIRE REQUIRED LOCKS
#     payload = {
#         "method": "acquire_locks",
#         "params": [opname, params],
#         "jsonrpc": "2.0",
#         "id": 0,
#     }
#     try:
#         response = requests.post(url, json=payload).json()
#     except requests.exceptions.Timeout:
#         print("Timeout while acquire", flush=True)
#         raise
#     except Exception as e:
#         print("Some other error while acquire", flush=True)
#         raise

#     if "error" in response:
#         print("Locks not acquired", flush=True)
#         raise
#     else:
#         print("MYAcquire ", response, flush=True)
#         print("locks acquired", flush=True)

#         # sleep the execution time
#         time.sleep(exectime[opname] * 0.001)

#         # release locks
#         payload = {
#             "method": "release_locks",
#             "params": [response["result"]],
#             "jsonrpc": "2.0",
#             "id": 0,
#         }
#         try:
#             response = requests.post(url, json=payload).json()
#         except requests.exceptions.Timeout:
#             print("Timeout while release", flush=True)
#             raise
#         except Exception as e:
#             print("Some other error while release", flush=True)
#             raise

#         print("MYRelease ", response, flush=True)
#         print("locks released", flush=True)


@flapp.route('/')
def hello_world():
    tic = datetime.now()
    execute('createauction', {'seller': 's12'})
    duration = datetime.now() - tic
    return f'Hello world from {whoami} , total time taken {str(duration)} \n'


@flapp.route('/do', methods=['GET', 'PUT', 'DELETE', 'POST'])
def do_get():
    print("CALLINGG the op..", flush=True)
    s = time.time()
    op = request.args.get('op', '')
    paramstring = request.args.get('params', '')

    params = {}
    for each in paramstring.split(","):
        kv = each.split("-")
        params[kv[0]] = kv[1]

    print(op, params, flush=True)
    execute(op, params)
    print("FINISHINGG the op..", time.time()-s, flush=True)
    return Response("{'a':'b'}", status=200, mimetype='application/json')
