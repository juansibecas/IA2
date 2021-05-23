from Annealing import Annealing
import random

class Gen:
    def __init__(self, population_length, n, warehouse):
        self.fitness=[]
        self.population=[]
        self.n=n
        tempini = 50
        tempfin = 0.1
        alpha = 0.99
        self.annealing = Annealing(tempini, tempfin, alpha, warehouse)
        
    def GA(self, it, time, tolerance):
        
        for i in range(it): #por ahora puse este limite solamente, una vez vayamos entendiendo mejor podemos agregar un limite de tiempo o de tolerancia
            
            self.calculate_fitness()
            
            self.population.sort(key=sort_by_f)
            
            #self.calculate_pick_probability() no hace falta porque random.choices en pick_fittest lo hace solo
            
            fittest = self.pick_fittest_individuals()
            
            self.population = self.crossover_and_mutation(fittest)
            
            

    def sel_and_rep(self):
        self.set_pop()
        flag=0
        it=0
        while flag==0: #con esto hacemos los metodos de detencion por cantidad de iteraciones o convergencia.

            #self.fitness=[(self.set_fitness(i), i) for i in self.population] #calculamosel fitnes de cada individuo y ordenamos para luego seleccionarlos
        
            #self.order_crossover()          #ahora hacemos los cruces entre los 
            #self.partially_mapped_crossover()
            #self.cycle_crossover()
            it+=1
            if it==100:
                flag=1
        return population #aca tenemos que retornar el de menor fitnes
    def order_crossover(self, parent1, parent2): #aca hay que ver despues como hacemos, si mandamos los padres como parametros, si los elegimos afuera o adentro, etc
                                                #Facu:creo q es mejor pasar la población como parametro y retornar otra población
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
        n_genes= len(parent1)
        child1 = [-1]*n_genes
        child2 = [-1]*n_genes
        cycles = [] #lista de ciclos. cada ciclo es una lista con los indices que le corresponden
        cycle_number = 0
        flag = 0
        
        for i in range(n_genes):    
            idx = i
            for cycle in cycles:  #se hace esto para no obtener ciclos repetidos (si un indice ya entro en un ciclo, pasa al siguiente indice)
                if idx in cycle:
                    flag = 1
                    break
            if flag == 1:
                flag = 0
                continue
            while True:  #parecido al de pmx
                try:
                    cycles[cycle_number].append(idx)
                except:
                    cycles.append([]) #la primera vez que entre al while, va a pasar por aca para agregar la lista del ciclo nuevo
                    cycles[cycle_number].append(idx)
                idx = parent2.index(parent1[idx]) #esta es la accion de moverse verticalmente y en diagonal hacia el indice que corresponda
                if idx in cycles[cycle_number]: #cuando se complete el ciclo va a entrar aca y romper el while
                    cycle_number+= 1
                    break
        
        for counter, cycle in enumerate(cycles):
            for idx in cycle:
                if counter % 2 == 0:            #en los ciclos pares child1 toma de parent1
                    child1[idx] = parent1[idx]
                    child2[idx] = parent2[idx]
                else:                           #en los ciclos impares child1 toma de parent2 
                    child1[idx] = parent2[idx]
                    child2[idx] = parent1[idx]

        return child1, child2
    
    
    def insertion_mutation(self, individual): #se inserta un gen en una posicion y se desplaza el resto hacia la derecha
        n_genes = len(individual)
        child = [-1]*n_genes
        idx1 = random.randint(0, n_genes-1)
        idx2 = random.randint(0, n_genes-1)
        
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
            
        child[idx1] = individual[idx1]
        child[idx1+1] = individual[idx2]
                                            #llenado del "hijo" en 3 partes
        for i in range(idx1):               #desde el inicio hasta el indice del primer gen
            child[i] = individual[i]
            
        for i in range(idx1+2, idx2+1):     #del primer gen al segundo. idx1+2 porque los 2 genes seleccionados ya se colocaron manualmente
            child[i] = individual[i-1]      #idx2+1 porque tiene que rellenar hasta idx2. i-1 en individual porque los indices quedan desfasados 1 lugar
        
        for i in range(idx2+1, n_genes):    #segundo gen hasta el final
            child[i] = individual[i]
                
        return child
        
    def exchange_mutation(self, individual): #se eligen 2 genes y se intercambian
        n_genes = len(individual)
        idx1 = random.randint(0, n_genes-1)
        idx2 = random.randint(0, n_genes-1)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        
        return individual
    
    def mixing_mutation(self, individual):
        n_genes = len(individual)
        genes_to_mix = random.randint(2, n_genes) #cantidad de genes a mezclar
        indexes = random.sample(range(n_genes), genes_to_mix) #indices de los genes a mezclar
        genes = []
        for idx in indexes:
            genes.append(individual[idx])
        random.shuffle(genes)
        for i, j in zip(indexes, range(genes_to_mix)):  #en los indices como estaban ordenados en un principio
            individual[i] = genes[j]                    #se colocan los genes mezclados
        
        return individual

def normalize(value, xi, xf):
    return (value - xi)/(xf - xi)
        
def sort_by_f(individual):
    return individual.fitness

def two_point_crossover_init(parent1, parent2):
    n_genes= len(parent1)
    child1 = [-1]*n_genes #los inicializo con -1 porque el 0 es un gen valido y puede complicar algunos crossovers y/o mutaciones
    child2 = [-1]*n_genes
    
    pointinit=random.randint(0, n_genes) #creamos punto inicial y final de cruce de crossver
    pointfin=random.randint(0, n_genes)
    
    while pointfin == pointinit : #para crear 2 puntos de cruce diferentes
        pointfin = random.randint(0, n_genes)
        
    if pointfin < pointinit: #para que el inicial sea siempre menor que el final
        pointinit, pointfin = pointfin, pointinit
    
    return n_genes, child1, child2, pointinit, pointfin
        
        
class Individual:
    
    def __init__(self, genes):
        self.genes = genes
        self.f = -1
        self.p = -1
        
    def set_f(self, f):
        self.f = f
        
    def set_p(self, p):
        self.p = p
        
        
        
        
        