#include<bits/stdc++.h>
using namespace std;
pair<int,int> a,b;
int g[5][5],cnt[4],ans;
bool vis[43046721+10];
int same(pair<int,int> x,pair<int,int> y,pair<int,int> z,int &f)
{
    if(g[x.first][x.second]>0 && g[x.first][x.second]==g[y.first][y.second] && g[x.first][x.second]==g[z.first][z.second])
    {
        if(x==b || y==b || z==b) {f=1;return 1;}
        return 2;
    }
    return 0;
}
bool check()
{
    int flag=0,k=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            k=k*3+g[i][j];
    if(vis[k]) return 0;
    vis[k]=1;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(i+2<4)
            {
                int k=same({i,j},{i+1,j},{i+2,j},flag);
                if(k>1) return 0;
            }
            if(j+2<4)
            {
                int k=same({i,j},{i,j+1},{i,j+2},flag);
                if(k>1) return 0;
            }
            if(i+2<4 && j+2<4)
            {
                int k=same({i,j},{i+1,j+1},{i+2,j+2},flag);
                if(k>1) return 0;
            }
            if(i+2<4 && j-2>=0)
            {
                int k=same({i,j},{i+1,j-1},{i+2,j-2},flag);
                if(k>1) return 0;
            }
        }
    return flag;
}
void dfs(int p)
{
    if(cnt[b.second]==b.first+1)
    {
        if(p==0) ans+=check();
        return;
    }
    for(int i=0;i<4;i++)
        if((i!=b.second && cnt[i]<4) || (i==b.second && cnt[i]<=b.first))
        {
            g[cnt[i]][i]=p+1;
            cnt[i]++;
            dfs(1-p);
            cnt[i]--;
            g[cnt[i]][i]=0;
        }
}
int main()
{
    a.first=0;
    scanf("%d%d%d",&a.second,&b.first,&b.second);
    a.second--,b.first--,b.second--;
    g[a.first][a.second]=1;
    cnt[a.second]++;
    dfs(1);
    printf("%d\n",ans);
    return 0;
}
