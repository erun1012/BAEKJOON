from sys import stdin

get = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()

while get.find(bomb) != -1:
    get = get.replace(bomb,"")
if len(get) > 0:
    print(get)
else:
    print("FRULA")
