#優先順序排序題:
#先考慮哪一個排序規則最明顯，因為最明顯的規則通常為優先序最高，也就是影響範圍最大，要最後再去做排序
#歸類完排序規則的優先順序後以優先序最低的開始做->用sort一步一步做上去
#最後得出的結論就為答案
while True:
	n,m=map(int,input().split())
	print("%d %d"%(n,m))
	if n==0 and m==0:
		break
	grid=[]
	for i in range(n):
		temp=int(input())
		tM=abs(temp)%m#餘數在負數時會以不同於一般除法規則的方式呈現，所以要加絕對值以將餘數正常化
		if temp<0:
			grid.append([temp,tM*-1,temp%2])
		else:
			grid.append([temp,tM,temp%2])

	temp1=[]
	for i in range(n):
		if grid[i][2]!=0:
			temp1.append(grid[i])
	temp1.sort(key=lambda temp1:temp1[0],reverse=1)
	#print(temp1)
	
	temp2=[]
	for i in range(n):
		if grid[i][2]==0:
			temp2.append(grid[i])
	temp2.sort(key=lambda temp2:temp2[0])
	#print(temp2)
	
	grid=temp1[:]+temp2[:]
	grid.sort(key=lambda grid:grid[1])
	for i in range(n):
		print(grid[i][0])