import sys

S = sys.stdin.readline().rstrip()
S_list = [0]*26

for i in S:
  S_list[ord(i)-97] += 1

for j in S_list:
  print(j, end=" ")