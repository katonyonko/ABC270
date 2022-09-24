import io
import sys

_INPUT = """\
6
5 2 5
1 2
1 3
3 4
3 5
6 1 2
3 1
2 5
1 2
4 1
2 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    D=[-1]*len(G)
    D[s]=-2
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]==-1:
          D[y]=x
          dq.append(y)
    return D

  N,X,Y=map(int,input().split())
  X-=1; Y-=1
  G=[[] for _ in range(N)]
  for _ in range(N-1):
    U,V=map(lambda x: int(x)-1,input().split())
    G[U].append(V)
    G[V].append(U)
  parent=bfs(G,Y)
  ans=[]
  while parent[X]!=-2:
    ans.append(X+1)
    X=parent[X]
  print(*ans,X+1)