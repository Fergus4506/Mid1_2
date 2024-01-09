#include<bits/stdc++.h>
using namespace std;
int num[62501];
int prince[62501],princess[62501];
int dp[62501];

int main() {
    ios::sync_with_stdio(false);
    int t;  cin >> t;
    int c=1;
    while(t--){
        int n,p,q;  cin >> n >> p >> q;
        int x,ans=0;
        memset(num,0,sizeof(num));
        for(int i=1;i<=p+1;i++){
            cin >> prince[i];
            num[prince[i]]=i;
        }

        for(int i=1;i<=q+1;i++){
            cin >> x;
            princess[i]=num[x];
            dp[i]=INT_MAX;
        }

        for(int i=1;i<=q+1;i++){
            int index=lower_bound(dp+1,dp+1+i,princess[i])-dp;
            dp[index]=princess[i];
            ans=max(ans,index);
            //cout << index << " " << dp[index] << " " << ans << "\n";
        }

        cout << "Case " << c << ": " << ans << "\n";
        c++;
    }
    return 0;
}
