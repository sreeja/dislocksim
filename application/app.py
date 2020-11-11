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
    exectime_filename = os.path.join(
        '/', 'usr', 'config', 'application', appname+'.json')
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
    with Locker(whoami, lock_service.zk, oplocks, locktypes, opname, params):
        time.sleep(exectime[opname] * 0.001)


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
