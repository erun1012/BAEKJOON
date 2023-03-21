#0001100 = 010으로 봐도 된다.
# 길이에 관계없이 문자가 바뀌는지만 보기 때문
import sys

S = sys.stdin.readline().rstrip()

count = 0
for i in range(0, len(S)-1):
  if S[i-1] != S[i]:
    count += 1
print(((count+1)//2))