#include <iostream>
#include <cstring>
using namespace std;
int p;
struct martix
{
    long long data[3][3];
    martix() {memset(data,0,sizeof(data));}
}ans,base;
martix operator *(martix res,martix temp) {
        martix cur;
        for (int i=1; i<=2; i++)
            for (int j=1; j<=2; j++)
                for (int k=1; k<=2; k++)
                    cur.data[i][j]= (cur.data[i][j]%p+(res.data[i][k]%p)*(temp.data[k][j]%p)%p)% p;
        return cur;
}
long long n,m;
void power(long long n)
{
    while (n){
        if (n&1) ans=base*ans;
        base=base*base;
        n>>=1;
    }
}
int f(int n)
{
  if (n<=2) {return ans.data[n][1];}
    else {
        power(n-2);
        return ans.data[1][1];
    }
}
int main()
{
    base.data[1][1]=1,base.data[1][2]=1,base.data[2][1]=1,base.data[2][2]=0;
    ans.data[1][1]=1,ans.data[2][1]=1;
    cin>>n>>m>>p;
    cout<<((f(n+2)-1)%f(m))%p;
    return 0;
}
