import random

class Gen:
    def __init__(self,shelves,n):
        self.fitness=[]
        self.population=[]
        self.shelves=shelves
        self.n=n
    
    def individuals(self): #creamos los individuos inicial con una lista ramdon sample
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

    def crossover_ordercross(self,selected):
        nind=len(self.shelves)#tamaño del individuo
        pointinit=random.randint(0,nind-1) #creamos punto inicial y final de cruce de crossver
        pointfin=random.randint(0,nind-1)
        while pointfin == pointinit : #para crear 2 puntos de cruce diferentes
            pointfin=random.randint(0,nind-1)
        father = random.sample(selected, 2)
        for i in range(len(population)):
            self.population[i]