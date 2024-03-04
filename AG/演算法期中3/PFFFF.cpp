#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,c=1;  cin >> t;
    while(t--){
        int n,p,q;  cin >> n >> p >> q;
        p++,q++;
        int pp[p],qq[q];
        int index_pp[n*n+1];
        memset(index_pp,0,sizeof(index_pp));
        for(int i=0;i<p;i++){
            cin >> pp[i];
            index_pp[pp[i]]=i;
        }
        for(int i=0;i<q;i++){
            int x;  cin >> x;
            qq[i]=index_pp[x];
        }
        for(auto &v:qq)
            cout << v << " ";
        cout<<endl;
        for(auto &v:index_pp)
            cout << v << " ";
        cout<<endl;
        vector<int> dp;
        dp.push_back(qq[0]);
        for(int i=1;i<q;i++){
            if(dp.back()<qq[i])
                dp.push_back(qq[i]);
            else
                *lower_bound(dp.begin(),dp.end(),qq[i])=qq[i];
        }
        cout << "Case " << c << ": " << dp.size() << "\n";
        c++;
    }

    return 0;
}
