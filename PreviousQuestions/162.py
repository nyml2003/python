import heapq
import math

sum=0.0
n=int(input())
vex=[]
edges=[[0]*n for _ in range(n)]
for i in range(n):
    vex.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        edges[j][i]=edges[i][j]=math.sqrt((vex[i][0]-vex[j][0])*(vex[i][0]-vex[j][0])+(vex[i][1]-vex[j][1])*(vex[i][1]-vex[j][1]))+(vex[i][2]-vex[j][2])*(vex[i][2]-vex[j][2])
dis=[float('inf')]*n
vis=[False]*n
dis[0]=0
q=[]
edgeNum=0  
heapq.heappush(q,(dis[0],0))
while q and edgeNum<n:
    x=heapq.heappop(q)
    if vis[x[1]]:
        continue
    edgeNum+=1
    sum+=x[0]
    vis[x[1]]=True
    for i in range(n):
        if i!=x[1] and edges[x[1]][i]<dis[i]:
            dis[i]=edges[x[1]][i]
            heapq.heappush(q,(dis[i],i))
print(round(sum,2))