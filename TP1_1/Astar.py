import math
from copy import copy
from Espacio import Espacio

class Astar:
    def __init__(self, inicial, final, espacio):
        self.inicial = inicial
        self.final = final
        self.espacio = espacio

    def h_euclid(self, actual, final, k): #función heuristica, calculamos la distancia euclidiana entre dos puntos.
        v = []
        for i in range(len(actual)):
            v.append(pow((actual[i]-final[i]),2))
        return math.sqrt(sum(v))*k 


    def camino(self): #Funcion para encontrar el menor camino.
            vecinos=[]  #guardaremos todos los vecinos de la posicion actual
            nodos=[]    #guardaremos todos los nodos - ver class Nodo
            flag=1
            f=0
            prev = Nodo(self.inicial, 0, 0, 0)
            g=0
            while flag:
                g+=1 #valor de la funcion g, es una unidad
                vecinos=self.espacio.find_neighbours(prev.pos)
                for j in range(len(vecinos)):
                    f=g+self.h_euclid(vecinos[j], self.final, 1)      #calculamos la funcion f para cada vecino, g vale una unidad por cada movimiento
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

