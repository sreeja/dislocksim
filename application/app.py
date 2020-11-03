import os
from flask import Flask, request
import time
import requests
import json
from datetime import datetime

def create_app():
  flapp = Flask(__name__)
  return flapp

def get_exec_time(appname):
  dirname = os.path.dirname(__file__)
  exectime_filename = os.path.join(dirname, appname+'.json')
  with open(exectime_filename, 'r') as exectime_file:
    # content = oplock_file.Read
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
exectime = get_exec_time(exp_app)

def execute(opname, params):
  url = "http://locker-"+whoami+":400"+str(replicas.index(whoami)+1)+"/jsonrpc" 
  print("locking rpc request to " + url, flush=True)
  # ACQUIRE REQUIRED LOCKS
  payload = {
        "method": "acquire_locks",
        "params": [opname, params],
        "jsonrpc": "2.0",
        "id": 0,
    }
  try:
    response = requests.post(url, json=payload).json()
  except requests.exceptions.Timeout:
    print("Timeout while acquire", flush=True)
    raise
  except Exception as e:
    print("Some other error while acquire", flush=True)
    raise

  print("MYAcquire ", response, flush=True)
  print("locks acquired", flush=True)
  # sleep the execution time
  # print(exectime[opname])
  time.sleep(exectime[opname] * 0.001)

  # release locks
  payload = {
        "method": "release_locks",
        "params": [response["result"]],
        "jsonrpc": "2.0",
        "id": 0,
    }
  try:
    response = requests.post(url, json=payload).json()
  except requests.exceptions.Timeout:
    print("Timeout while release", flush=True)
    raise
  except Exception as e:
    print("Some other error while release", flush=True)
    raise

  print("MYRelease ", response, flush=True)


  print("locks released", flush=True)


@flapp.route('/')
def hello_world():
  tic = datetime.now()
  execute('createauction',{'seller':'s12'})
  duration = datetime.now() - tic
  return f'Hello world from {whoami} , total time taken {str(duration)} \n'

@flapp.route('/do', methods=['GET','PUT','DELETE','POST'])
def do_get(): 

  print("Calling the op..", flush=True)
  op = request.args.get('op', '')
  paramstring = request.args.get('params', '')

  params = {}
  for each in paramstring.split(","):
    kv = each.split("-")
    params[kv[0]] = kv[1]

  print(op, params, flush=True)

  execute(op, params)
  # except Exception as e:
  #   print("Errorwewant", str(e), flush=True)
  #   return "failed"
  return "done"

# @flapp.route('/do', methods=['PUT'])
# def do_put():
#   op = request.args.get('op', '')
#   paramstring = request.args.get('params', '')

#   params = {}
#   for each in paramstring.split(","):
#     kv = each.split("-")
#     params[kv[0]] = kv[1]

#   print(op, params, flush=True)

#   execute(op, params)
  
#   return "done"

# @flapp.route('/do', methods=['DELETE'])
# def do_delete():
#   op = request.args.get('op', '')
#   paramstring = request.args.get('params', '')

#   params = {}
#   for each in paramstring.split(","):
#     kv = each.split("-")
#     params[kv[0]] = kv[1]

#   print(op, params, flush=True)

#   execute(op, params)
  
#   return "done"

# @flapp.route('/do', methods=['POST'])
# def do_post():
#   op = request.args.get('op', '')
#   paramstring = request.args.get('params', '')

#   params = {}
#   for each in paramstring.split(","):
#     kv = each.split("-")
#     params[kv[0]] = kv[1]

#   print(op, params, flush=True)

#   execute(op, params)
  
#   return "done"
