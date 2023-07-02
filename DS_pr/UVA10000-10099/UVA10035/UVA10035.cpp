#include<iostream>
using namespace std;
int main(){
    long long int n,m;
    int put=0;
    while(cin>>n>>m){
        if(n==0 && m==0)
            break;
        put=0;
        int carry=0;
        while(n!=0 || m!=0){
            if(((n%10)+(m%10)+put)>=10){
                put=1;
                carry+=1;
            }
            else{
                put=0;
            }
            n=n/10;
            m=m/10;
        }
        if(carry==0)
            cout<<"No carry operation."<<endl;
        else if(carry==1)
            cout<<"1 carry operation."<<endl;
        else
            cout<<carry<<" carry operations."<<endl;
    }
}