#include"bits/stdc++.h" // using "" instead of <>, so it will search locally for the precompiled version first
using namespace std; 
void solve(); 
int main() 
{
    solve();
    return 0; 
} 
void solve() 
{
    // Unweigted SSSDSP: basic level bfs. Here the solution of the max color changes is shortestPath - 1
    int n, m; cin >> n >> m;
    vector<vector<int>> AL(n, vector<int>());
    for(int i=0;i<m;i++){
        int a, b; cin >> a >> b;
        a--; b--;
        AL[a].push_back(b);
        AL[b].push_back(a);
    }
    vector<int> q{0};
    vector<bool> seen(n, false);
    seen[0] = true;
    int shortestPath = 0;
    while(q.size()){
        vector<int> nq;
        for(int cur: q){
            if(cur == n-1){
                cout << shortestPath-1;
                return;
            }
            for(int next:AL[cur]){
                if(seen[next] == false){
                    seen[next] = true;
                    nq.push_back(next);
                }
            }
        }
        shortestPath++;
        q = nq;
    }

}