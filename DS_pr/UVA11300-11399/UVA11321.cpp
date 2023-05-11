#include <iostream>
#include <algorithm>
using namespace std;

struct List{
	int num;
	int mod;
	int Even_Odd;
};

List list[10000];

bool cmp(List a,List b){
	if(a.mod==b.mod){
		if(a.Even_Odd==1 && b.Even_Odd==1)
			return a.num>b.num;
		else if(a.Even_Odd==0 && b.Even_Odd==0)
			return a.num<b.num;
		else
			return a.Even_Odd>b.Even_Odd;
	}else
		return a.mod<b.mod;
	
};

int main(){
    int N,M;
	while(cin>>N>>M){
		cout<<N<<" "<<M<<endl;
		if(N==0 && M==0)break;
		for(int i=0;i<N;i++){
			cin>>list[i].num;
			list[i].mod=(list[i].num)%M;
			list[i].Even_Odd=list[i].num%2;
		}
		sort(list,list+N,cmp);
		for(int i=0;i<N;i++){
			cout<<list[i].num<<endl;
		}
		     
	}
	return 0;
}