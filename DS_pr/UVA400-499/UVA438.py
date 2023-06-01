import math
pi=3.141592653589793
while True:
    try:
        #園內接三角形求圓周長
        n=list(map(float,input().split()))

        #先算三邊邊長
        ab=((n[0]-n[2])**2+(n[1]-n[3])**2)**0.5
        ac=((n[0]-n[4])**2+(n[1]-n[5])**2)**0.5
        bc=((n[2]-n[4])**2+(n[3]-n[5])**2)**0.5

        #匴出其中一點的cos值並利用arcos回推角度
        cosA=(ab*ab+ac*ac-bc*bc)/(2*ab*ac)
        A=math.acos(cosA)
        #角度出來後利用園內接三角形的特性(正弦公式)算出直徑(2r)
        r=bc/math.sin(A)
        print(round(r*pi*100)/100)   

    except EOFError:
        break