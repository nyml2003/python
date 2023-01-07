import functools
class Dsu:
    def __init__(self,size):
        self.fa=list(range(size))
        self.size = [1] * size
    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]     
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.fa[y] = x
        self.size[x] += self.size[y]
ans=0
linkedVex=1
n,m=map(int,input().split())
dsu=Dsu(n+1)
edges=[]
for i in range(m):
    edges.append(list(map(int,input().split())))
edges.sort(key= lambda x:x[2])
for i in range(m):
    e=edges[i]
    if (dsu.find(e[0])!=dsu.find(e[1])):
        dsu.union(e[0],e[1])
        ans+=e[2]
        linkedVex+=1
        if (linkedVex==n):
            break
if (linkedVex==n):
    print(ans)
else:
    print("orz")    