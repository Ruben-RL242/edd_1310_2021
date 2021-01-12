class PriorityQueue:
    def __init__( self):
        self.__cola = list()

    def is_empty( self):
        return len(self.__cola) == 0

    def length( self):
        return len(self.__cola)

    def enqueue( self, prioridad, elem):
        self.__cola.append((prioridad, elem))
        for x in range(self.length()):
            pos = x
            actual = self.__cola[x]
            while pos > 0 and self.__cola[pos-1][0] > actual[0]:
                self.__cola[pos] = self.__cola[pos-1]
                pos-=1
            self.__cola[pos] = actual

    def dequeue( self):
        return self.__cola.pop(0)

    def to_string( self):
        for elem in self.__cola:
            print(f"<-{elem}",end="")
        print("")
