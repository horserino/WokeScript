import sys


class WoketualMachine:
  # The Wokescript VM
  def __init__(self):
    self.stack = []
    
  def _pop(self):
    self.stack.pop()
    
  def _append(self, arg):
    self.stack.append(arg)
    
  def add(self):
    first_num = self._pop()
    second_num = self._pop()
    t = first_num + second_num
    self._append(t)
    
  def print_answer(self):
    a = self._pop()
    print(a)
    
  def load_val(self, num):
    self._append(num)

def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
