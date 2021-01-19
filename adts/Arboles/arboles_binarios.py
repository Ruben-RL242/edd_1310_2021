class NodoArbol:
    def __init__(self , value , left = None , right = None):
        self.data = value
        self.right = right
        self.left = left

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self , value):
        # Regla 1
        if self.__root == None:
            self.__root = NodoArbol(value)
        # Regla 2
        else:
            self.__insert__(self.__root , value)

    def __insert__(self , nodo , value):
        if nodo.data == value:
            print("El Dato ya existe, no se ingresa nada")
        elif value < nodo.data:
            # Regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            #Regla 2
            else:
                self.__insert__(nodo.left , value)
        else:
            # Regla 1
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            # Regla 2
            else:
                self.__insert__(nodo.right , value)

    def __recorrido_in(self , nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data , end = ", ")
            self.__recorrido_in(nodo.right)

    def transversal(self , format = "inorden"):
        if format == "inorden":
            print("Inorden")
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("Preorden")
            #self.__recorrido_pre(self.__root)
        elif format == "posorden":
            print("Posorden")
            #self.__recorrido_pos(self.__root)
        else:
            print("Error , ese formato no existe")
        print("")
