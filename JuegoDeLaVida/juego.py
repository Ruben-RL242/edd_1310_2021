class Juego:
    CELULA_VIVA=1
    CELULA_MUERTA=0

    def __init__(self,rows,cols,generaciones,poblacion):
        self.largo=__cols
        self.alto=rens
        self.grid=Array2D(self.alto , self.largo, 0)
        self.generaciones=generaciones

        for celula in poblacion:
            self.grid.set_item(celula[0],celula[1],self.CELULA_VIVA)

    def configura_generacion(self, nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0],celula[1],self.CELULA_VIVA)

    def imprime_grid(self):
        for r in range(self.grid.get_num_rows()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r,c)==0
                    print("░░",end="")
                else:
                    print("▓▓",end="")
            print("")
        
