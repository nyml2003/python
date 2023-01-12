#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstring>
const int N = 50009;
using namespace std;
struct Edge {
    int u;
    int v;
    int next;
}e[N], edge[N];
typedef pair<int, int> pii;
stack<int> q;
queue<int> p;
int dfn[N], low[N], h[N], w[N], d[N], fa[N], head[N], in[N];
int dis[N];
int instack[N];
int s, edgenum, dnum, ans;
void addEdge(int u, int v) {
    edgenum++;
    e[edgenum].u = u;
    e[edgenum].v = v;
    e[edgenum].next = h[u];
    h[u] = edgenum;
}
void tarjan(int u)
{
    s++;
    low[u] = s;
    dfn[u] = s;
    q.push(u);
    instack[u] = 1;
    for (int i = h[u]; i; i = e[i].next) {
        int v = e[i].v;
        if (!dfn[v]) tarjan(v);
        if (instack[v]) low[u] = min(low[u], low[v]);
    }
    if (low[u] == dfn[u]) {
        int flag = 0, cnt = 0, od = 0;
        while (1) {
            int v = q.top();
            q.pop();
            instack[v] = 0;
            if (v == u) break;
            w[u] += w[v];
            w[v] = 0;
            fa[v] = u;
        }
        d[++dnum] = u;
    }
}
void topo() {
    
    for (int i = 1; i <= dnum; i++) if (in[d[i]] == 0) { 
        p.push(d[i]); dis[d[i]] = w[d[i]]; 
    }
    while (!p.empty()) {
        int u = p.front();
        p.pop();
        for (int i = head[u]; i; i = edge[i].next) {
            int v = edge[i].v;
            dis[v] = max(dis[v], dis[u] + w[v]);
            in[v]--;
            if (in[v] == 0) p.push(v);
        }
    }
    for (int i = 1; i <= dnum; i++) ans = max(ans, dis[d[i]]);
}

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++) cin >> w[i];
    for (int i = 1; i <= m; i++) {
        int u, v;
        cin >> u >> v;
        addEdge(u, v);
    }
    for (int i = 1; i <= n; i++) fa[i] = i;
    for (int i = 1; i <= n; i++) if (!dfn[i]) tarjan(i);
    edgenum = 0;
    for (int i = 1; i <= m; i++) {
        int u = fa[e[i].u], v = fa[e[i].v];
        if (u != v) {
            edgenum++;
            edge[edgenum].u = u;
            edge[edgenum].v = v;
            edge[edgenum].next = head[u];
            head[u] = edgenum;
            in[v]++;
        }

    }
    topo();
    cout << ans << endl;
    return 0;
}
