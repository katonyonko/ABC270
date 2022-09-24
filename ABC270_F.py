import io
import sys

_INPUT = """\
6
4 2
1 20 4 7
20 2 20 3
1 3 5
1 4 6
3 1
1 1 1
10 10 10
1 2 100
7 8
35 29 36 88 58 15 25
99 7 49 61 67 4 57
2 3 3
2 5 36
2 6 89
1 6 24
5 7 55
1 3 71
3 4 94
5 6 21
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #Union Find
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  N,M=map(int,input().split())
  uf=UnionFind(N+2)
  uf2=UnionFind(N+2)
  uf3=UnionFind(N+2)
  uf4=UnionFind(N+2)
  edge=[]
  X=list(map(int,input().split()))
  Y=list(map(int,input().split()))
  for _ in range(M):
    A,B,Z=map(int,input().split())
    A-=1; B-=1
    edge.append((Z,A,B))
  for i in range(N):
    edge.append((X[i],i,N))
    edge.append((Y[i],i,N+1))
  edge.sort()
  ans=10**20

  def func(UF,E,n,k):
    global ans
    c=0
    tmp=0
    for i in range(len(E)):
      z,a,b=E[i]
      if k==1 and (b==N or b==N+1) or k==2 and b==N or k==3 and b==N+1: continue
      if UF.find(a)!=UF.find(b):
        tmp+=z
        UF.union(a,b)
        c+=1
    if c==n-1: ans=min(ans,tmp)

  func(uf,edge,N,1)
  func(uf2,edge,N+1,2)
  func(uf3,edge,N+1,3)
  func(uf4,edge,N+2,4)
  print(ans)