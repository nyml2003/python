l,r=map(int,input().split())
ans=0
for i in range(l,r+1):
    if '2022' in str(i):
        ans+=i
print(ans)
