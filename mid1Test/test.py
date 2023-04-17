# #給定一個範圍(x,y)，根據方位然後移動若超出範圍，機器人會掉下去並會在超出前的格子標記，往後的機器人若到此格子，則無視掉下去的指令
# def direction(instruction,side):
# 	if side=="E":
# 		if instruction=="R":
# 			return "S"
# 		elif instruction=="L":
# 			return "N"
# 	elif side=="W":
# 		if instruction=="R":
# 			return "N"
# 		elif instruction=="L":
# 			return "S"
# 	elif side=="N":
# 		if instruction=="R":
# 			return "E"
# 		elif instruction=="L":
# 			return "W"
# 	elif side=="S":
# 		if instruction=="R":
# 			return "W"
# 		elif instruction=="L":
# 			return "E"

# x,y=map(int,input().split())
# world= [[1 for i in range(x+1)] for j in range(y+1)]
# #print(world)
# while True:
# 	try:
# 		initialX,initialY,side=input().strip(" ").split()
# 		instructions=input()
# 		initialX=int(initialX)
# 		initialY=int(initialY)
# 		subX,subY,check,subside=0,0,0,""
# 		for i in range(len(instructions)):
# 			#print("%d %d %s"%(initialX,initialY,side))
# 			if instructions[i]!=" ":
# 				subside=side
# 				subX=initialX
# 				subY=initialY
# 				if instructions[i]=="R" or instructions[i]=="L":
# 					side=direction(instructions[i],side)
# 				else:
# 					if side=="E":
# 						initialX+=1
# 					elif side=="W":
# 						initialX-=1
# 					elif side=="N":
# 						initialY+=1
# 					elif side=="S":
# 						initialY-=1
# 				print("%d %d"%(subX,subY))
# 				if initialX>x or initialX<0 or initialY>y or initialY<0:
# 					if world[subY][subX]!=0:
# 						world[subY][subX]=0
# 						check=1
# 						break
# 					else:
# 						initialX=subX
# 						initialY=subY

# 		if check==1:
# 			print("%d %d %s LOST"%(subX,subY,subside))
# 		else:
# 			print("%d %d %s"%(initialX,initialY,side))
# 	except EOFError:
# 		break

# 計算每個輸入出現的概率，並用name的ascii大小印出
# while True:
# 	try:
# 		n=int(input())
# 		for k in range(n):
# 			if k==0:#注意這該死的空格，只會輸入一次
# 				space=input()
# 			trees=[]
# 			#print(space)
# 			while True:
# 				try:
# 					tree=input()
# 					if tree=="":
# 						break
# 					trees.append(tree)
# 				except:
# 					break
# 			#print(trees)
# 			ans=[]
# 			temp=[]
# 			for i in range(len(trees)):
# 				if trees[i] not in temp:
# 					temp.append(trees[i])
# 					count=trees.count(trees[i])
# 					ans.append([trees[i],count/len(trees)*100])
# 			ans.sort(key=lambda ans:ans[0])
# 			for i in range(len(ans)-1):
# 				print("%s %.4f"%(ans[i][0],ans[i][1]))
# 			print("%s %.4f"%(ans[-1][0],ans[-1][1]))
# 			if k!=n-1:
# 				print()
# 	except EOFError:
# 		break

# 輸入一十進位數，計算其二進位和十六進位有多少個1
# while True:
# 	try:
# 		n=int(input())
# 		for i in range(n):
# 			m=int(input())
# 			subm=m
# 			bs=0
# 			hm=0
# 			count=0
# 			while subm>0:
# 				if subm%2==1:
# 					count+=1
# 				subm=subm//2
# 			print(count,end=" ")
# 			count=0
# 			while m>0:
# 				temp=m%10
# 				while temp>0:
# 					if temp%2==1:
# 						count+=1
# 					temp=temp//2
# 				m=m//10
# 			print(count)
# 	except EOFError:
# 		break


# while True:
# 	try:
# 		case=int(input())
# 		for i in range(case):
# 			day=int(input())
# 			p=int(input())
# 			hartal=[]
# 			for j in range(p):
# 				h=int(input())
# 				for k in range(1,day+1):
# 					if h*k>day:
# 						break
# 					else:	
# 						hartal.append(h*k)
# 			count=0
# 			temp=[]
# 			for l in range(len(hartal)):
# 				same=hartal.count(hartal[l])
# 				if hartal[l] not in temp:
# 					temp.append(hartal[l])
                    
# 			for a in temp:
# 				if a%7!=0 and a%7!=6:
# 					count+=1
# 			print(count)	
# 	except EOFError:
# 		break

def feyman(num):
    if num==1:
        return 1
    else:
        return num*num+feyman(num-1)
while True:
    try:
        n=int(input())
        if n==0:
            break
        print(feyman(n))
    except:
        break
#!/bin/bash