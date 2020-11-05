from arrays import Array
archivo=open( 'junio.dat', 'r' )
lineas = archivo.readlines()
lineas = [ l.replace(' ','').strip().split(',') for l in lineas ]
lectura=len(lineas)
lista=Array(lectura)
menor=2016
mayor=2020
for x in range(0,lectura,1):
    lista.set_item(lineas[x],x)
for x in range(1,lectura,1):
    precio_horas=276.5
    sueldo_base=9850
    horas=int(lista.get_item(x)[4])
    ingreso=int(lista.get_item(x)[6])
    salario_extra=horas*precio_horas
    total=sueldo_base+salario_extra
    prestaciones=float((2020-ingreso)*0.03)
    total_mas_prestaciones=((prestaciones*9850)+total)
    print(f"{x}.-El empleado {lineas[x][0]} con nombre: {lineas[x][1]} tiene un sueldo base de 9850\nsumando sus horas extras y sus prestaciones su sueldo total es de: ${total_mas_prestaciones}\n")
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
for x in range(1,lectura,1):
    ingreso=int(lista.get_item(x)[6])
    if(ingreso==menor):
        print(lista.get_item(x)[1]," entrando en el año: ",lista.get_item(x)[6])
print("Los empleado con menor antiguedad son: ")
for x in range(1,lectura,1):
    ingreso=int(lista.get_item(x)[6])
    if(ingreso==mayor):
        print("El empleado con menor antiguedad es: ",lista.get_item(x)[1])
