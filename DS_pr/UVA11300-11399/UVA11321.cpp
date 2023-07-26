#include<bits/stdc++.h>
using namespace std;

struct sp{
	int ts;
	int m_mod;
	int odd_even;
};

bool cmp(sp a,sp b){//sort return false才會交換
	if(a.m_mod==b.m_mod){
		if(a.odd_even!=b.odd_even)
			return a.odd_even>b.odd_even;
		else if(a.odd_even==1 && b.odd_even==1)
			return a.ts>b.ts;
		else
			return a.ts<b.ts;
	}else{
		return a.m_mod<b.m_mod;
	}

}

int main(){
	int n,m;
	while(1){
		cin>>n>>m;
		cout<<n<<" "<<m<<endl;
		if(n==0 && m==0)
			break;
		vector<sp> list;
		for(int i=0;i<n;i++){
			sp temp;
			cin>>temp.ts;
			temp.m_mod=temp.ts%m;
			temp.odd_even=abs(temp.ts%2);
			list.push_back(temp);
		}
		sort(list.begin(),list.end(),cmp);

		for(int i=0;i<n;i++){
			cout<<list[i].ts<<endl;
		}
		
	}
	
	
	return 0;
}