N, K = map(int,input().split())

n1, n2, n3 = 1, 1, 1

for i in range(1, N+1):
  n1 *= i
for j in range(1, (N-K)+1):
  n2 *= j
for k in range(1, K+1):
  n3 *= k

result = n1/(n2*n3)
print(int(result))