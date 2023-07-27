#include <bits/stdc++.h>
using namespace std;
int main(){ 
	string s;
    int count=0;
	while(getline(cin,s)){
        if(count)
            cout<<endl;
		int ans[128]={0};
		for(int i=0;i<s.size();i++){
			ans[int(s[i])]+=1;
		}

        int max=0;

        for(int i=31;i<128;i++){
            if(ans[i]>max)
                max=ans[i];
        }
        int check=1;
        int now=1;
        while(check){
            if(now==max)
                check=0;
            for(int i=127;i>-1;i--){
                if(ans[i]==now)
                    cout<<i<<" "<<ans[i]<<endl;
            }
            now+=1;
            
        }
		count+=1;
	}

	return 0;
}