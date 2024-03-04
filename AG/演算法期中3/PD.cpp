#include <iostream>
#include <vector>
#include <set>

using namespace std;
set<string> ans;
string s1,s2;
void func(vector<vector<int>> dp, int s1_size, int s2_size, string s_ans){
    cout << s1_size << " " << s2_size << "\n";
    while(s1_size > 0 && s2_size >0){
        if(s1[s1_size-1] == s2[s2_size-1]){
            s_ans = s1[s1_size-1] + s_ans;
            s1_size--,s2_size--;
        }
        else if(dp[s1_size-1][s2_size] > dp[s1_size][s2_size-1]){
            s1_size--;
        }
        else if(dp[s1_size-1][s2_size] < dp[s1_size][s2_size-1]){
            s2_size--;
        }
        else{
            func(dp, s1_size-1, s2_size, s_ans);
            func(dp, s1_size, s2_size-1, s_ans);
            // cout << s1_size << " " << s2_size << "\n";
            return;

        }

    }
    ans.insert(s_ans);

}

int main(){
    ios_base::sync_with_stdio(false);
    while(cin >> s1 >> s2){
        int s1_size = s1.size();
        int s2_size = s2.size();
        vector<vector<int>> dp(s1_size+1,vector<int>(s2_size+1,0));
        for(int i=1;i<=s1_size;i++){
            for(int j=1;j<=s2_size;j++){
                if(s1[i-1] == s2[j-1])
                    dp[i][j] = dp[i-1][j-1]+1;
                else
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]);
            }
        }

        // for(int i=0;i<=s1_size;i++){
        //     for(int j=0;j<=s2_size;j++){
        //         cout << dp[i][j] << " ";
        //     }
        //     cout << "\n";
        // }
        //cout << "\n";
        func(dp, s1_size, s2_size, "");
        for(auto &v: ans){
            cout << v << "\n";
        }
        ans.clear();

    }

    return 0;
}

/*
agcat
gac
      a g c a t
    0 0 0 0 0 0
g   0 0 1 1 1 1
a   0 1 1 1 2 2
c   0 1 1 2 2 2
    0
ac
ga
gc

*/
