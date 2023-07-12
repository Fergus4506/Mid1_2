n=int(input())
count=2
allAnimal=[]
for i in range(n):
    allAnimal.append(int(input()))
allAnimal.sort()
minN,maxN=allAnimal[0],allAnimal[len(allAnimal)-1]
leght,right=0,len(allAnimal)-1
while minN!=maxN:
    if maxN>minN:
        leght+=1
        minN+=allAnimal[leght]
    elif minN>maxN:
        right-=1
        maxN+=allAnimal[right]
    count+=1

# print(allAnimal[leght],allAnimal[right])
if leght+1==right:
    if leght==0 and right==len(allAnimal)-1:
        print(allAnimal[leght])
    else:
        print(allAnimal[leght]+1)
else:
    print(allAnimal[leght+1])