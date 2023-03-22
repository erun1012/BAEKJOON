#1213
import sys

S = sys.stdin.readline().rstrip()
S_list = [0]*26
Result = []

for i in S:
  S_list[ord(i)-65] += 1

count = 0
for j in S_list:
  if j % 2 == 1:
    count += 1
    
    
if count >= 2:
  print("I'm Sorry Hansoo")
if count <= 1:
  pos = 0
  p = 0
  for k in range(0, len(S_list)):
    if S_list[k] > 0:
      if S_list[k] % 2 == 1:
        p = k+65
        S_list[k] -= 1
      for l in range(S_list[k]):
        Result.insert(pos, chr(k+65))
      pos += S_list[k]//2
  if p != 0:
    Result.insert(pos, chr(p))
for n in Result:
  print(n, end="")