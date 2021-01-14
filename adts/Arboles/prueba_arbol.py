class NodoArbol:
    def __init__(self , value , left=None , right=None):
        self.data = value
        self.left = left
        self.right = right

arbol=NodoArbol("R" , NodoArbol("C") , NodoArbol("H"))
print(arbol.right.data)
print(arbol.data)

arbol2 = NodoArbol(4, NodoArbol(3, NodoArbol(2, NodoArbol(2, None, None)), None), NodoArbol(5))
print(arbol2.left.left.data)
