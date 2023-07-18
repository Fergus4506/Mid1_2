#include<bits/stdc++.h>

using  namespace std;
typedef long long ll;
const int N=6;
int a[N][N],cnt[N];//cnt用来记录每列已经下了多少棋子
int X0,X1,Y1,ans;
map<ll,int> vis;
 
ll recheck()
{
    ll sum=0;
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            sum=sum<<2 | a[j][i];//确保状态唯一性
     return sum;
}
int judge(int p)
{
 
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
        {
            if(i+2<=3&&a[i][j]==p&&a[i+1][j]==p&&a[i+2][j]==p)return 1;//竖
            if(j+2<=3&&a[i][j]==p&&a[i][j+1]==p&&a[i][j+2]==p)return 1;//横
            if(i+2<=3&&j+2<=3&&a[i][j]==p&&a[i+1][j+1]==p&&a[i+2][j+2]==p)return 1;//右上
            if(i-2>=0&&j+2<=3&&a[i][j]==p&&a[i-1][j+1]==p&&a[i-2][j+2]==p)return 1;//左上
        }
    return 0;
}
void dfs(int p)
{
 
    unsigned int k=recheck();
    if(vis[k])return;
    vis[k]=1;
    if(judge(1)||judge(2)||a[X1][Y1])
    {
        if(judge(2)&&a[X1][Y1]==2)ans++;//以白棋在x1，y1处结尾且白棋连续
        return;
    }
 
    for(int i=0; i<4; i++)//四列分别放棋
    {
 
        if(cnt[i]==4)continue;
        a[i][cnt[i]++]=p;
        dfs(3-p);     //   dfs(p^3)  p=2时p^3为1,反之为2（按位异或，不同为1，相同为0）
        a[i][--cnt[i]]=0;
    }
}
int main()
{
 
    scanf("%d%d%d",&X0,&Y1,&X1); 
    X0--,Y1--,X1--;//下标从0开始
    a[X0][cnt[X0]++]=1;//1代表黑，2代表白
    dfs(2);
    printf("%d\n",ans);
    return 0;
}