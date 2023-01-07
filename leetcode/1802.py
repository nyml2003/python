n=int(input("n:"))
index=int(input("index:"))
maxSum=int(input("maxSum:"))
left=index
right=n-index-1
i=0
j=maxSum+1

while i+1<j:
    m=int((i+j)/2)
    tmp=m*n
    if left<m-1:
        tmp-=left*(left+1)/2
    else:
        tmp-=(m-1)*(left+1-m/2)
    if right<m-1:
        tmp-=right*(right+1)/2
    else:
        tmp-=(m-1)*(right+1-m/2)
    if tmp>maxSum:
        j=m
    else:
        i=m
    print("["+str(i),end=',')
    print(str(j)+")",end=' ')
    print(m,end=' ')
    print(tmp)
print(i)