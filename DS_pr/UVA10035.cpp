#include <iostream>
#include <string>
using namespace std;
int main(){
	string n,m;
	while(cin>>n>>m){
		int up=0,count=0,ans=0;
		while(count>=n.length() && count!=m.length()){
			int temp=up;
			if(count<n.length())
				temp+=int(n[count]);
			if(count<m.length())
				temp+=int(m[count]);
			if(temp>=10){
				up=1;
				ans+=1;
			}else
				up=0;
		}
		if(ans==0)
			cout<<"No carry operation.\n";
		else if(ans==1)
			cout<<"1 carry operation.\n";
		else
			cout<<ans<<" carry operations.\n";
	}
	return 0;
}