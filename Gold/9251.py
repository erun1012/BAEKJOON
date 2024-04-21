# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#longest-common-subsequence-substring

from sys import stdin

S1 = ' '+stdin.readline().rstrip()
S2 = ' '+stdin.readline().rstrip()
LCS = [[0 for _ in range(len(S2))] for _ in range(len(S1))]
for i in range(1, len(S1)):
    for j in range(1, len(S2)):
        if S1[i] == S2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[-1][-1])
