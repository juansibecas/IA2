import math
import numpy as np
class Aestrella:
    def __init__(self,ini,final,mapa,pasillo,estante):
        self.ini = ini
        self.final = final
        self.mapa = mapa
        self.pasillo = pasillo
        self.estante = estante

    def h(self,actual): #función heuristica
        h1=pow((actual[0]-self.final[0]),2)
        h2=pow((actual[1]-self.final[1]),2)
        h= (math.sqrt(h1 + h2))*3
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
        for valor in vecinos:
            if valor !=self.final:
                if valor in self.estante:
                    vecinos.remove(valor)
        return vecinos

    def menor(self,fnodos):
        index=0
        indice=index
        menor=fnodos[0]
        for valor in fnodos:
            if valor < menor:
                menor= valor
                indice=index
            index+=1
        return indice

    def camino(self,columna,fila):
        vecinos=[]
        nodos=[]
        fnodos=[]
        flag=1
        f=0
        camino=[]
        actual=self.ini
        camino.append(actual)
        self.mapa[actual[0],actual[1]]=1
        print(self.mapa)
        g=0
        while flag:
            vecinos=self.encuentra_vecinos(actual,columna, fila)
            for j in range(len(vecinos)):
                f=g+self.h(vecinos[j])
                fnodos.append(f)
                nodos.append(vecinos[j])
            index=self.menor(fnodos) 
            actual=nodos[index]
            fnodos.pop(index)
            nodos.pop(index)
            if self.final in vecinos:
                flag=0
            g+=1
            camino.append(actual)
            self.mapa[actual[0],actual[1]]=1
            print(self.mapa)
        print(camino)

