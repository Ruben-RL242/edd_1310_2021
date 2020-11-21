class Nodo:
    def __init__( self , value , siguiente= None):
        self.data = value       # falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__( self ):
        self.__head = None

    def is_empty( self ):
        return self.__head == None

    def append( self , value ):
        nuevo = Nodo( value )
        if self.__head == None: # self.is_empty()
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.siguiente
        print(" ")

    def remove( self , value ):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head=self.__head.siguiente
        else:
            anterior=None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior=curr_node     #variable temproal que guarda el valor anterior al que se va a eliminar
                curr_node= curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente=curr_node.siguiente
            else:
                print("El dato no existe en la lista")

    def preppend(self , value):
        nuevo=Nodo(value , self.__head)
        self.__head=nuevo

    def tail( self ):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def get(self , posicion=None):#por defecto regrese el ultimo
        contador=0
        dato=None
        if posicion == None :
            dato=self.tail().data
        else:
            curr_node = self.__head
            while contador != posicion and curr_node.siguiente != None:
                curr_node = curr_node.siguiente
                contador = contador + 1
            if(contador==posicion):
                dato = curr_node.data
            else:
                dato="posicion no existe en la lista"
        return dato

    #Agregar antes de la primer coincidiencia, si no encuentra la referencia no hace la inserccion.
    def add_before(self,reference_value,value):
        nuevo= Nodo(value)
        curr_node=self.__head
        while curr_node.data != reference_value and curr_node.siguiente != None: # aqui se busca el nodo que se va a utilizar como referencia
            curr_new=curr_node
            curr_node= curr_node.siguiente
        if curr_node.data == reference_value and curr_node.data != self.__head.data:
            curr_new.siguiente=nuevo
            curr_new.siguiente.siguiente=curr_node
        else:
            if curr_node.data == reference_value:
                self.__head=nuevo
                nuevo.siguiente=curr_node

    #Agregar después de la referencia
    def add_after(self,reference_value,value):
        nuevo= Nodo(value)
        curr_node=self.__head
        while curr_node.data != reference_value and curr_node.siguiente != None:#aqui se busca el nodo que se va a utilizar como referencia
            curr_node= curr_node.siguiente
            curr_new= curr_node.siguiente
        if curr_node.data == reference_value and curr_node.data != self.__head.data:
            curr_node.siguiente=nuevo
            curr_node.siguiente.siguiente=curr_new
        else:
            if curr_node.data == reference_value:
                curr_new = curr_node.siguiente
                curr_node.siguiente=nuevo
                curr_node.siguiente.siguiente=curr_new
