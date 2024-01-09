#這部分的函式為輾轉相除法找反元素的部分
#利用輾轉相除中gcd(a,b)=sa+tb的部分來解決找尋互質的數字
#其中的S也就是下面變數的X1=>也就是算到最後對於a的反元素
def mod_inverse(a, b):
    m0, x0, x1 = b, 0, 1
    while a > 1:
        q = a // b
        b, a = a % b, b
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def find_n_and_d(p, q, e):
    n = p * q
    f_n = (p - 1) * (q - 1)

    d = mod_inverse(e, f_n)

    return n, d

def encrypt(ms, e, n):
    chrGrid = []
    t1=0
    t2=0
    ct=0
    if len(ms)%2!=0:
        ms+=" "
    for char in ms:
        if char == " ":
            char_value = 26
        else:
            char_value = ord(char) - ord('A')
        ct+=1
        if ct==2:
            t2=char_value
            chrGrid.append(t1*100+t2)
            ct=0
        else:
            t1=char_value
    print("M =",*chrGrid)
    enGrid = [(pow(char, e, n)) for char in chrGrid]
    return enGrid

def decrypt(enGrid, d, n):
    deGrid = [(pow(char, d, n)) for char in enGrid]
    de_ms = ""
    for i in range(0, len(deGrid)):
        if deGrid[i]//100== 26:
            de_ms += " "
        else:
            de_ms += chr(deGrid[i]//100 + ord('A'))
        if deGrid[i]%100== 26:
            de_ms += " "
        else:
            de_ms += chr(deGrid[i] %100 + ord('A'))
        
    #print(de_ms)
    return de_ms

def main():
    e = int(input("請輸入e:"))
    p = int(input("請輸入p:"))
    q = int(input("請輸入q:"))

    n, d = find_n_and_d(p, q, e)
    print(f"(n, d): ({n}, {d})")

    ms = input("請輸入所要加密之文字:")
    en_ms = encrypt(ms.upper(), e, n)
    print("C =", *en_ms)

    de_ms = decrypt(en_ms, d, n)
    print("解碼後:", de_ms)

if __name__ == "__main__":
    main()