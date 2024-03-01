#include<iostream>
#include<vector>
#include<string>
#include<cstring>
using namespace std;
int main(){
    int sp;
    int first;
    int ck=0;
    while(cin>>first){
        if(ck){
            printf("\n");
        }
        vector<int> number;
        number.push_back(first);
        int temp;
        for(int i=0;i<5;i++){
            cin>>temp;
            number.push_back(temp);
        }
        cin>>temp;
        sp=temp;
        int n;
        cin>>n;
        for(int i=0;i<n;i++){
            int num=0,spcheck=0;
            for(int j=0;j<6;j++){
                cin>>temp;
                if(temp==sp){
                    spcheck=1;
                    continue;
                }
                for(auto trg: number){
                    if(temp==trg){
                        // cout<<temp<<" "<<trg<<endl;
                        num+=1;
                        break;
                    }
                }
            }
            // cout<<num<<" "<<spcheck<<endl; 
            if(num==6){
                cout<<"Ticket "<<i+1<<": 1st prize"<<endl;
            }else if(num==5 && spcheck==1){
                cout<<"Ticket "<<i+1<<": 2nd prize"<<endl;
            }else if(num==5){
                cout<<"Ticket "<<i+1<<": 3rd prize"<<endl;
            }else if(num==4 && spcheck==1){
                cout<<"Ticket "<<i+1<<": 4th prize"<<endl;
            }else if(num==4){
                cout<<"Ticket "<<i+1<<": 5th prize"<<endl;
            }else if(num==3 && spcheck==1){
                cout<<"Ticket "<<i+1<<": 6th prize"<<endl;
            }else if(num==2 && spcheck==1){
                cout<<"Ticket "<<i+1<<": 7th prize"<<endl;
            }else if(num==3){
                cout<<"Ticket "<<i+1<<": general prize"<<endl;
            }else{
                cout<<"Ticket "<<i+1<<": lose"<<endl; 
            } 
        }
        ck=1;
    }
    return 0;
}