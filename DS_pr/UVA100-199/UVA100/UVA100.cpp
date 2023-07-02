#include <iostream>
using namespace std;
int main(){
	int n,m;
	while(cin>>n>>m){
        cout<<n<<" "<<m<<" ";
		if(n>m){
			int t=n;
			n=m;
			m=t;
		}
		int max=0;
		for(int i=n;i<=m;i++){
			int temp=i,count=1;
			while(temp!=1){
				if(temp%2)
					temp=temp*3+1;
				else
					temp=temp/2;
				count+=1;
			}
			if(count>max)
				max=count;
		}
		cout<<max<<endl;
	}
}