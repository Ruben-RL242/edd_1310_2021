class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value
        self.next=siguiente
class CircularList:
    def __init__(self):
        self.__head=None
        self.__referencia=None

    def is_empty(self):
        return self.__head==None

    def insert(self,value=None):
        nuevo=Nodo(value)
        if self.__head == None:
            self.__head=self.__ref=nuevo
            self.__ref.siguiente=self.__head
        elif self.search(value)== True:#Valor ya en lista
            print(f"El valor {value} ya se encuentra en la lista")
        elif value == None:
            pass
        elif value > self.__ref.data:
            curr_ref=self.__ref
            self.__ref=curr_ref.siguiente=nuevo
            self.__ref.siguiente=self.__head
        else:
            if value < self.__head.data:
                nuevo.siguiente=self.__head
                self.__head= nuevo
                self.__ref.siguiente=self.__head
            else:
                if value > self.__head.data:
                    curr_ref=self.__ref.siguiente
                    while value > curr_ref.data:#aqui se ordena
                        curr_ant=curr_ref
                        curr_ref=curr_ref.siguiente
                    nuevo.siguiente=curr_ant.siguiente
                    curr_ant.siguiente=nuevo

    def transversal(self):
        curr_node=self.__ref
        print("----lista actual")
        while curr_node.siguiente != self.__ref:
            print(f"{curr_node.siguiente.data} → ",end="")
            curr_node= curr_node.siguiente
        print(f"{curr_node.siguiente.data} → ")

    def search(self,value=None):
        existe=False
        curr_ref=self.__ref
        while curr_ref.siguiente != self.__ref:
            if curr_ref.data==value:
                existe=True
            curr_ref=curr_ref.siguiente
        return existe

    def remove(self,value=None):
        if value==None:
            pass
        elif self.__head==self.__ref:
            self.__head=self.__ref=None
        else:
            curr_ref=self.__ref
            while curr_ref.data != value and curr_ref.siguiente != self.__ref:
                curr_ant=curr_ref
                curr_ref=curr_ref.siguiente
            print(f"elemento eliminado es: {curr_ref.data}")
            if curr_ref.data == self.__head.data:
                self.__head = self.__head.siguiente
                self.__ref.siguiente=self.__head
            elif curr_ref.data == self.__ref.data:
                curr_reff=self.__head
                while curr_reff.siguiente != self.__ref:
                    curr_reff=curr_reff.siguiente
                curr_reff.siguiente=self.__head
                self.__ref= curr_reff
            else:
                curr_ant.siguiente=curr_ant.siguiente.siguiente
