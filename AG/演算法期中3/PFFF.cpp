#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t; cin >> t;
    int c=1;
    while(t--){
        int n,p,q;  cin >> n >> p >> q;
        p++,q++;
        int prince[p],princess[q];
        int num[n*n+1];
        // int dp[q+1];
        memset(num,0,sizeof(num));
        // memset(dp,1e9,sizeof(dp));
        int ans=0;
        for(int i=0;i<p;i++){
            cin >> prince[i];
            num[prince[i]]=i;
        }
        for(int i=0;i<q;i++){
            int x;  cin >> x;
            princess[i]=num[x];
        }
        // for(auto &v:prince){
        //     cout << v << " ";
        // }cout << "\n";
        // for(auto &v:princess){
        //     cout << v << " ";
        // }cout << "\n";

        // for(int i=0;i<q;i++){
        //     if(dp[princess[i]]==0)
        //         dp[princess[i]]=1;
        //     for(int j=0;j<princess[i];j++){
        //         dp[princess[i]]=max(dp[princess[i]],dp[j]+1);
        //         ans=max(ans,dp[princess[i]]);
        //     }
        // }

        vector<int> dp;
        dp.push_back(princess[0]);
        for(int i=1;i<q;i++){
            int tame=princess[i];
            if(tame>dp.back())
                dp.push_back(tame);
            else
                *lower_bound(dp.begin(),dp.end(),tame)=tame;
        }

        cout << "Case " << c << ": " << dp.size() << "\n";
        c++;
    }

    return 0;
}
/*
1
3 6 7
1 7 5 4 8 3 9
1 4 3 5 6 2 8 9
Case 1: 4
*/
