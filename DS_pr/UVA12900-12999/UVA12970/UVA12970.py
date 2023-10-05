import math
# cont=1
# while 1:
#     v1,d1,v2,d2=map(int,input().split())
#     if v1==0 and d1==0 and v2==0 and d2==0:
#         break
#     if d1/v1 < d2/v2:
#         print("Case #%d: You owe me a beer!"%(cont))
#     else:
#         print("Case #%d: No beer for the captain."%(cont))
#     avg=d1*v2+v1*d2
#     time=v1*v2*2
#     if avg%(time):
#         a=math.gcd(avg,time)
#         avg=avg//a
#         time=time//a
#         print("Avg. arrival time: %d/%d"%(avg,time))
#     else:
#         print("Avg. arrival time: %d"%(int(avg/time)))
#     cont+=1
count=1
while 1:
    v1,d1,v2,d2=map(int,input().split())
    if d1 and d2 and v1 and v2:
        a=v2*d1
        b=v1*d2
        if a > b:
            print("Case #%d: No beer for the captain."%(count))
        elif a<b:
            print("Case #%d: You owe me a beer!"%(count))
        avg=d1*v2+d2*v1
        time=2*v2*v1
        a=math.gcd(avg,time)
        if time/a==1:
            print("Avg. arrival time: %d"%(int(avg/time)))
        else:
            print("Avg. arrival time: %d/%d"%(avg//a,time//a))
        count+=1
    else:
        break

