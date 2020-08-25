class LockType:
  def __init__(self):
    pass

  def __init__(self, name, params):
    self.name = name
    self.params = params


class Lock:
  def __init__(self):
    pass

  def __init__(self, name, locktype, mode):
    self.name = name
    self.locktype = locktype
    self.mode = mode






#   type LockType struct {
# 	Name      string  `json:"name"`
# 	Params    []Param `json:"params"`
# 	Category  string  `json:"category"`
# 	Placement string  `json:"placement"`
# }

# type Param struct {
# 	Param string `json:"param"`
# }

# type OpLock struct {
# 	Op    string `json:"op"`
# 	Locks []Tok  `json:"locks"`
# }

# type Tok struct {
# 	Name string `json:"name"`
# 	Mode string `json:"mode"`
# }

# type Lock struct {
# 	Name string   `json:"name"`
# 	Type LockType `json:"type"`
# 	Mode string   `json:"mode"`
# }
