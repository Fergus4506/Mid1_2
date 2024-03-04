#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;  cin >> n;
    int ans[n];
    int index[n];
    for(int i=0;i<n;i++){
        int x;  cin >> x;
        ans[x-1]=i+1;
    }
    int student[n];
    int x;
    while(cin >> x){
        student[x-1]=1;
        for(int i=1;i<n;i++){
            cin >> x;
            student[x-1]=i+1;
        }

        // for(auto &v:ans)
        //    cout << v << " ";
        // cout << "\n";
        // for(auto &v:student)
        //    cout << v << " ";
        vector<vector<int>> dp(n+1,vector<int>(n+1,0));
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(ans[i-1]==student[j-1])
                    dp[i][j]=dp[i-1][j-1]+1;
                else
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
            }
        }
        cout << dp[n][n] << "\n";
    }

    return 0;
}
/*
4
4 2 3 1
1 3 2 4
3 2 1 4
2 3 4 1
10
3 1 2 4 9 5 10 6 8 7
2 10 1 3 8 4 9 5 7 6

1 2 3 4 5 6 7 8 9 10
4 7 2 3 10 6 9 1 5 8
3 1 2 4 9 5 10 6 8 7
*/
