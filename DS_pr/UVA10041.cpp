#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int len;
		cin>>len;
		int all[len];
		for(int j=0;j<len;j++){
			cin>>all[j];
		}
		sort(all,all+len);
		int ans,p;
		if(len%2==0)
			p=len/2-1;
		else
			p=len/2;
		int check=all[p];
		for(int j=0;j<len;j++){
			ans+=abs(all[j]-check);
		}
		cout<<ans<<endl;
	}
	return 0;
}