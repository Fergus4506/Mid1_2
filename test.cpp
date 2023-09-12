#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    while((cin>>n>>m) && n!=0 && m!=0){
        string temp;
        
        for(int i=0;i<n;i++){
            cin>>temp;
            for(int j=0;j<m;j++){
                cout<<temp[j];
            }
        }
    }
    return 0;
}