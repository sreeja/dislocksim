import os
from flask import Flask, request

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

whoami = os.environ.get("WHOAMI")
replicas = ["paris", "tokyo", "singapore", "capetown", "newyork"]

@app.route('/')
def hello_world():
    return f'Hello world from {whoami} \n'

@app.route('/do')
def do():
  app = request.args.get('app', '')
  op = request.args.get('op', '')
  paramstring = request.args.get('params', '')

  params = {}
  for each in paramstring.split(","):
    kv = each.split("-")
    params[kv[0]] = kv[1]

  print(app, op, params, flush=True)

  # ACQUIRE REQUIRED LOCKS

  # sleep the execution time

  # release locks

  
  return "done"
