class Array2D:

    def __init__(self,rows, cols, value):
        self.__cols = cols
        self.__rows = rows
        self.__array=[[value for x in range(self.__cols)] for y in range(self.__rows)]

    def to_string(self):
        [print("---",end="") for x in range(self.__cols)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end="") for x in range(self.__cols)]
        print("")

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,row,col):
        return self.__array[row][col]

    def set_item( self , row , col , valor ):
        self.__array[row][col]=valor

    def clearing(self, valor=0):
        for ren in range(self.__rows):
            for col in range(self.__cols):
                self.__array[ren][col]=valor
class Juego:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0

    def __init__(self, rens, cols, generaciones, poblacion):
        self.largo = cols
        self.alto = rens
        self.grid = Array2D(self.alto, self.largo, 0)
        self.generaciones = generaciones

        for celula in poblacion:
            self.grid.set_item(celula[0], celula[1], self.CELULA_VIVA)

    def generacioness(self):
        return self.generaciones

    def configura_generacion(self, nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0], celula[1], self.CELULA_VIVA)

    def imprime_grid(self):
        for r in range(self.grid.get_num_rows()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r, c) == 0:
                    print(" ░░", end="")
                else:
                    print(" ▓▓", end="")
            print("")

    def get_num_rows(self):
        return self.alto

    def get_num_cols(self):
        return self.largo

    def set_celula_muerta(self, row, col):
        self.grid.set_item(row, col, self.CELULA_MUERTA)

    def set_celula_viva(self, row, col):
        self.grid.set_item(row, col, self.CELULA_VIVA)

    def get_is_viva(self, row, col):
        return self.grid.get_item(row, col) == self.CELULA_VIVA

    def get_is_muerta(self, row, col):
        return self.grid.get_item(row, col) == self.CELULA_MUERTA

    def get_numero_vecinos_vivos(self , row , col ):
        limites=[ row-1 , row+1 , col-1 , col+1 ]
        vecinos = 0
        if row >= 0 and row <= self.alto-1 and col >= 0 and col <= self.largo -1 :
            for r in range(limites[0],limites[1]+1):
                for c in range(limites[2],limites[3]+1):
                    if r == self.get_num_rows():
                        r = 0
                    if c == self.get_num_cols():
                        c = 0
                    if self.get_is_viva(r,c):
                        vecinos += 1
        if self.get_is_viva(row,col):
            vecinos -= 1
        return (vecinos)


    def evo(self):
        lista_clone=[]
        for rw in range( self.grid.get_num_rows() ):
            list_row = []
            for cn in range( self.grid.get_num_cols() ):
                list_row.append( self.grid.get_item(rw, cn) )
            lista_clone.append(list_row)
        for rws in range(self.grid.get_num_rows()):
            for cl in range(self.grid.get_num_cols()):
                if self.get_is_viva(rws,cl) and (self.get_numero_vecinos_vivos(rws,cl) == (2 or 3)):
                    lista_clone[rws][cl]= self.CELULA_VIVA
                if self.get_is_viva(rws,cl) and (self.get_numero_vecinos_vivos(rws,cl) <= 1):
                    lista_clone[rws][cl]= self.CELULA_MUERTA
                if self.get_is_viva(rws,cl) and (self.get_numero_vecinos_vivos(rws,cl) >= 4):
                    lista_clone[rws][cl]= self.CELULA_MUERTA
                if self.get_is_muerta(rws,cl) and self.get_numero_vecinos_vivos(rws,cl)== 3 :
                    lista_clone[rws][cl]= self.CELULA_VIVA
        for xr in range( len(lista_clone) ):
            for xc in range( len(lista_clone[xr])):
                self.grid.set_item( xr, xc, lista_clone[xr][xc])

    def play(self):
        print(f"Generacion 1")
        juego.imprime_grid()
        print("")
        for generacion in range(juego.generacioness()):
            print("")
            juego.evo()
            print(f"Generacion {generacion + 2 }")
            juego.imprime_grid()

print("cordenadas de inicio [(1,2), (2,1), (2,2), (2,3)]")
juego = Juego(7, 7, 6, [(1,2), (2,1), (2,2), (2,3)])
juego.play()
