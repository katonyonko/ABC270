import io
import sys

_INPUT = """\
6
10 2
1 4
11 4
1 2 3 6
10000 10
1 2 4 8 16 32 64 128 256 512
10 3
1 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  dp=[0]*(N+1)
  for i in range(N):
    for j in range(K):
      if i+A[j]<N+1:
        dp[i+A[j]]=max(dp[i+A[j]],A[j]+i-dp[i])
  print(dp[-1])