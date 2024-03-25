maxN,minN=11,-1
while 1:
    # print(minN,maxN)
    number=int(input())
    if number==0:
        break 
    txt=input()
    if txt=="too high":
        maxN=min(maxN,number)
    elif txt=="too low":
        minN=max(minN,number)
    else:
        if number>minN and number<maxN:
            print("Stan may be honest")
            
        else:
            print("Stan is dishonest")
        maxN,minN=11,-1
