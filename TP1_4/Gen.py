from Annealing import Annealing
import random
import time
from copy import copy

class Gen:
    def __init__(self, population_length, warehouse, orders, temp_ini, temp_fin, alpha):
        self.population_length = population_length
        self.shelves = warehouse.shelves       
        self.orders = orders
        self.population = []
        self.warehouse = warehouse
        self.annealing = Annealing(temp_ini, temp_fin, alpha, warehouse)
        self.t0 = time.time()
        self.generation = -1
    
    def __str__(self):
        t1 = time.time()
        self.generation += 1
        return f'generation {self.generation} complete, time elapsed: {t1-self.t0}\n lowest avg length: {self.population[0].f}'
    
    def population_init(self):
        for individual_idx in range(self.population_length):
            genes_numbers_only = random.sample(range(len(self.shelves)), len(self.shelves))
            genes_with_a_P = []
            for i in genes_numbers_only:
                genes_with_a_P.append('P' + str(i))
            self.population.append(Individual(genes_with_a_P))
            
        self.calculate_fitness()
        
        self.population.sort(key=sort_by_fn, reverse = True) #se ordena descendiente segun f porque fn=1 es el mas apto (menor costo de camino)
        
        print(f"{self}")
        
    def GA(self, max_it, max_time, tolerance):
        
        lowest_avg_lengths = []
        t0 = time.time()
        it = 0
        
        while True:
            
            fittest = self.pick_fittest_individuals()
            
            self.population.extend(self.crossover_and_mutation(fittest))
            
            self.calculate_fitness()
            
            self.population.sort(key=sort_by_fn, reverse = True) #se tiene que ordenar la lista antes de remove_weakest()
            
            self.remove_weakest()
            
            self.calculate_fitness() #repito calculate fitness varias veces para recalcular los fn, que es una operacion corta en tiempo
                                     #los f no se vuelven a calcular si ya tienen un valor asignado
            
            print(f"{self}")
            
            #criterios de finalizacion
            
            it += 1
            t1 = time.time()
            lowest_avg_lengths.append(self.population[0].f)
            
            if it > 10: #aca puse 10 para calcular el cambio entre el ultimo y el decimo ultimo
                change = (lowest_avg_lengths[-10] - lowest_avg_lengths[-1])/lowest_avg_lengths[-10]
            else:
                change = 100
            if it == max_it or t1-t0 > max_time or change < tolerance:
                break

    def calculate_fitness(self):  #van a tener que estar normalizados y ordenados al reves (el de recorrido mas chico = 1, el de recorrido mas grande=0)
        fsn=[] #fitness sin normalizar
        for individual in self.population:
            f_orders=[]
            if individual.f == -1: #para que no se vuelva a hacer el calculo si ya se habia hecho para ese individuo
                for order in self.orders:
                    mapped_order = order.calculate_mapped_order(individual.genes, self.shelves) #mapea la orden segun el individuo
                    _, total_path_length = self.annealing.simulated_annealing(mapped_order)     #calculo de pasos para cada orden
                    f_orders.append(total_path_length)                                          #se guardan los pasos de cada orden para ese ind
                self.warehouse.write_db_to_file() #se escribe en "memoria cache"
                avg_path=sum(f_orders)/len(f_orders)
                fsn.append(avg_path)
                individual.set_f(avg_path)
            else:
                fsn.append(individual.f)
        max_path=max(fsn)
        min_path=min(fsn)
        for individual, f_value in zip(self.population, fsn):         #como los valores mas aptos son los mas bajos, hay que invertir la escala
            individual.set_fn(normalize(f_value, max_path, min_path)) #por eso mando min y max al reves que como esta en la func de normalizacion
        

    def calculate_pick_probability(self): #al final no se usa porque random.choices lo hace solo con weights en pick_fittest
        f_sum = 0
        for individual in self.population:
            f_sum += individual.f
        for individual in self.population:
            p = individual.f / f_sum
            individual.set_p(p)
            
    def pick_fittest_individuals(self):
        n = 5                               #fraccion 1/n de la poblacion se va a tener en cuenta
        k = round(len(self.population)/n)
        if k<2: k=2
        fitnesses = []
        for individual in self.population:
            fitnesses.append(individual.fn)
        fittest = random.choices(self.population, weights = fitnesses, k=k) #weights aporta la probabilidad de elegir a cada individuo p[i]=f[i]/sum(f)
        
        return fittest
    
    def remove_weakest(self):
        excess_population = len(self.population) - self.population_length #en este paso la poblacion es de 20 + los que se generaron en crossover
        temp_population = copy(self.population)
        for idx in range(self.population_length, self.population_length + excess_population): #como la poblacion ya estaba ordenada, se sacan los sobrantes al final
            individual_to_remove = temp_population[idx]
            self.population.remove(individual_to_remove)
        
    def crossover_and_mutation(self, fittest_selection):
        k=1 #variar segun la cantidad de crossovers que se quieran hacer, pmx larga 1 hijo y los otros largan de a 2
        ammount_of_crossovers = int(len(self.population)/k)
        new_population = []
        
        for n in range(ammount_of_crossovers): #crossover
            parent1 = random.choice(fittest_selection).genes
            parent2 = random.choice(fittest_selection).genes
            child1 = self.partially_mapped_crossover(parent1, parent2) #aca se puede variar el metodo de crossover, tambien hay que cambiar el k
            new_population.append(Individual(child1))
            #new_population.append(Individual(child2))
        
        for individual in new_population: #mutacion
            mutated_genes = self.insertion_mutation(individual.genes) #aca se puede variar el metodo de mutacion
            individual = Individual(mutated_genes)
            
        return new_population

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
                    if idx < pointinit or idx >= pointfin: #cuando idx cae fuera del intervalo - ES UN OR, NO AND
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

def normalize(value, xmin, xmax):
    return (value - xmin)/(xmax - xmin)
        
def sort_by_fn(individual):
    return individual.fn

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
        self.fn = -1
        
    def set_f(self, f):
        self.f = f
    
    def set_fn(self, fn):
        self.fn = fn

    def set_p(self, p):
        self.p = p
        
        
        
        
        