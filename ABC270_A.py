import io
import sys

_INPUT = """\
6
1 2
5 3
0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  print(A|B)