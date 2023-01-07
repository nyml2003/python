s=input()
t=s.split()
pre=-1
ans=True
for i in range(len(t)):
    try:
        cur=int(t[i])
        if (cur>pre) :
            pre=cur
        else:
            ans=False
            break 
    except ValueError:
        continue
print(ans)