#include<bits/stdc++.h>
using namespace std;

vector<string> dp[101][101];

vector<string> solve(string &a, string &b, int n, int m) {
    if(n == 0 || m == 0) return {""};
    if(dp[n][m].size()) return dp[n][m];
    if(a[n-1] == b[m-1]) {
        vector<string> tmp = solve(a, b, n-1, m-1);
        for(string &s : tmp) s.push_back(a[n-1]);
        return dp[n][m] = tmp;
    } else {
        vector<string> left = solve(a, b, n-1, m);
        vector<string> right = solve(a, b, n, m-1);
        if(left[0].size() > right[0].size()) return dp[n][m] = left;
        else if(left[0].size() < right[0].size()) return dp[n][m] = right;
        else {
            left.insert(left.end(), right.begin(), right.end());
            sort(left.begin(), left.end());
            left.erase(unique(left.begin(), left.end()), left.end());
            return dp[n][m] = left;
        }
    }
}

int main() {
    string a, b;
    while(cin >> a >> b) {
        for(int i = 0; i <= a.size(); i++)
            for(int j = 0; j <= b.size(); j++)
                dp[i][j].clear();
        vector<string> ans = solve(a, b, a.size(), b.size());
        for(string &s : ans) cout << s << endl;
    }
    return 0;
}
