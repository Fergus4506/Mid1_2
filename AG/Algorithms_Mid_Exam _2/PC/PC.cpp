#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m, ans;
vector<vector<bool>> mp;
void DFS(int now_i = 0, int now_j = 0, int cnt = 0){
    mp[now_i][now_j] = false;
    ans = max(ans, cnt);
    int u = 0, d = 0, l = 0, r = 0;
    for (int i = now_i-1; i >= 0; i--){
        u += mp[i][now_j];
        if (u == 2){
            DFS(i, now_j, cnt+1);
            mp[i][now_j] = true;
            break;
        }
    }
    for (int i = now_i+1; i < n; i++){
        d += mp[i][now_j];
        if (d == 2){
            DFS(i, now_j, cnt+1);
            mp[i][now_j] = true;
            break;
        }
    }
    for (int j = now_j-1; j >= 0; j--){
        l += mp[now_i][j];
        if (l == 2){
            DFS(now_i, j, cnt+1);
            mp[now_i][j] = true;
            break;
        }
    }
    for (int j = now_j+1; j < m; j++){
        r += mp[now_i][j];
        if (r == 2){
            DFS(now_i, j, cnt+1);
            mp[now_i][j] = true;
            break;
        }
    }
}
int main(){
    while (cin >> n >> m){
        ans = 0;
        mp = vector<vector<bool>>(n, vector<bool>(m, true));
        DFS();
        cout << ans << endl;
    }
}