#include <iostream>
#include <vector>

using namespace std;
int main(){
    int n;
    cin >> n;
    while(n--){
        int m,count=0;
        cin >> m;
        vector<int> num(m);
        for(int i=0;i<m;i++)
            cin >> num[i];
        for(int i=0;i<m;i++){
            for(int j=0;j<m-i-1;j++){
                if(num[j] > num[j+1]){
                    int tame = num[j];
                    num[j] = num[j+1];
                    num[j+1] = tame;
                    count++;
                }
            }
        }
        cout << count << "\n";
        // for(auto &v:num)
        //     cout << v << " ";
    }

    return 0;
}
