#MISION TIC RETO SEMANA 6, FUNCIÓN FRECUENCIA DE NOTAS
#EN CUERDA DE NOTAS STRING

Cur = input()

def cnvrt(Cur):
    letrs = ''
    for i in range(len(Cur)):
        if Cur[i].isalpha() == True:
            letrs += Cur[i].upper()
        else:
            letrs += ''
    return letrs

Cur1 = cnvrt(Cur)

def read(Cur1):
    letas = Cur1[0]
    letas += ' '
    for i in range(len(Cur1)):
        if Cur1[i-1] != Cur1[i]:
            letas += Cur1[i]
            letas += ' '
        else:
            letas += ''
    return letas

def count(Cur1):
    nums = ''
    count = 0
    for i in range(0,len(Cur1)-1,1):
        count = 1
        while (Cur1[i-1]== Cur1[i]):
            count +=1
    nums += str(count)
    return nums

Cur2 = read(Cur1)

def frq(Cur1):
    num = 0       
    act = Cur1[0]
    res = ''
    for i in range(len(Cur1)):
        if Cur1[i] == act:
            num += 1
        else:
            res += str(num) + ' '
            act = Cur1[i]
            num = 1
    res += str(num) + ' '
    return res

print(Cur2)
print(frq(Cur1))
