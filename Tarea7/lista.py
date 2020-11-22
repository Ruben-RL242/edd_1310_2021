class NodoDoble:
    def __init__(self, value=None, siguiente=None, anterior=None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble()
        self.__tail = NodoDoble()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size( self ): #Regresa el numero de elementos en la lista
        return self.__size

    def is_empty( self ):
        return self.__head.data == None and self.__tail.data==None

    def append( self , value ):
        self.__size+=1
        nuevo=NodoDoble(value)
        if self.is_empty(): # self.is_empty()
            self.__head = NodoDoble(value=value)
            self.__tail=self.__head
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            nuevo=NodoDoble(value=value , anterior=curr_node)
            curr_node.next = nuevo
            self.__tail=nuevo

    def find_from_tail(self , value):
        curr_node=self.__tail
        contador=0
        while curr_node.data != value:
            curr_node= curr_node.prev
            contador += 1
        return contador

    def find_from_head(self , value):
        curr_node=self.__head
        contador=0
        while curr_node.data != value:
            curr_node= curr_node.next
            contador += 1
        return contador

    def remove_from_tail(self, value):
        self.__size-=1
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            curr_node = self.__tail
            while curr_node.data != value and curr_node.prev != None:
                curr_node = curr_node.prev
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                self.__size+=1
                print("item not found")

    def remove_from_head(self, value):
        self.__size-=1
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            curr_node = self.__head
            while curr_node.data != value and curr_node.next != None:
                curr_node = curr_node.next
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                self.__size+=1
                print("item not found")

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.next
        print(" ")

    def reverse_transversal( self ):
        curr_node = self.__tail
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.prev
        print(" ")
