#include"bits/stdc++.h" // using "" instead of <>, so it will search locally for the precompiled version first
using namespace std; 
void solve(); 
int main() 
{
    solve();
    return 0; 
} 

// BFS基礎應用，利用queue將每一個點的子節點算過後在往下走
// 換句話說只要一找到符合條件的點那點就是最短路徑長
// 因為要符合一層一層算的模式所以需要等這層的節點都判斷完後再去更新最大長度和queue的值
// 並且要注意因為這題為無向圖所以不能讓他跑進迴圈中，當判斷到要準備跑到以跑過的節點時就要忽略該資料
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