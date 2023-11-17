#include<bits/stdc++.h>
using namespace std;
int main(){
    
    long long int m,n,k;
    while(cin>>m>>n>>k){
        long long int mg[m];
        long long int ng[n];
        for(int i=0;i<m;i++){
            cin>>mg[i];
        }
        for(int i=0;i<n;i++){
            cin>>ng[i];
        }
        sort(mg,mg+m);
        sort(ng,ng+n);
        long long int ans=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(mg[i]+ng[j]==k)
                    ans+=1;
                else if(mg[i]+ng[j]>k)
                    break;
            }
        }
        cout<<ans<<endl;
    } 
    
    return 0;
}