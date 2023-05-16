for i in range(2,200+1):
    for j in range(2,i):
        for z in range(j,i):
            for x in range(z,i):
                if i**3==j**3+z**3+x**3:
                    print("Cube = %d, Triple = (%d,%d,%d)"%(i,j,z,x))
                    break
#硬炸法->會超時需用cpp