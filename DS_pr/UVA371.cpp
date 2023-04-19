#include<iostream>

using namespace std;

int ack(long long int n){
    if(n==1)return 1;
    if(n%2==0)
        return ack(n/2)+1;
    else
        return ack(n*3+1)+1;
}

int main(){
    long long int L,H;
    while(scanf("%lld%lld",&L,&H)!=EOF && L!=0 && H!=0){
        if(L>H)swap(L,H);
        int maxL=0;
        long long maxN=0;
        for(long long int i=L;i<=H;i++){
            int temp=ack(i)-1;
            if(temp>maxL){
                maxL=temp;
                maxN=i;
            }
        }
        printf("Between %lld and %lld, %lld generates the longest sequence of %d values.\n", L, H, maxN, maxL);
    }
    return 0;
}