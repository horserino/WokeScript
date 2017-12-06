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
