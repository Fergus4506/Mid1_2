//this codde is for the problem 10721 - Bar Codes from UVA online judge
// Date: 2021/09/10

#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

long long dp[55][55][55];

long long solve(int n, int k, int m){
    if(n == 0 && k == 0) return 1;
    if(n <= 0 || k <= 0) return 0;
    if(dp[n][k][m] != -1) return dp[n][k][m];
    long long ans = 0;
    for(int i = 1; i <= m; i++){
        ans += solve(n - i, k - 1, m);
    }
    return dp[n][k][m] = ans;
}

int main(){
    int n, k, m;
    while(cin >> n >> k >> m){
        memset(dp, -1, sizeof(dp));
        cout << solve(n, k, m) << endl;
    }
    return 0;
}
//discuss the code
//this code is a dynamic programming problem, the problem is to find the number of ways to make a bar code of length n with k segments and each segment can be of length 1 to m.
//the code is using a 3D dp array to store the number of ways to make a bar code of length n with k segments and each segment can be of length 1 to m.
