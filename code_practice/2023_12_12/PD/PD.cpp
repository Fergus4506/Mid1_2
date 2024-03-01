
#include<stdio.h>
#define LL long long
#define mod 1000000007
int main(void)
{
	LL now, sum, m, ans;
	int T, i, n, a, b, j, cas = 1;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		ans = m = 1;
		for(i=1;i<=n;i++)
		{
			scanf("%d%d", &a, &b);
			now = sum = 1;
			for(j=1;j<=b;j++)
			{
				now = now*a%mod;
				sum = (now+sum)%mod;
                printf("now: %lld sum: %lld\n",now, sum);
			}
			sum = (sum+b*now)%mod;
			m = m*now%mod;
			ans = ans*sum%mod;
            printf("now: %lld sum: %lld ans: %lld\n",now, sum,ans);
		}
		ans = (ans+m)%mod;
		printf("Case %d: %lld\n", cas++, ans);
	}
	return 0;
}
