#include <iostream>
#include <vector>
using namespace std;
int n,m;
int Max=-1;
vector<vector<int>> num(8,vector<int>(8,1));
void jump(int index_i, int index_j, int max_ans){
    int ori_index_i=index_i, ori_index_j=index_j;
    int count=0;
    // for(int i=0;i<n;i++){
    //     for(int j=0;j<m;j++){
    //         cout << num[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    //cout << max_ans <<"\n";
    if(Max < max_ans)
        Max=max_ans;

    while(index_j < m){
        index_j++;
        if(index_j == m)
            break;
        if(count >= 1 && num[index_i][index_j]){
            num[index_i][index_j]=0;
            //cout << "right" << "\n";
            jump(index_i,index_j,max_ans+1);
            num[index_i][index_j]=1;
            break;
        }
        else if(num[index_i][index_j]){
            count++;
        }
    }
    index_i=ori_index_i; index_j=ori_index_j;
    count=0;
    while(index_j >= 0){
        index_j--;
        if(index_j == -1)
            break;
        if(count >= 1 && num[index_i][index_j]){
            num[index_i][index_j]=0;
            //cout << "left" << "\n";
            jump(index_i,index_j,max_ans+1);
            num[index_i][index_j]=1;
            break;
        }
        else if(num[index_i][index_j]){
            count++;
        }
    }
    index_i=ori_index_i; index_j=ori_index_j;
    count=0;
    while(index_i < n){
        //cout << index_i << " " << count << " " << num[index_i][index_j] << "\n";
        index_i++;
        if(index_i == n)
            break;
        if(count >= 1 && num[index_i][index_j]){
            num[index_i][index_j]=0;
            //cout << "down" << "\n";
            jump(index_i,index_j,max_ans+1);
            num[index_i][index_j]=1;
            break;
        }
        if(num[index_i][index_j]){
            count++;
        }
    }
    index_i=ori_index_i; index_j=ori_index_j;
    count=0;
    while(index_i >= 0){
        index_i--;
        if(index_i == -1)
            break;
        if(count >= 1 && num[index_i][index_j]){
            num[index_i][index_j]=0;
            //cout << "up" << "\n";
            jump(index_i,index_j,max_ans+1);
            num[index_i][index_j]=1;
            break;
        }
        else if(num[index_i][index_j]){
            count++;
        }
    }
    count=0;
}
int main(){
    while(cin >> n >> m){
        ios_base::sync_with_stdio(false);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                num[i][j]=1;
            num[0][0]=0;//start

            jump(0,0,0);
            cout << Max << "\n";
            Max=-1;
    }

        // for(int i=0;i<n;i++){
        //     for(int j=0;j<m;j++){
        //         cout << num[i][j] << " ";
        //     }
        //     cout << "\n";
        // }
    //}

    return 0;
}
