import shlex


class Environment:
  def __init__(self):
    self.declared = []
    self.variables = {
      
    }
  
  def add_variable(self, var, value):
    self.variables[var] = value
    
  def get_variable(self, var, value):
    return self.variables[var]
  
  def parse(code):
    c = shlex.split(code)
    tok = ""
    for char in code:
      char += tok
      if tok == ";" or tok == " ":
        tok == ""
      elif tok == "sample text to:":
        v = tok.split(":", 1)[1]
        print(v, end="\n")
        tok = ""
      elif tok == "var ":
        v = tok.split(" ", 1)[1]
        self.declared.append(v)
        tok = ""
      elif tok in self.declared:
        v = tok.split("=", 1)[1]
        self.add_variable(tok, v)
        tok = ""
      elif tok == "quick maths":
        print(3)
        tok = ""
