class NodoArbol:
    def __init__(self, value, left = None, right= None):
        self.data = value
        self.left = left
        self.right = right
def main():
    print("Arbol binario 1")
    arbol_1 = NodoArbol('+', NodoArbol('-', NodoArbol(5), NodoArbol(4)) , NodoArbol('*', NodoArbol(3), NodoArbol(2)))
    print(f"||||||||||||{arbol_1.data}||||||||||||||||")
    print(f"||||||{arbol_1.left.data}|||||||||||||{arbol_1.right.data}||||||||")
    print(f"|||{arbol_1.left.left.data}|||||{arbol_1.left.right.data}||||||{arbol_1.right.left.data}||||||{arbol_1.right.right.data}|||||")
    print("\n********************** Recorrido prefijo **********************")
    print(f"{arbol_1.data}--->{arbol_1.left.data}--->{arbol_1.left.left.data}--->{arbol_1.left.right.data}--->{arbol_1.right.data}--->{arbol_1.right.left.data}--->{arbol_1.right.right.data}")
    print("\n********************** Recorrido posfijo **********************")
    print(f"{arbol_1.left.left.data}--->{arbol_1.left.right.data}--->{arbol_1.left.data}--->{arbol_1.right.left.data}--->{arbol_1.right.right.data}--->{arbol_1.right.data}--->{arbol_1.data}")
    print("\n********************** Recorrido infijo **********************")
    print(f"{arbol_1.left.left.data}--->{arbol_1.left.data}--->{arbol_1.left.right.data}--->{arbol_1.data}--->{arbol_1.right.left.data}--->{arbol_1.right.data}--->{arbol_1.right.right.data}")
    print("\n\nArbol binario 2")
    arbol_2 = NodoArbol(40, NodoArbol(30 , NodoArbol(25) , NodoArbol(35)) , NodoArbol(50 , NodoArbol(45) , NodoArbol(60)) )
    print(f"||||||||||||{arbol_2.data}||||||||||||||||")
    print(f"||||||{arbol_2.left.data}|||||||||||||{arbol_2.right.data}|||||||")
    print(f"|||{arbol_2.left.left.data}|||||{arbol_2.left.right.data}||||||{arbol_2.right.left.data}||||||{arbol_2.right.right.data}||")
    print("\n********************** Recorrido prefijo **********************")
    print(f"{arbol_2.data}--->{arbol_2.left.data}--->{arbol_2.left.left.data}--->{arbol_2.left.right.data}--->{arbol_2.right.data}--->{arbol_2.right.left.data}--->{arbol_2.right.right.data}")
    print("\n********************** Recorrido posfijo **********************")
    print(f"{arbol_2.left.left.data}--->{arbol_2.left.right.data}--->{arbol_2.left.data}--->{arbol_2.right.left.data}--->{arbol_2.right.right.data}--->{arbol_2.right.data}--->{arbol_2.data}")
    print("\n********************** Recorrido infijo **********************")
    print(f"{arbol_2.left.left.data}--->{arbol_2.left.data}--->{arbol_2.left.right.data}--->{arbol_2.data}--->{arbol_2.right.left.data}--->{arbol_2.right.data}--->{arbol_2.right.right.data}")
main()
