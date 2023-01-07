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


n,m=map(int,input().split())
dsu=Dsu(n)
for _ in range(m):
    z,x,y=map(int,input().split())
    x=x-1
    y=y-1
    if (z==1):
        dsu.union(x,y)
    elif (z==2):
        x,y=dsu.find(x),dsu.find(y)
        if (x==y):
            print("Y")
        else:
            print("N")