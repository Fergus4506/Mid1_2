n=int(input())
i=0
while True:
    try:        
        b=input()
        if i!=0:
            print()
        x=int(input())
        inGrid=[]
        for j in range(x):
            inGrid.append(list(map(int,input().split())))
        c=0
        ans_list=[]
        for j in range(x-1,-1,-1):
            now=inGrid[j][0]+inGrid[j][1]+c
            if now>=10:
                c=1
                now=now%10
            else:
                c=0
            ans_list.append(str(now))
        ans=''.join(ans_list[::-1])
        print(ans)
        i+=1
    except EOFError:
        break
#因為python真的是報幹慢，所以只能用c++寫速度才夠
#所以以下為類似上面概念的C++寫法
# #include<iostream>
# #include<cstdio>
# #include<cstring>
# using namespace std;

# int answer[1000002] = {0};//先設定一個陣列為了存取等等需要用到的程式
# int main(){
#   bool blank_line = 0;//確認換行
#   int N, M, num1, num2;
#   while( scanf( "%d", &N ) != EOF ){//讀EOF是為了讓他停止
#     for( int i = 0 ; i < N ; i++ ){//有幾個測資
    
#       scanf( "%d", &M );
#       memset( answer, 0, sizeof(answer) );//歸零上一個測資所使用的空間
      
#       for( int j = M-1 ; j >= 0 ; j-- ){//倒退抓值(因為最大的第1個輸入)
#         scanf( "%d%d", &num1, &num2 );
#         answer[j] += num1+num2;
#       }
      
#       for( int j = 0 ; j < M ; j++ ){//計算進位
#         answer[j+1] += answer[j]/10;
#         answer[j] %= 10;
#       }
      
#       if( answer[M] ) M++;//確認最大值有無進位存在

#       if( blank_line ) printf( "\n" );//測資間所需的換行
#       blank_line = 1;

#       for( int j = M-1 ; j >= 0 ; j-- )
#         printf( "%d", answer[j] );
        
#       printf( "\n" );
#     }
#   }
#   return 0;
# }