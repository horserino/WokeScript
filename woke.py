import sys

ascended_level = 0
# Ascended level: the permission level for your script
# Ascend with 'ascend'

def parse(src):
  c = src.splitlines()
  if not src.startswith("woke"):
    return
  for line in c:
    # Check for 'ascend'
    if "ascend" in line:
      ascended_level = ascended_level + 1
    if "output" in line:
      if ascended_level >= 1:
        print(line[7:])
      else:
        print("is not woke: not ascended enough")
