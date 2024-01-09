#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool is_prime(int n){
    if(n<=1)
        return false;
    if(n<=3)
        return true;
    if(n%2==0)
        return false;
    for(int i=3;i * i <= n;i+=2){
        if(n%i==0)
            return false;
    }
    return true;
}
void Bidirectional(vector<int> ans, vector<int> number, int n, int pre_number){
    if(ans.size()==n){
        if(is_prime(ans[n-1]+1)){
            for(auto &v:ans)
                cout << v << " ";
            cout << endl;
            ans.clear();
            ans.push_back(1);

        }
    }
    for(int i=2;i<=n;i++){
        if(number[i]==1)
            if(is_prime(pre_number+i)){
                ans.push_back(i);
                number[i]=0;
                Bidirectional(ans,number,n,i);
                ans.pop_back();
                number[i]=1;
            }
    }

}
int main(){
    int n;
    int Case=1;
    while(cin >> n){
        vector<int> number(n+1,1);
        vector<int> ans;
        ans.push_back(1);
        cout << "Case " << Case << ":" << endl;
            Case++;
        Bidirectional(ans,number,n,1);
        cout << endl;

    }
    return 0;
}

/*
6
8
Case 1:
1 4 3 2 5 6
1 6 5 2 3 4
Case 2:
1 2 3 8 5 6 7 4
1 2 5 8 3 4 7 6
1 4 7 6 5 8 3 2
1 6 7 4 3 8 5 2
*/
