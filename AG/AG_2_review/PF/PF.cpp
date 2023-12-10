#include<bits/stdc++.h>
using namespace std;

bool compare(vector<float> a,vector<float> b){
    return a[0]>b[0];
}

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int num;
        cin>>num;
        vector<vector<float>> grid;
        for(int j=0;j<num;j++){
            vector<float> temp;
            float d,s;
            cin>>d>>s;
            temp.push_back(s/d);
            temp.push_back(j+1);
            grid.push_back(temp);
        }
        sort(grid.begin(),grid.end(),compare);
        for(int j=0;j<num;j++){
            if(j+1==num)
                cout<<grid[j][1]<<endl;
            else
                cout<<grid[j][1]<<" ";
        }
    }
    return 0;
}