n=int(input())
for i in range(n):
	temp=list(map(int,input().split()))
	check=temp[1:]
	ans=[]
	ck=True
	for j in check:
		if len(ans)==0:
			ans.append(j)
		else:
			if ck and ans[len(ans)-1]>j:
				ans.append(j)
				ck=not ck
			elif not ck and ans[len(ans)-1]<j:
				ans.append(j)
				ck=not ck
			else:
				ans.pop()
				ans.append(j)
	print(len(ans))