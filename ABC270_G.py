import io
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
    