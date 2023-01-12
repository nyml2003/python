     
def f(n)->int:
    base=[[1,1],[1,0]]
    ans=[[1,0],[1,0]]
    if n<3:
        return ans[n-1][0]
    else:
        n-=2
        while n:
            if n&1:
                ans= [[sum(map(lambda a: a[0]*a[1], zip(l, s))) for l in zip(*ans)] for s in base]
            base= [[sum(map(lambda a: a[0]*a[1], zip(l, s))) for l in zip(*base)] for s in base]
            n>>=1
        return ans[0][0]


n,m,p=map(int,input().split())
print(((f(n+2)-1) % f(m)) %p)