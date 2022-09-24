import io
import sys

_INPUT = """\
6
10 -10 1
20 10 -10
100 1 1000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X,Y,Z=map(int,input().split())
  if 0<Y and Y<X and Y<Z or 0>Y and Y>X and Y>Z: print(-1)
  elif 0<X and (Y>X or Y<0) or 0>X and (Y<X or Y>0): print(abs(X))
  else: print(abs(Z)+abs(Z-X))