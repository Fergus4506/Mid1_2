#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool is_prime(int num){
    if(num<=1)
        return false;
    if(num<=3)
        return true;
    if(num%2==0)
        return false;
    for(int i=3;i*i<=num;i+=2)
        if(num%i==0)
            return false;
    return true;
}
int main(){
    int n;
    string map="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    int Case=1;
    cin >> n;
    while(n--){
        vector<int> count(100);
        string s;
        cin >> s;
        for(int i=0;i<s.size();i++){
            //cout << s[i] ;
            if(s[i]>='0' && s[i]<='9')
                count[s[i]-'0']++;
            else if(s[i]>='A' && s[i]<='Z')
                count[s[i]-'A'+10]++;
            else
                count[s[i]-'a'+36]++;
        }
        cout << "Case " << Case << ": ";
        Case++;
        bool empty=true;
        for(int i=0;i<62;i++){
            if(is_prime(count[i])){
                cout << map[i];
                empty=false;
            }

        }
        if(empty)
            cout << "empty";

        cout << endl;
    }


    return 0;
}

/*
0123456789BCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz
Sample Input
3
ABCC
AABBBBDDDDD
ABCDFFFF
Sample Output
Case 1: C
Case 2: AD
Case 3: empty
*/
