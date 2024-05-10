#TIC RETO SEMANA 4, FUNCIÓN JUEGO NOTAS DE CUERDAS STRING

Jms = input('Introduzca cuerdas de James: ')
Krk = input('Introduzca cuerdas de Kirk: ')
Sng = input('Introduzca la secuencia de cuerdas del juego: ')

if str.isalpha(Krk) == False or str.isupper(Krk) == False or str.isalpha(Jms) == False or str.isupper(Jms) == False or len(Krk) != len(Jms) or str.isalpha(Sng) == False or str.isupper(Sng) == False:
    print('Asegúrese que Kirk y James hayan elegido el mismo número de letras, y que todas las entradas sean letras mayúsculas')
    Jms = input('Introduzca otra vez cuerdas de James: ')
    Krk = input('Introduzca otra vez cuerdas de Kirk: ')
    Sng = input('Introduzca otra vez la secuencia de cuerdas del juego: ')

def game(Krk, Jms, Sng):
    conteo = ''
    ptosjms = 0
    ptoskrk = 0
    for i in range(len(Sng)):
        if Sng[i] in Krk and Sng[i] not in Jms:
            ptoskrk += 1
        elif Sng[i] not in Krk and Sng[i] in Jms:
            ptosjms += 1
        else:
            ptoskrk += 0
            ptosjms += 0
        if ptoskrk < ptosjms:
            conteo += 'J'
        elif ptoskrk > ptosjms:
            conteo += 'K'
        else:
            conteo += 'L'
    return conteo

print(game(Krk, Jms, Sng))
