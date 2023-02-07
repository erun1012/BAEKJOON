L = int(input())
s = list(input())
S, Sum, M = [], 0, 1234567891

for x in s:
  S.append(ord(x)-96)

for i in range(0, L):
  Sum += (S[i] * 31**i)

print(Sum % M)
