import collections
import fileinput
class Graph:
    def __init__(self,size=0)->None:
        self.head=[0]*size
        self.edge=[[0,0,0]]
        self.w=[0]
        self.size=size
        self.inDegree=[0]*size
    def addEdge(self,edge)->None:
        u,v=edge[0],edge[1]
        self.edge.append([u,v,self.head[u]])
        self.head[u]=len(self.edge)-1
    def addValue(self,value:list)->None:
        self.w+=value
    def topo(self)->int:
        vis=collections.deque()
        dis=self.w.copy()
        for i in range(1,self.size):
            if self.inDegree[i]==0:
                vis.append(i)
        while vis:
            u=vis.popleft()
            i=self.head[u]
            while i:
                v=self.edge[i][1]
                dis[v]=max(dis[v],dis[u]+self.w[v])
                self.inDegree[v]-=1
                if self.inDegree[v]==0:
                    vis.append(v)
                i=self.edge[i][2]
        return max(dis)        

class Spn:
    def __init__(self,graph:Graph)->None:
        self.dfncnt=0
        self.low=[0]*graph.size
        self.dfn=[0]*graph.size
        self.vis=collections.deque()
        self.fa=list(range(graph.size))
        self.w=[]
        self.dic={}
        self.graph=graph
    def tarjan(self,u:int)->None:
        self.dfncnt+=1
        self.low[u]=self.dfncnt
        self.dfn[u]=self.dfncnt
        self.vis.append(u)
        i=self.graph.head[u]
        while i:
            v=self.graph.edge[i][1]
            if (self.dfn[v]==0):
                self.tarjan(v)
            if v in self.vis:
                self.low[u]=min(self.low[u],self.low[v])
            i=self.graph.edge[i][2]
        if (self.low[u]==self.dfn[u]):
            while True:
                v=self.vis.pop()
                if (u==v): 
                    break
                self.graph.w[u]+=self.graph.w[v]
                self.graph.w[v]=0
                self.fa[v]=u
            self.w.append(self.graph.w[u])
            self.dic[u]=len(self.w)
    def shrink(self,graph:Graph)->Graph:
        for i in range(1,graph.size):
            if self.dfn[i]==0:
                self.tarjan(i)
        g=Graph(len(self.w)+1)
        for i in graph.edge:
            u,v=self.fa[i[0]],self.fa[i[1]]
            if (u!=v):
                u,v=self.dic[u],self.dic[v]
                g.addEdge([u,v])
                g.inDegree[v]+=1
        g.addValue(self.w) 
        return g


            
if __name__=="__main__":
    file=open('D:\\code\\python\\luogu\\input.txt','r')
    n,m=map(int,file.readline().split())
    g=Graph(n+1)
    g.addValue(list(map(int,file.readline().split())))
    for i in range(m):
        g.addEdge(list(map(int,file.readline().split())))
    spn=Spn(g)
    g=spn.shrink(g)
    print(g.topo())
    file.close()
    


