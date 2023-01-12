import os
import sys

# 请在此输入您的代码

def f(a,i:int,j:int)->int:
    if i<0 or j<0 or i<j:
        return 0
    if b[i][j]==0:
        b[i][j]=a[i][j]+max(f(a,i-1,j-1),f(a,i-1,j))
    return b[i][j]
n=int(input())
a=[]
b=[]
for i in range(n):
  a.append(list(map(int,input().split())))
  b.append([0]*n)
if n % 2==0:
    print(max(f(a,n-1,n//2-1),f(a,n-1,n//2)))
else:
    print(f(a,n-1,(n-1)//2))