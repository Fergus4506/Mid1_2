#include<iostream>
#include<vector>
using namespace std;
int ans=-1;
int jump(vector<vector<int > >num, int n, int m , int index_i, int index_j, int count){
    int right_count=0, left_count=0, up_count=0, down_count=0;
    int original_index_j=index_j, original_index_i=index_i;

    if(ans < count)
        ans=count;
//     for(int i=0;i<n;i++){
//         for(int j=0;j<m;j++)
//             cout << num[i][j] <<" ";
//         cout << endl;
//     }
    // cout << count << endl << endl;
    while(index_j < m){   //to_right
        index_j++;
        if(index_j >= m)
            break;
        if(right_count > 0 && num[index_i][index_j] == 1){
            num[index_i][index_j] = 0;//new index

            jump(num, n, m , index_i, index_j, ++count);
            num[index_i][index_j] = 1;//back
            index_j = original_index_j;
            count--;
            break;
        }
        if(num[index_i][index_j]){
            right_count++;
        }

    }
    index_i = original_index_i;
    index_j = original_index_j;
    while(index_j >= 0){   //to_left
        index_j--;
        if(index_j == -1)
            break;
        if(left_count > 0 && num[index_i][index_j] == 1){
            num[index_i][index_j] = 0;//new index

            jump(num, n, m , index_i, index_j, ++count);
            num[index_i][index_j] = 1;//back
            index_j = original_index_j;
            count--;
            break;
        }
        if(num[index_i][index_j]){
            left_count++;
        }

    }
    index_i = original_index_i;
    index_j = original_index_j;
    while(index_i < n){   //to_down
        index_i++;
        if(index_i == n)
            break;
        if(down_count > 0 && num[index_i][index_j] == 1){
            num[index_i][index_j] = 0;//new index
            jump(num, n, m , index_i, index_j, ++count);
            num[index_i][index_j] = 1;//back
            index_i = original_index_i;
            count--;
            break;
        }
        if(num[index_i][index_j]){
            down_count++;
        }

    }
    index_i = original_index_i;
    index_j = original_index_j;
    while(index_i >= 0){   //to_up
        index_i--;
        if(index_i == -1)
            break;
        if(up_count > 0 && num[index_i][index_j] == 1){
            num[index_i][index_j] = 0;//new index

            jump(num, n, m , index_i, index_j, ++count);
            num[index_i][index_j] = 1;//back
            index_i = original_index_i;
            count--;
            break;
        }
        if(num[index_i][index_j]){
            up_count++;
        }

    }
    // for(int i=0;i<n;i++){
    //     for(int j=0;j<m;j++)
    //         cout << num[i][j] <<" ";
    //     cout << endl;
    // }
    // cout << count << endl << endl;
    return 0;
}


int main(){
    int n,m;
    for(int k=1;k<7;k++)
        for(int l=1;l<7;l++){
        n=k,m=l;
        cout << n << " " << m << "\n";
        ans=-1;
        vector<vector<int > > num(n,vector<int>(m,1));
        num[0][0]=0;

        jump(num, n, m , 0, 0 ,0);

        // for(int i=0;i<n;i++){
        //     for(int j=0;j<m;j++)
        //         cout << num[i][j] <<" ";
        //     cout << endl;
        // }
        cout << ans << endl;
    }
    return 0;
}
