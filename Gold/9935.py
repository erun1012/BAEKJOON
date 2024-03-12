from sys import stdin

get = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()

lastbomb = bomb[-1]
list = []

for char in get:
    list.append(char)
    if char == lastbomb and ''.join(list[-len(bomb):]) == bomb:
        del list[-len(bomb):]
        
result = ''.join(list)
if result == '':
    print("FRULA")
else:
    print(result)
