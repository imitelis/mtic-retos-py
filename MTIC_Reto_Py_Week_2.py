#MISION TIC RETO SEMANA 2, FUNCIÓN GANANCIA INTS

producto = input('Introduzca el nombre del producto: ')
costu = int(input('Introduzca el costo unitario del producto: '))
costpvp = int(input('Introduzca el precio de venta al público: '))
unidisp = int(input('Introduzca el número de unidades disponibles: '))

def ganancia(costu, costpvp, unidisp):
    ganas = costpvp*unidisp - costu*unidisp
    return ganas

print('Producto: ',producto)
print('CU: $',costu)
print('PVP: $',costpvp)
print('Unidades Disponibles: ',unidisp)
print('Ganancia: $',ganancia(costu, costpvp, unidisp))
