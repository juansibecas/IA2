from Annealing import Annealing
from Warehouse import Warehouse
import random
from copy import copy
import time
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
import numpy as np



if __name__=='__main__':
    columns = 16  #para el genético trabajamos con 16, 13, 3, 6
    rows = 13
    dx = 3
    dy = 6
    temp_ini = 50
    temp_fin = 0.1
    alph = 0.9
    k = 20 #cantidad de productos en la lista de pick
    m = 100 #cantidad de ordenes
    plt.xlim(0, 1)
    t1 = time.time()
        
    warehouse = Warehouse(rows,columns, dx, dy)
    warehouse.create_aisles()
    shelves = warehouse.create_shelves()

    scaler = preprocessing.MinMaxScaler()
    temperature=[]
    energy=[]
    for i in range (m):
       
        initial_picks = []    
    
        for i in range(k):
            initial_picks.append([random.randint(0,rows-1), random.randint(0,columns-1)]) #no hace falta que uses el create_prod.
                                                                    #cambie el astar para que admita el caso de las estanterias tambien
                                                                    
        #print("lugares a visitar:", initial_picks) 
        
        annealing = Annealing(temp_ini, temp_fin, alph, initial_picks, warehouse)
        
        order_temp, total_path_length = annealing.simulated_annealing(initial_picks)
        
        temperature.append(annealing.temperature)
        energy.append(annealing.energy)
        
        """
        order_temp = list(map(tuple,order_temp))
        picknumber = {(n,j): i for i, (n,j) in enumerate(initial_picks)} #con lista de tuplas funca
        result = list(map(picknumber.get, order_temp))
        print("longitud total a recorrer:", total_path_length)
        print("El orden adecuado de pick es: ")
        print(result)
        """
    warehouse.write_db_to_file()
    t2 = time.time()
    print("tiempo de ejecucion:", t2-t1)   
           
    n=[]
    n=list(range(np.shape(np.transpose(np.array(temperature)))[1]))

    temp_df = pd.DataFrame(np.flip(np.transpose(np.array(temperature))), columns=n)
    scaled_temp = scaler.fit_transform(temp_df)
    scaled_temp = pd.DataFrame(scaled_temp)
    
    energy_df = pd.DataFrame(np.flip(np.transpose(np.array(energy))), columns=n)
    scaled_energy = scaler.fit_transform(energy_df)
    scaled_energy = pd.DataFrame(scaled_energy)    
    
    for i in range (m):
        plt.plot(scaled_temp.iloc[:,i],scaled_energy.iloc[:,i])
    plt.show()
    
