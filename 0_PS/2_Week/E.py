import sys

A, B, C, M = map(int, sys.stdin.readline().rstrip().split())

Max_time, Sleepy, i = 0, 0, 0
while i < 24:
  if (Sleepy + A) <= M:
    Sleepy += A
    Max_time += 1
  else:
    Sleepy -= C
    if Sleepy < 0:
      Sleepy = 0
  i += 1

print(Max_time * B)