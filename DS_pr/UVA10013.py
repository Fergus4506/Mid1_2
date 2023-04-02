n=int(input())
for i in range(n):
	b=input()
	if i!=0:
		print()
	x=int(input())
	inGrid=[]
	for j in range(x):
		inGrid.append(list(map(int,input().split())))
	c=0
	ans_list=[]
	for j in range(x-1,-1,-1):
		now=inGrid[j][0]+inGrid[j][1]+c
		if now>=10:
			c=1
			now=now%10
		else:
			c=0
		ans_list.append(str(now))
	ans=''.join(ans_list[::-1])
	print(ans)