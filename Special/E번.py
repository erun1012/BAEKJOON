import sys

K = int(sys.stdin.readline())
A, B = [0]*K, [0]*K
for i in range(K):
  S = list(map(str, sys.stdin.readline().rstrip().split()))
  if S[0] == 'add':
    if S[1] == 'A':
      A[i] = S[2]
    elif S[1] == 'B':
      B[i] = S[2]
  elif S[0] == 'delete':
    if S[1] == 'A':
      A.remove(S[2])
    elif S[1] == 'B':
      B.remove(S[2])
  else:
    F = S[1]
    result = 0
    for k in range(0, len(A)):
      for l in range(0, len(B)):
        for j in range(0, len(F)-1):
          if (A[k] != 0) and (B[l] != 0):
            if  A[k][:j+1] + B[l][-(len(F)-1-j):] == F:
                  result += 1
    print(result)