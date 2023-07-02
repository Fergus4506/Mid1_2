n=list(map(int,input().split()))
ground=[[0]*(n[0]+1) for i in range(n[1]+1)]
w=["N","E","S","W"]
while True:
	try:
		start=input().split()
	except:
		break
	inX=int(start[0])
	inY=int(start[1])
	inW=start[2]
	order=input()
	lost=True
	#print(ground)
	for i in range(len(order)):
		#print("%d %d %s"%(inX,inY,str(inW)))
		lost=True
		check=True
		if order[i]=='R':
			for j in range(3):
				if inW==w[j]:
					inW=w[j+1]
					check=False
					break
			if inW==w[3] and check:
				inW=w[0]
		elif order[i]=="L":
			for j in range(1,4):
				if inW==w[j]:
					inW=w[j-1]
					check=False
					break
			if inW==w[0] and check:
				inW=w[3]
		elif order[i]=="F":
			if inW=="N":
				if inY+1>n[1] and ground[inY][inX]==0:
					ground[inY][inX]=-1
					lost=False
					print("%d %d %s LOST"%(inX,inY,str(inW)))
					break
				elif ground[inY][inX]!=-1:
					inY=inY+1
				elif ground[inY][inX]==-1 and inY+1<=n[1]:
					inY=inY+1	
			elif inW=="E":
				if inX+1>n[0] and ground[inY][inX]==0:
					ground[inY][inX]=-1
					lost=False
					print("%d %d %s LOST"%(inX,inY,str(inW)))
					break
				elif ground[inY][inX]!=-1:
					inX=inX+1
				elif ground[inY][inX]==-1 and inX+1<=n[0]:
					inX=inX+1
			elif inW=="S":
				if inY-1<0 and ground[inY][inX]==0:
					ground[inY][inX]=-1
					lost=False
					print("%d %d %s LOST"%(inX,inY,str(inW)))
					break
				elif ground[inY][inX]!=-1:
					inY=inY-1
				elif ground[inY][inX]==-1 and inY-1>=0:
					inY=inY-1
			elif inW=="W":
				if inX-1<0 and ground[inY][inX]==0:
					ground[inY][inX]=-1
					lost=False
					print("%d %d %s LOST"%(inX,inY,str(inW)))
					break
				elif ground[inY][inX]!=-1:
					inX=inX-1
				elif ground[inY][inX]==-1 and inX-1>=0:
					inX=inX-1	

			
	if lost:
		print("%d %d %s"%(inX,inY,str(inW)))