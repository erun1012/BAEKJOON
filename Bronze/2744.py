import sys

N = str(sys.stdin.readline().rstrip())

for i in N:
  if i.isupper():
    print(i.lower(), end="")
  else:
    print(i.upper(), end="")