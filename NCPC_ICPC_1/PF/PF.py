n=int(input())
allAnimal=[]
for i in range(n):
    allAnimal.append(int(input()))
allAnimal.sort()
print(*allAnimal)
maxNumber=allAnimal[len(allAnimal)-1]
sumGrid=[]
temp=0
for i in range(len(allAnimal)):
    temp+=allAnimal[i]
    sumGrid.append([temp,allAnimal[i]])
print(sumGrid)