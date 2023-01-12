#include <iostream>
#include <cstring>
#include <queue>
#include <utility>
#include <cstdio>
#include <algorithm>
#include <cmath>
const int N=2009;
using namespace std;
struct node
{
    double dis;
    int v;
    node(double dis,int v):dis(dis),v(v){}
    bool operator>(const node& Node) const 
    {
        return this->dis>Node.dis;
    }
};
struct Edge{int v,next; double w;}edge[1000009];
priority_queue<node, vector<node>, greater<node> > q;
double dis[N];
int head[N];
int p[N];
bool vis[N],flag;
int n,m,cnt=0,edgeNum=0;
double sum=0.0;
int x[N],y[N],h[N];
void addEdge(int u,int v,double w){
    cnt++;
    edge[cnt].v=v;
    edge[cnt].w=w;
    edge[cnt].next=head[u];
    head[u]=cnt;
}
void prim(int st)
{
    fill(dis,dis+2000,0x3f3f3f3f);
    memset(vis,false,sizeof(vis));
    memset(p,0,sizeof(p));
    dis[st]=0.0;
    node e(dis[st],st);
    q.push(e);
    while ((!q.empty()) && edgeNum<n)
    {
        node x=q.top();
        q.pop();
        if (vis[x.v]) continue;
        edgeNum++;
        sum+=x.dis;
        vis[x.v]=true;
        for (int i=head[x.v]; i; i=edge[i].next)
        {
            if (edge[i].w<dis[edge[i].v])
            {
                dis[edge[i].v]=edge[i].w;
                node e(dis[edge[i].v],edge[i].v);
                q.push(e);
            }
        }
    }
}
int main()
{
    scanf("%d",&n);
    for (int i=1; i<=n; i++)
        cin>>x[i]>>y[i]>>h[i];
    for (int i=1; i<=n; i++)
        for (int j=i+1; j<=n; j++)
        {
            double w=sqrt((x[j]-x[i])*(x[j]-x[i])+(y[j]-y[i])*(y[j]-y[i]))+(h[j]-h[i])*(h[j]-h[i]);
            addEdge(i,j,w);
            addEdge(j,i,w);
        }
            
    prim(1);
    printf("%.2lf",sum);
    return 0;
}