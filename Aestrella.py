import math
import numpy as np
class Aestrella:
    def __init__(self,ini,final,mapa,pasillo,estante):
        self.ini = ini
        self.final = final
        self.mapa = mapa
        self.pasillo = pasillo
        self.estante = estante

    def h(self,actual): #función heuristica, calculamos la distancia euclidiana entre dos puntos.
        h1=pow((actual[0]-self.final[0]),2)
        h2=pow((actual[1]-self.final[1]),2)
        h= (math.sqrt(h1 + h2))*2 #multiplicamos por 2 para que tenga mas peso frente a la g. 
        return h
    
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
            if vecinos[jj] !=self.final: #menos si el ultimo punto es una estanteria, asi puede diferenciar si llego al final
                if vecinos[jj] in self.estante:
                    vecinos.remove(vecinos[jj])
                    jj-=1
                if self.mapa[vecinos[jj][0],vecinos[jj][1]] == 1: #para que no pueda volver a un lugar en el que ya estuvo
                    vecinos.remove(vecinos[jj])
                    jj-=1
        return vecinos

    def menor(self,fnodos):#funcion para elegir la menor funcion f entre todos los nodos existentes.
        index=0
        indice=index
        menor=fnodos[0]
        for valor in fnodos:
            if valor < menor:
                menor= valor
                indice=index
            index+=1
        return indice      #retorna el indice del menor valor

    def camino(self,columna,fila): #Funcion para encontrar el menor camino.
        vecinos=[]  #guardaremos todos los vecinos de la posicion actual
        nodos=[]    #guardaremos todos las ubicaciones posibles, nodos
        fnodos=[]   #guardaremos las funciones f de todos los nodos, para luego elegir la menor
        flag=1
        f=0
        camino=[]
        actual=self.ini #posicion actual. 
        camino.append(actual)
        self.mapa[actual[0],actual[1]]=1 #Para tener un 1 en los lugares donde va pasando.
        print(self.mapa)
        g=0
        while flag:
            vecinos=self.encuentra_vecinos(actual,columna, fila)
            for j in range(len(vecinos)):
                f=g+self.h(vecinos[j])      #calculamos la funcion f para cada vecino, g vale una unidad por cada movimiento
                fnodos.append(f)
                nodos.append(vecinos[j])
            index=self.menor(fnodos)        
            actual=nodos[index]             #actualizamos el valor actual 
            fnodos.pop(index)               #eliminamos el valor actual de los nodos y de fnodos para que no se pueda volver a el 
            nodos.pop(index)               
            if self.final in vecinos:       #si el final esta dentro de los vecinos, termina el programa. Llegamos
                flag=0
            g+=1                            #valor de la funcion g, es una unidad
            camino.append(actual)
            self.mapa[actual[0],actual[1]]=1
            print(self.mapa)
        return camino

