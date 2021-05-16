import numpy as np
class Warehouse:
    def __init__(self, rows, columns, dx, dy):
        self.columns=columns
        self.rows=rows
        self.aisles=[]
        self.shelves=[]
        self.map=np.zeros((rows,columns))
        self.dx=dx
        self.dy=dy

    def create_aisles(self): #Funcion para crear el pasillo el dx y dy son porque tendremos pasillo cada dx filas
        px=0                # y cada dy columnas.
        py=0
        while py <self.rows:
            for j in range(self.columns):
                self.aisles.append([py,j])
            py+=self.dy
        while px <self.columns:
            for i in range(self.rows):
                if [i,px] not in self.aisles:
                    self.aisles.append([i,px])
            px+=self.dx
        return self.aisles
    
    def create_shelves(self): #Funcion para crear las estanterias, donde no tenemos pasillo es una estanteria
        for i in range(self.rows):
            for j in range(self.columns):
                if [i,j] not in self.aisles:
                    self.shelves.append([i,j])
                    self.map[i,j] = 2 #JP: le meti un 2 para que se vea un poco mejor el mapita
        return self.shelves
    
    def find_neighbours(self, actual, final): #función para encontrar a los vecinos
        ii=(int(actual[0]))#indices en i
        ij=(int(actual[1]))#indices en j
        neighbours=[[ii+1,ij],[ii-1,ij],[ii,ij+1],[ii,ij-1]]
        if ii-1 < 0 : #Borramos los que estan fuera de los limites
            neighbours.remove([ii-1,ij])
        if ii+1 >=self.rows :
            neighbours.remove([ii+1,ij])  
        if ij-1 < 0 :
            neighbours.remove([ii,ij-1])
        if ij+1 >=self.columns :
            neighbours.remove([ii,ij+1])
        jj=-1
        for a in range(len(neighbours)): #borramos los que sean estanterias, ya que no pueden ir ahi. 
            jj+=1
            if jj <= len(neighbours)-1:
                if neighbours[jj] !=final: #menos si el ultimo punto es una estanteria, asi puede diferenciar si llego al final
                    if neighbours[jj] in self.shelves:
                        neighbours.remove(neighbours[jj])
                        jj-=1
                    if self.map[neighbours[jj][0], neighbours[jj][1]] == 1: #para que no pueda volver a un lugar en el que ya estuvo
                        neighbours.remove(neighbours[jj])
                        jj-=1
        return neighbours
    
    def assign_aisle_to_shelf(self, shelf): #chequea cual de los vecinos a la izquierda y a la derecha es un pasillo y lo devuelve
        if [shelf[0], shelf[1]-1] in self.aisles: #(el horizontal es la segunda componente)
            return [shelf[0], shelf[1]-1]
        else:
            return [shelf[0], shelf[1]+1]