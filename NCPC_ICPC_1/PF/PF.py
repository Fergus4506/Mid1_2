n=int(input())
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
        right+=1
        maxN+=allAnimal[right]
print(allAnimal[leght]+1)