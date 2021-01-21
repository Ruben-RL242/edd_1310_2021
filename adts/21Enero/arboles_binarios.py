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

    def __recorrido_pos(self , nodo):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data , end=", ")

    def __recorrido_pre(self , nodo):
        if nodo:
            print(nodo.data , end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def transversal(self , format = "inorden"):
        if format == "inorden":
            print("Inorden")
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("Preorden")
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            print("Posorden")
            self.__recorrido_pos(self.__root)
        else:
            print("Error , ese formato no existe")
        print("")

    def search(self , value):
        if self.__root == None:
            print("Vacio")
            return None
        else:
            return self.__search(self.__root , value )

    def __search(self , nodo , value):
        if nodo == None: #vacio??
            return None
        elif nodo.data == value: #caso base de recursividad
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            print("buscar a la izq.")
            return self.__search(nodo.left , value )
        else:
            print("buscar a la derecha")
            return self.__search(nodo.right , value )

    def remove(self , value):
        encontrado = self.search(value)
        #caso 1
        if encontrado.left == None and encontrado.right == None:
            print("eliminando " , encontrado.data)
            encontrado = None
        #caso 2
        elif (encontrado.left != None and encontrado.right == None) or (encontrado.left == None and encontrado.right != None):
             print("A eliminar: ", encontrado.data)
