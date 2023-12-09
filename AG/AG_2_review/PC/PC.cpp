#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int x = 0; x < n; x++) {
        int itemN, maxCt;
        cin.ignore();
        string bk;
        getline(cin, bk);
        cin >> itemN >> maxCt;
        vector<int> grid(itemN);
        for (int i = 0; i < itemN; i++) {
            cin >> grid[i];
        }
        sort(grid.begin(), grid.end(), greater<int>());

        int ans = 0;
        vector<int> ckl;
        ckl.push_back(grid[0]);
        for (int i = 1; i < grid.size(); i++) {
            int ck = 1;
            for (int j = 0; j < ckl.size(); j++) {
                if (ckl[j] + grid[i] <= maxCt) {
                    ans++;
                    ckl.erase(ckl.begin() + j);
                    ck = 0;
                    break;
                }
            }
            if (ck) {
                ckl.push_back(grid[i]);
            }
        }
        cout << ans + ckl.size() << endl;
        if (x != n - 1) {
            cout << endl;
        }
    }
    return 0;
}