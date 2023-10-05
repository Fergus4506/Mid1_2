// #include <iostream>
// using namespace std;
// inline long long int gcd(long long int a,long long int b) {
//     return b>0 ? gcd(b,a%b):a;
// }
// int main(){
//     int count=1;
//     while(1){
//         long long int v1,v2,d1,d2;
//         cin>>v1>>d1>>v2>>d2;
//         if(v1 && d1 && v2 && d2){
//             if(float(d1)/float(v1)>=float(d2)/float(v2))
//                 cout<<"Case #"<<count<<": No beer for the captain."<<endl;
//             else
//                 cout<<"Case #"<<count<<": You owe me a beer!"<<endl;
//             long long int avg=d1*v2+d2*v1;
//             long long int time=2*v2*v1;
//             long long int a=gcd(avg,time);
//             if(time/a!=1){
//                 cout<<"Avg. arrival time: "<<avg/a<<"/"<<time/a<<endl;
//             }
//             else{
//                 cout<<"Avg. arrival time: "<<avg/time<<endl;
//             }
//         }
//         else{
//             break;
//         }
//         count++;
//     }
//     return 0;
// }
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
using namespace std;
long long int gcd(long long int a,long long int b)
{
     return b?gcd(b,a%b):a;
}
int main()
{
    long long int v1,d1,v2,d2,cas=1;
    while(cin>>v1>>d1>>v2>>d2 && (v1!=0||v2!=0||d1!=0||d2!=0))
    {
        long long int a=d1*v2,b=d2*v1;
        if(a<b) printf("Case #%lld: You owe me a beer!\n",cas++);
        else if(a>b) printf("Case #%lld: No beer for the captain.\n",cas++);
        long long int time=d1*v2+d2*v1,mo=v1*v2*2;          
        long long int div=gcd(time,mo);
        long long int s=time/div,m=mo/div;
        if(m==1)  printf("Avg. arrival time: %lld\n",s);
        else printf("Avg. arrival time: %lld/%lld\n",s,m);
    }
    return 0;
}