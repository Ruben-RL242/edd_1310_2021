class Nodo:
    def __init__(self , dato):
        self.dato=dato
        self.siguiente=None
#ejemplo 1 #un solo elemento
a=Nodo(12)
print(a.dato)
print(a.siguiente)
#empiezan a agregarse mas elementos
#ejemplo 2
a.siguiente=Nodo(20)

#ejemplo 3
a.siguiente.siguiente=Nodo(30)

#ejemplo 4
a.siguiente.siguiente.siguiente=Nodo(40)

#ejemplo 5
a.siguiente.siguiente.siguiente.siguiente=Nodo(50)

#Eliminando elemento 30
a.siguiente.siguiente=a.siguiente.siguiente.siguiente

#Ejemplo 7 cambiar un dato
a.siguiente.siguiente
a.dato=45

#Ejemplo 8 Insertar un dato entre dos.
tmp= a.siguiente.siguiente.siguiente#Respaldo mi nodo 50, para que no se pierda la referencia
a.siguiente.siguiente.siguiente=Nodo(48) #creo mi nuevo nodo
a.siguiente.siguiente.siguiente.siguiente= tmp #vuelvo agregar mi nodo 50

#corrido Transversal
curr_node = a
print(curr_node.dato , "---> " , end = "")
while(curr_node.siguiente != None):
    curr_node = curr_node.siguiente
    print(curr_node.dato , "---> " , end = "")
print("")
