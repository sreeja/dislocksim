# generate granularity lattice
import itertools
import json

def getlockname(list):
  result = "_".join(sorted(list))
  return result

def visit(start, vertices, visited):
  visited.add(start)
  for e in vertices[start]:
    if e not in visited:
      visited = visited.union(visit(e, vertices, visited))
  return visited

def isvalidcombo(combo):
  # check whether it is a single connected graph. If yes, valid
  vertices = {}
  for c in combo:
    v = c.split("_")
    if v[0] not in vertices:
      vertices[v[0]] = []
    if v[1] not in vertices:
      vertices[v[1]] = []

    vertices[v[0]] += [v[1]]
    vertices[v[1]] += [v[0]]

  visited = set()
  starts = combo[0].split("_")
  if len(vertices[starts[0]]) > 0 :
    visited = visit(starts[0], vertices, visited)
  else:
    visited = visit(starts[1], vertices, visited)
  if len(vertices) == len(visited):
    return True
  return False


# get_coarsenings function provides all possible coarsening options for the tokens for a specific application
def get_coarsenings(filename):
  with open(filename, 'r') as f:
    tokens = json.load(f)

  locks = set()

  for t in tokens :
    for c in t["conflicts"]:
      lockname = getlockname([t["name"], c["conflict"]])
      locks.add(lockname)

  finelocks = [l for l in locks]

  #  at this point we have a list of locks. Next step is to generate all valid combinations
  combos = []
  for i in range(2, len(finelocks)):
    for each in itertools.combinations(finelocks, i):
      combos += [each]

  for c in combos:
    if isvalidcombo(c):
      lockname = getlockname(c)
      locks.add(lockname)

  # print(locks)
  # print(len(locks))
  return locks


# import os
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'auction', 'token.json')
# get_coarsenings(filename)
