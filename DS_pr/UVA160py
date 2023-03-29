grid=[]
for i in range(2,100):
	check=True
	for j in range(2,int(i**0.5)):
		if i%j==0:
			check=False
			break
	if check:
		grid.append(i)
while True:
	try:
		n=int(input())
		temp=1
		if n==0:
			break
		for i in range(1,n+1):
			temp=temp*i
		ans=[]
		count=0
		last=0
		start=False
		while temp!=1:
			check=True
			while temp%grid[count]==0 and temp!=0:
				check=False
				if grid[count]!=last:
					ans.append(1)
					last=grid[count]
				elif grid:
					ans[len(ans)-1]+=1
				temp=temp//grid[count]
			if check and False:
				ans.append(0)
			count+=1
		print("{:3d}! =".format(n),end="")
		for i in range(len(ans)):
			if i==14:
				print("{:3d}".format(ans[i]))
				if i+1!=len(ans):
					print("      ",end="")
			else:
				print("{:3d}".format(ans[i]),end="")
		if i!=14:
			print()
					
					
					
	except EOFError:
		break