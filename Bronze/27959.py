import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

price =(N*100) -  M

if price >= 0:
  print("Yes")

else:
  print("No")