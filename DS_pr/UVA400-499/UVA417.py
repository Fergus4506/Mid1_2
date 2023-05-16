grid=[]
for i in range(26):
    grid.append(chr(ord('a')+i))
def makegrid(last,len,ans):
    if len==0:
        grid.append(ans)
        return
    if last=="":
        for i in range(ord('a'),ord('z')+1):
            makegrid(chr(i),len,ans+chr(i))
    else:
        for i in range(ord(last)+1,ord('z')+1):
            makegrid(chr(i),len-1,ans+chr(i))
for i in range(5):
    makegrid("",i,"")
grid.pop(grid.index(""))
while True:
    try:
        n=input()
        try:
            print(grid.index(n)+1)
        except ValueError:
            print(0)
    except EOFError:
        break