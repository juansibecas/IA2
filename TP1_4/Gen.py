import random

class Gen:
    def __init__(self,shelves,n):
        self.fitness=[]
        self.population=[]
        self.shelves=shelves
        self.n=n
    
    def individuals(self): #creamos los individuos inicial con una lista random sample
        i=len(self.shelves)
        return (random.sample(range(0,i),i))

    def set_pop(self): #creamos una nueva pobacion de individuos
        for j in range(self.n):
            self.population.append(self.individuals())

    def get_pop(self):
        print(self.population)

    def set_fitness(self,individual):
        fit=0

    def sel_and_rep(self):
        self.set_pop()
        print(self.population[9][98])
        #self.fitness=[(self.set_fitness(i), i) for i in self.population]
        selected=self.population

    def order_crossover(self, parent1, parent2): #aca hay que ver despues como hacemos, si mandamos los padres como parametros, si los elegimos afuera o adentro, etc
        
        n_genes, child1, child2, pointinit, pointfin = two_point_crossover_init(parent1, parent2)
        counter1= 0
        counter2= 0
        
        for i in range(pointinit, pointfin): #crossover comun entre punto inicial y punto final
            child2[i] = parent1[i] #aca va hijo 1 con padre 2
            child1[i] = parent2[i]
        
        for i in range(pointfin-n_genes, pointfin): #crossover de orden. aca va hijo 1 con padre 1. recorro la lista desde un indice negativo
            if parent1[i] not in child1:           #counter cumple la funcion de mantener el indice del hijo cuando parent[i] ya estaba colocado
                child1[i-counter1]= parent1[i]
            else:
                counter1+= 1
                
            if parent2[i] not in child2:
                child2[i-counter2]= parent2[i]
            else:
                counter2+= 1
        
        return child1, child2
    
    def partially_mapped_crossover(self, parent1, parent2):
        
        n_genes, child1, _, pointinit, pointfin = two_point_crossover_init(parent1, parent2)
        
        for i in range(pointinit, pointfin): #crossover comun entre punto inicial y punto final
            child1[i] = parent1[i]
            
        for i in range(pointinit, pointfin):
            gene_value = parent2[i]
            if gene_value not in child1:
                idx = i
                while True:
                    idx = parent2.index(parent1[idx])  #esta es la accion de moverse verticalmente y despues buscar el indice de ese valor en el otro padre
                    if idx < pointinit and idx >= pointfin: #cuando idx cae fuera del intervalo
                        child1[idx] = gene_value            #se inserta el gen elegido en ese lugar
                        break
        
        for i in range(n_genes):
           if parent2[i] not in child1:
               child1[i] = parent2[i]
        
        return child1 #no se si aca hay que hacer los 2 hijos o solo 1, si son los 2 habria que hacer lo de antes de vuelta pero al reves
    
    def cycle_crossover(self, parent1, parent2):
        return parent1
        
    
        
        
def two_point_crossover_init(parent1, parent2):
    n_genes= len(parent1)
    child1= [0]*n_genes
    child2= [0]*n_genes
    
    pointinit=random.randint(0, n_genes) #creamos punto inicial y final de cruce de crossver
    pointfin=random.randint(0, n_genes)
    
    while pointfin == pointinit : #para crear 2 puntos de cruce diferentes
        pointfin=random.randint(0, n_genes)
        
    if pointfin < pointinit: #para que el inicial sea siempre menor que el final
        pointinit, pointfin = pointfin, pointinit
    
    return n_genes, child1, child2, pointinit, pointfin
        
        
        
        
        
        
        
        