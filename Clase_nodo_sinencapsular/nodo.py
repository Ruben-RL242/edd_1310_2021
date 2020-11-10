class Nodo:
    def __init__(self , dato):
        self.dato=dato
        self.siguiente=None

#ejemplo 1
a=Nodo(10)
print(a.dato)
print(a.siguiente)

#corrido Transversal
curr_node=a
print(curr_node.siguiente , "-->" , end="")
    curr_node=curr_Node.siguiente
    print(curr_Node.dato, end="")
    print("")
