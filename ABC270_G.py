import io
import re
import sys

_INPUT = """\
6
3
5 2 1 1 0
5 2 2 3 0
11 1 1 0 10
"""
sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    P,A,B,S,G=map(int,input().split())
    AI=pow(1-A,P-2,P)
    if S==G: print(0)
    elif G>=P: print(-1)
    else:
      if A==1:
        if B%P==0: print(-1)
        else: print((G-S)*pow(B,P-2,P)%P)
      elif A==0:
        if B==G: print(1)
        else: print(-1)
      else:
        M=max(int(P**.5),1)
        tmp=[pow(A,j,P) for j in range(M)]
        tmp2=set(tmp)
        flg=-1
        a=(G-B*AI)*pow(S-B*AI,P-2,P)%P
        b=pow(A,M*(P-2),P)
        for i in range(P//M+2):
          if a in tmp2:
            flg=0
            for j in range(M):
              if a==tmp[j]:
                print(i*M+j)
                break
            break
          a=(a*b)%P
        if flg==-1: print(flg)