import numpy as np
class Almacen:
    def __init__(self,filas,columnas):
        self.columnas=columnas
        self.filas=filas
        self.pasillo=[]
        self.estante=[]
        self.almacen=np.zeros((filas,columnas))

    def crear_pasillo(self): #Funcion para crear el pasillo el 5 y 3 son porque tendremos pasillo cada 5 filas
        px=0                 # y cada 3 columnas.
        py=0
        dy=5
        dx=3
        while py <self.filas:
            for j in range(self.columnas):
                self.pasillo.append([py,j])
            py+=dy
        while px <self.columnas:
            for i in range(self.filas):
                if [i,px] not in self.pasillo:
                    self.pasillo.append([i,px])
            px+=dx
        return self.pasillo
    
    def crear_estante(self): #Funcion para crear las estanterias, donde no tenemos pasillo es una estanteria
        for i in range(self.filas):
            for j in range(self.columnas):
                if [i,j] not in self.pasillo:
                    self.estante.append([i,j])
                    self.almacen[i,j] = 2 #JP: le meti un 2 para que se vea un poco mejor el mapita
        return self.estante