#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    while(cin>>n){
        vector<int> list;
        int check=1,last=0;
        for(int i=0;i<n;i++){
            int temp;
            cin>>temp;
            if(i!=0)
                list.push_back(abs(temp-last));
            last=temp;
        }
        if(n==1){
            cout<<"Jolly"<<endl;
            continue;
        }
        sort(list.begin(),list.end());
        last=list[0];
        if(last==0){
            cout<<"Not jolly"<<endl;
            continue;
        }
        for(int i=1;i<list.size();i++){
            if(list[i]!=last+1){
                cout<<"Not jolly"<<endl;
                check=0;
                break;
            }
            last=list[i];
        }
        if(check)
            cout<<"Jolly"<<endl;
        
    }
    
    return 0;
}