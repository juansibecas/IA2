import math
from copy import copy

class Astar:
    def __init__(self, start, finish, space, it):
        self.start = start
        self.finish = finish
        self.space = space
        self.it = it

    def h_euclid(self, start, finish, k): #función heuristica, calculamos la distancia euclidiana entre dos puntos.
        v = []
        for i in range(len(start)):
            v.append(pow((start[i]-finish[i]),2))
        return math.sqrt(sum(v))*k  #k elegido por usuario segun necesidad. factor de multiplicacion generalmente igual a 1


    def path(self): #Funcion para encontrar el menor camino.
            neighbours=[]  #guardaremos todos los vecinos de la posicion actual
            nodes=[]    #guardaremos todos los nodos - ver class Nodo
            f=0
            prev = Node(self.start, 0, 0, 0)
            g=0
            it=0
            
            if self.start == self.finish: #termina de una si empieza en el destino
                return [[self.start]], 0

            while True:
                it+=1
                neighbours=self.space.find_neighbours(prev.pos)
                
                if self.finish in neighbours:                   #si el final esta dentro de los vecinos, se mueve a el y termina el programa
                    prev = Node(self.finish, 0, "end", prev)    #le pongo cualquier cosa que no sea 0 al nivel
                    break
                
                for neighbour in neighbours:
                    g = prev.level + 1  #con 1 toma como lo mismo hacer un paso en diagonal a uno segun la direccion de un eje cualquiera
                                        #la alternativa para tener esa diferencia en cuenta seria h_euclid(prev.pos, neighbour, 1)
                    f = g + self.h_euclid(neighbour, self.finish, 1)      #calculamos la funcion f para cada vecino
                    nodes.append(Node(neighbour, f, g, prev))
                
                
                nodes = delete_duplicates(nodes)    #aca hay que quitar duplicados, es decir, nodos de la misma posicion y con un valor igual de f
                
                nodes.sort(key=sort_by_f)           #se ordena la lista de nodos de menor a mayor segun f
                
                prev = copy(nodes[0])
                nodes.pop(0)                        #eliminamos el valor actual de los nodos para que no se pueda volver a el   
                
                if it == self.it:
                    break
                    
            print(f"{it} iteraciones")
            path = []
            path = prev.connect_path(path) 
            path.reverse()
            path_len = len(path)-1 #-1 porque en path se incluye la posicion inicial
            
            return path, path_len

def delete_duplicates(lst):
    return list(set(lst))

def sort_by_f(nodo):
    return nodo.f

class Node:
    def __init__(self, pos, f, level, prev):  
        self.pos = pos
        self.f = f
        self.level = level #es el valor de g, los espacios recorridos hasta llegar aca
        self.prev = prev #guarda el nodo previo
        
    def __eq__(self, other): #eq y hash se definen para que el object sea hashable, y se pueda usar set() para eliminar duplicados
        return self.pos == other.pos and self.f == other.f #en este caso se eliminan duplicados segun pos y f
    
    def __hash__(self):
        return hash((tuple(self.pos), self.f))
    
    def connect_path(self, path): #se conecta un nodo al previo y asi sucesivamente hasta llegar al inicio del recorrido
        path.append(self.pos)
        if self.level == 0:
            return path
        else:
            return self.prev.connect_path(path)

