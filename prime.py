n=10**8
Prime=[]
isPrime=[False]*n
def Euler(n)->None:
    for i in range(2,n):
        if isPrime[i]==False:
            Prime.append(i)
            print(i)
        for j in Prime:
            if i*j<n:
                isPrime[i*j]=True
                if i % j == 0:
                    break
Euler(n)
file=open('D:\\code\\python\\primes.txt','r')
cnt=0
try:
    while True:
        line=file.readline()
        if not line:
            break
        if int(line) in Prime:
            cnt+=1
finally:
    file.close()
print(cnt)