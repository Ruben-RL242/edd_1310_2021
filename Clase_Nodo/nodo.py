class Nodo:
    def __init__( self , dato ):
        self.__dato = dato
        self.__siguiente = None

    def get_dato( self ):
        return self.__dato

    def set_dato( self , d ):
        self.__dato = d

    def get_siguiente( self ):
        return self.__siguiente

    def set_siguiente( self , d ):
        self.__siguiente = d

    def show(self):
        curr_node = self  # Head
        print(" Inicio de la estructura ligada:")
        print("|" + str(curr_node.get_dato()) + "| -->", end="")
        while (curr_node.get_siguiente() != None):
            curr_node = curr_node.get_siguiente()
            print("|" + str(curr_node.get_dato()) + "| -->", end="")
        print("\nFin")

#Ejmeplo 1
a=Nodo(10)
a.show()

# Ejemplo 2
a.set_siguiente(Nodo(20))
a.show()

#Ejemplo 3
a.get_siguiente().set_siguiente(Nodo(30))
a.show()
#Ejemplo 4
a.get_siguiente().get_siguiente().set_siguiente(Nodo(40))
a.show()
#Ejemplo 5
a.get_siguiente().get_siguiente().get_siguiente().set_siguiente(Nodo(50))
a.show()

#Para cambiar el valor del primer Nodo
a.set_dato(12)
a.show()

#Ejemplo 7
a.get_siguiente().get_siguiente().get_siguiente().set_dato(46)
a.show()

#ejemplo 8
a.get_siguiente().set_dato(25)
a.show()

a.get_siguiente().get_siguiente().get_siguiente().set_siguiente(None)
a.show()
