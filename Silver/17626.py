from sys import stdin
import math

n = int(stdin.readline().rstrip())

DP_list = [5 for _ in range(n+1)]

for i in range(1, int(math.sqrt(n))+1):
    DP_list[i**2] = 1

def answer(n):
    
    if DP_list[n] == 1:
        return 1
    
    for i in range(1, int(math.sqrt(n))+1):
        if DP_list[n-i**2] == 1:
            return 2
    
    for i in range(1, int(math.sqrt(n))+1):
      for j in range(1, int(math.sqrt(n-i**2)) + 1):
          if DP_list[n-i**2-j**2] == 1:
              return 3
    return 4
print(answer(n))
