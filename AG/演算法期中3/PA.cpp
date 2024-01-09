#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    int n;
    while(cin >> n){
        if(!n)
            break;
        vector<int> x(n);
        vector<int> y(n);
        for(int i=0;i<n;i++){
            cin >> x[i] >> y[i];
        }
        sort(y.begin(),y.end());
        long long int mid;
        long long int count=0;

        mid=y[(n-1)/2];
        for(auto &v:y)
            count+=abs(mid-v);
        cout << mid << " " << count << endl;
    }

    return 0;
}

/*
5
1 2
3 4
5 6
7 8
9 10
*/
