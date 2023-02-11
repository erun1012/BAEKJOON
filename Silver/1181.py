import sys

N = int(sys.stdin.readline())

Word_list = []

for i in range(N):
  Word = str(sys.stdin.readline().strip())
  if Word in Word_list:
    continue
  else:
    Word_list.append(Word)
    
Word_list.sort()
Word_list.sort(key = len)

for j in Word_list:
    print(j)