#TIC RETO SEMANA 7, FUNCIÓN JUEGO CONTEO Y CONVERSION
#DE CUERDA DE NOTAS STRING

import json
cur = input()
selec = input()
cuer = json.loads(cur)

def cnvrt(selec):
    letrs = ''
    for i in range(len(selec)):
        if selec[i].isalpha() == True:
            letrs += selec[i].lower()
        else:
            letrs += ''
    return letrs

nsel = cnvrt(selec)

def conta(cuer, nsel):
    conteo = 0
    for i in range(len(nsel)):
        if str(nsel[i]) in cuer:
            conteo += int(cuer[str(nsel[i])])
        else:
            conteo += 0
    return conteo

def finalcuer(cuer, selec):
    letas = ''
    for i in range(len(selec)):
        if str(selec[i]) in cuer:
            letas += str(selec[i])
            letas += ','
        else:
            letas += ''
    letas = letas[:-1]
    return letas

print(conta(cuer, nsel))
print(finalcuer(cuer, selec))
