import numpy as np
class Almacen:
    def __init__(self,filas,columnas):
        self.columnas=columnas
        self.filas=filas
        self.pasillo=[]
        self.estante=[]
        self.x=[]
        self.y=[]
        self.almacen=np.zeros((filas,columnas))

    def crear_pasillo(self): #Funcion para crear el pasillo el 5 y 3 son porque tendremos pasillo cada 5 filas
        px=0                 # y cada 3 columnas.
        py=0
        while py <self.filas:
            for j in range(self.columnas):
                self.pasillo.append([py,j])
            py+=5
        while px <self.columnas:
            for i in range(self.filas):
                if [i,px] not in self.pasillo:
                    self.pasillo.append([i,px])
            px+=3
        return self.pasillo
    def crear_estante(self): #Funcion para crear las estaterias, donde no tenemos pasillo es una estanteria
        for i in range(self.filas):
            for j in range(self.columnas):
                if [i,j] not in self.pasillo:
                    self.estante.append([i,j])
        return self.estante