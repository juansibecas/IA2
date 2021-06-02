import numpy as np
from copy import copy
import os
class Warehouse:
    def __init__(self, rows, columns, dx, dy):
        self.columns=columns
        self.rows=rows
        self.aisles=[]
        self.shelves=[]
        self.map=np.zeros((rows,columns))
        self.dx=dx
        self.dy=dy
        self.file_name = f'Warehouse {self.columns} {self.rows} {self.dx} {self.dy}.txt'
        self.file = self.file_init()
        
    def file_init(self):
        try:
            with open(self.file_name, 'r', encoding="utf8") as f:
                return f.readlines()
        except: #si el archivo no se creo todavia, va a parar aca
            with open(self.file_name, 'w', encoding="utf8") as f:
                string = ''
                for j in range(self.rows*self.columns): #rows*columns es la cantidad de posiciones que hay en el almacen
                    string += ','
                for i in range(self.rows*self.columns): #inserto los strings de ,,,, en cada fila
                    f.write(string)
                    f.write('\n')
            return self.file_init()
                    
    def create_aisles(self): #Funcion para crear el pasillo el dx y dy son porque tendremos pasillo cada dx filas
        px=0                 #y cada dy columnas.
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
        """    
        neighbours = []
        row = actual[0]
        column = actual[1]
        neighbours=[[row+1,column],[row-1,column],[row,column+1],[row,column-1]]
        for neighbour in neighbours:
            if neighbour[0] < 0 or neighbour[0] > self.rows-1:
                neighbours.remove(neighbour)
                continue
            if neighbour[1] < 0 or neighbour[1] > self.columns-1:
                neighbours.remove(neighbour) 
                continue
            if neighbour in self.shelves:
                neighbours.remove(neighbour)
                continue
        """
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
        
    def clear_map(self): #para hacer varios a* seguidos con el mismo warehouse
        self.map = np.zeros((self.rows, self.columns))
    
    def check_db(self, pos1, pos2):             #de aca para abajo estan todas las funciones para hacer la base de datos de a*
        pos1_index = self.get_pos_index(pos1)   #esta se hace antes de cada a*, para saber si ese caso ya se ha calculado 
        pos2_index = self.get_pos_index(pos2)   
        line = copy(self.file[pos1_index])      #entro a la fila correspondiente a la pos1
        line_split = line.split(',')            #separo el string por las comas para tener la lista con todos los costos
        cost = line_split[pos2_index]           #busco el costo segun el indice dado por la pos2
        if cost != '':                          #si esta vacio, entra al else y devuelve -1 (significa que no se calculo todavia)
            return cost
        else:
            return -1
        
    def write_to_db(self, pos1, pos2, cost):            #db seria self.file. despues de cada a*, se escribe el costo calculado ahi
        pos1_index = self.get_pos_index(pos1)           
        pos2_index = self.get_pos_index(pos2)
        line = self.file[pos1_index]                    #entro a la fila correspondiente a pos1
        line_split = line.split(',')                    #separo el string por las comas para tener la lista con todos los costos
        line_split[pos2_index] = str(cost)              #en esa lista busco el indice correspondiente a la pos2 y le inserto {cost}
        self.file[pos1_index] = ','.join(line_split)    #vuelvo a juntar la lista para formar el string como estaba (pero con un numero cambiado)
        
    def write_db_to_file(self):             #esta se hace una sola vez, al final de todo el programa para escribir self.file en el archivo
        if os.path.exists(self.file_name):  #elimino el archivo viejo
            os.remove(self.file_name)
        with open(self.file_name, 'w', encoding="utf8") as f:
            for line in self.file:          #escribo todas las lineas
                f.write(line)
        
    def get_pos_index(self, pos):
        return pos[0]*self.columns + pos[1] #le doy indices a las posiciones: [0 1 2 3 4  5   esto seria el mapa del almacen
                                                                             # 6 7 8 9 10 11] si fuesen 2 filas y 6 columnas por ej
                                                                             # si quiero ir del [0,0] al [0,5], los indices serian 0 y 5
                                                                             # entonces en el archivo voy al indice [0,5], que va a tener
                                                                             #guardado ese costo. en el indice [5,0] se va a guardar el
                                                                             #mismo valor
        