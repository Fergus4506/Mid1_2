#include <iostream>
using namespace std;
int main(){
    int start;
    while(cin>>start){
        int grid[9];
        grid[0]=start;
        for(int i=1;i<9;i++){
            cin>>grid[i];
        }
        int checkstart=0;
        for(int i=0;i<9;i++){
            if(grid[i]!=0){
                if(checkstart){
                    if(grid[i]<0)
                        cout<<" -";
                    else
                        cout<<" +";
                    if(abs(grid[i])!=1 || i==8)
                        cout<<" "<<abs(grid[i]);
                    else
                        cout<<" ";
                    if(i==7)
                        cout<<"x";
                    else if(i<7)
                        cout<<"x^"<<9-i-1;
                }else{
                    checkstart=1;
                    if(grid[i]<0)
                        cout<<"-";
                    if(abs(grid[i])!=1 || i==8)
                        cout<<abs(grid[i]);
                    if(i==7)
                        cout<<"x";
                    else if(i<7)
                        cout<<"x^"<<9-i-1;
                }
            }
        }
        if(checkstart==0)
            cout<<0;
        cout<<endl;
    }
    
    return 0;
}