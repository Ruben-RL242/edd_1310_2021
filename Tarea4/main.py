from adts import Array
archivo=open( 'junio.dat', 'rt' )
lineas = archivo.readlines()
lineas = [ l.replace(' ','').strip().split(',') for l in lineas ]
renglon=len(lineas)
lista=Array(renglon)
menor=2016
mayor=2020
precio_horas=276.5
sueldo_base=9850
for x in range(0,renglon,1):
    lista.set_item(lineas[x],x)
for x in range(1,renglon,1):
    horas=int(lista.get_item(x)[4])
    ingreso=int(lista.get_item(x)[6])
    salario_extra=horas*precio_horas
    total=sueldo_base+salario_extra
    prestaciones=(2020-ingreso)*3
    total_mas_horas=total
    total_mas_prestaciones=(total_mas_horas)+(((mayor-ingreso)*0.03)*sueldo_base)
    print(f"{x}.-El empleado {lineas[x][0]} con nombre: {lineas[x][1]} {lineas[x][2]} tiene un sueldo base de 9850\nsumando sus {horas} horas extras su sueldo es de: ${total_mas_horas} y tiene un %{prestaciones} de prestaciones \n lo que lo deja con un sueldo total de {total_mas_prestaciones}\n")
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
print("Los empleados con mayor antiguedad son: ")
for x in range(1,renglon,1):
    ingreso=int(lista.get_item(x)[6])
    if(ingreso==menor):
        print(lista.get_item(x)[1]," entrando en el año: ",lista.get_item(x)[6], end="             ")
print("\n\nLos empleados con menor antiguedad son: ")
for x in range(1,renglon,1):
    ingreso=int(lista.get_item(x)[6])
    if(ingreso==mayor):
        print(lista.get_item(x)[1]," entrando en el año: ",lista.get_item(x)[6], end="             ")
