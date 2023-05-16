// #include <iostream>
// #include <math.h>
// using namespace std;
// int main(){
//     for(int i=2;i<=200;i++){
//         for(int j=2;j<=200;j++){
//             for(int z=j;z<=200;z++){
//                 for(int x=z;x<=200;x++){
//                     int temp=pow(i,3);
//                     int check=pow(j,3)+pow(z,3)+pow(x,3);
//                     if(temp==check)
//                         cout<<"Cube = "<<i<<", Triple = ("<<j<<","<<z<<","<<x<<")"<<endl;
//                 }
//             }
//         }
//     }
// }
//不用pow函式的形況下速度差很多->函式庫在這裡會減緩執行速度
#include <iostream>
using namespace std;

int main(){
  for( int a = 2 ; a <= 200 ; ++a ){
    for( int b = 2 ; b < a ; ++b ){
      for( int c = b ; c < a ; ++c ){
        for( int d = c ; d < a ; ++d ){
          if( a*a*a == b*b*b + c*c*c + d*d*d ){
            cout<<"Cube = "<<a<<", Triple = ("<<b<<","<<c<<","<<d<<")"<<endl;
          }
        }
      }
    }
  }
  return 0;
}
