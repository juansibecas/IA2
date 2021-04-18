import math
import numpy as np
from copy import copy
class Aestrella:
    def __init__(self,ini,final,mapa,pasillo,estante):
        self.ini = ini
        self.final = final
        self.mapa = mapa
        self.pasillo = pasillo
        self.estante = estante

    def h_euclid(self, actual, final, k): #función heuristica, calculamos la distancia euclidiana entre dos puntos.
        v = []  #la cambie para que sea mas general y se pueda volver a usar
        for i in range(len(actual)):
            v.append(pow((actual[i]-final[i]),2))
        return math.sqrt(sum(v))*k #multiplicamos por 2 para que tenga mas peso frente a la g. 

    def h_manhattan(self, actual, final): #heuristica manhattan
        v = []
        for i in range(len(actual)):
            v.append(abs(actual[i] - final[i]))
        return sum(v)
    
    def encuentra_vecinos(self,actual, columna, fila): #función para encontrar a los vecinos
        ii=(int(actual[0]))#indices en i
        ij=(int(actual[1]))#indices en j
        vecinos=[[ii+1,ij],[ii-1,ij],[ii,ij+1],[ii,ij-1]]
        if ii-1 < 0 : #Borramos los que estan fuera de los limites
            vecinos.remove([ii-1,ij])
        if ii+1 >=fila :
            vecinos.remove([ii+1,ij])  
        if ij-1 < 0 :
            vecinos.remove([ii,ij-1])
        if ij+1 >=columna :
            vecinos.remove([ii,ij+1])
        jj=-1
        for a in range(len(vecinos)): #borramos los que sean estanterias, ya que no pueden ir ahi. 
            jj+=1
            if jj <= len(vecinos)-1:
                if vecinos[jj] !=self.final: #menos si el ultimo punto es una estanteria, asi puede diferenciar si llego al final
                    if vecinos[jj] in self.estante:
                        vecinos.remove(vecinos[jj])
                        jj-=1
                    if self.mapa[vecinos[jj][0],vecinos[jj][1]] == 1: #para que no pueda volver a un lugar en el que ya estuvo
                        vecinos.remove(vecinos[jj])
                        jj-=1
        return vecinos
      
    def camino(self,columna,fila): #Funcion para encontrar el menor camino.
        vecinos=[]  #guardaremos todos los vecinos de la posicion actual
        nodos=[]    #guardaremos todos los nodos - ver class Nodo
        flag=1
        f=0
        prev = Nodo(self.ini, 0, 0, 0)
        g=0
        while flag:
            g+=1 #valor de la funcion g, es una unidad
            vecinos=self.encuentra_vecinos(prev.pos,columna, fila)
            for j in range(len(vecinos)):
                f=g+self.h_manhattan(vecinos[j], self.final)      #calculamos la funcion f para cada vecino, g vale una unidad por cada movimiento
                nodos.append(Nodo(vecinos[j], f, g, prev))
            
            nodos.sort(key=sort_by_f) #se ordena la lista de nodos de menor a mayor segun f
            if nodos[0].nivel < g:
                g = nodos[0].nivel #si el algoritmo vuelve a una rama anterior, vuelve el valor de g al original
                
            
            prev = copy(nodos[0])
            nodos.pop(0)                    #eliminamos el valor actual de los nodos para que no se pueda volver a el               
            if self.final in vecinos:       #si el final esta dentro de los vecinos, se mueve a el y termina el programa. Llegamos
                prev = Nodo(self.final, 0, 0, copy(prev))    
                flag=0
        
        camino = []
        camino = prev.connect_path(camino) 
        camino.reverse()
        
        for i in camino:
            self.mapa[i[0], i[1]] = 1 #1 es por donde pasa
        print(self.mapa) #JP: te lo corri para que no se printee el mapa 18 veces
        
        return camino



def sort_by_f(nodo):
    return nodo.f

class Nodo:
    def __init__(self, pos, f, nivel, prev):  
        self.pos = pos
        self.f = f
        self.nivel = nivel #es el valor de g, los espacios recorridos hasta llegar aca
        self.prev = prev #guarda el nodo previo
    
    def connect_path(self, path): #se conecta un nodo al previo y asi sucesivamente hasta llegar al inicio del recorrido
        path.append(self.pos)
        if self.prev == 0:
            return path
        else:
            return self.prev.connect_path(path)