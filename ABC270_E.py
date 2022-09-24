import io
import sys

_INPUT = """\
6
1 1
1
3 3
1 3 0
2 1000000000000
1000000000000 1000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  tmp=[(0,-1)]+sorted([(A[i],i) for i in range(N)])
  flg=0
  for i in range(N):
    a,b=tmp[i]
    c,d=tmp[i+1]
    if K-(c-a)*(N-i)<0:
      t=i
      break
    K-=(c-a)*(N-i)
    if i==N-1: a=c; flg=1
  A=[max(0,A[i]-a) for i in range(N)]
  if flg==0:
    n=K//(N-t)
    K-=n*(N-t)
    A=[max(0,A[i]-n) for i in range(N)]
  for i in range(N):
    if K==0: break
    if A[i]>0:
      A[i]-=1
      K-=1
  print(*A)