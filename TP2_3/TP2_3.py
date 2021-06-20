## fuzzy controler

import matplotlib.pyplot as plt
from FuzzyVar import FuzzyVar
from FuzzyAbstractMachine import FAM
import Pendulo
import time
import math

def run():
    ammount_of_membership_functions = 5 #se puede cambiar ajustando la tabla de rules a nxn. valores posibles 3, 5, 7
    overlap_percent = 50
    theta_max = math.pi/4
    theta_speed_max = 1
    f_max = 50
    N = 1000 #discretizacion en las funciones de pertenencia (se usa solamente para graficarlas)
    start = [-theta_max, -theta_speed_max, -f_max]
    end = [theta_max, theta_speed_max, f_max]
    names = ['Theta', 'Theta_speed', 'F']
    dx = []
    for i in range(len(start)):
        num = (end[i]-start[i])/N
        dx.append(num)
    
    if ammount_of_membership_functions == 3:        #nombres hardcodeados para los 3 casos
        memb_func_names = ['N', 'Z', 'P']
    elif ammount_of_membership_functions == 5:
        memb_func_names = ['NG', 'NP', 'Z', 'PP', 'PG']
    elif ammount_of_membership_functions == 7:
        memb_func_names = ['NG', 'NM', 'NP', 'Z', 'PP', 'PM', 'PG']
    
    
    theta = FuzzyVar(names[0], start[0], end[0], overlap_percent, dx[0], ammount_of_membership_functions, memb_func_names)
    
    theta_speed = FuzzyVar(names[1], start[1], end[1], overlap_percent, dx[1], ammount_of_membership_functions, memb_func_names)
    
    f = FuzzyVar(names[2], start[2], end[2], overlap_percent, dx[2], ammount_of_membership_functions, memb_func_names)
    
    variables = {'Theta':theta, 'Theta_speed':theta_speed, 'Applied_force':f}
    
    for var_n, var_key in enumerate(variables):
        var = variables[var_key]
        var.init_membership_functions()
        fig, ax = plt.subplots()
        ax.set(xlabel='var domain', ylabel='u(x)', title='membership function '+ var_key, xlim=(start[var_n], end[var_n]))
        for i in var.membership_functions:
            ax.plot(i.x, i.y)
    
    
    #tabla de doble entrada, columnas theta y filas theta_speed. esta tabla tiene que ser de nxn, siendo n la cantidad de funciones de pertenencia por variable
    rules = [['PG', 'PG', 'PG', 'PP', 'Z'],
             ['PG', 'PG', 'PP', 'Z', 'NP'],
             ['PG', 'PP', 'Z', 'NP', 'NG'],
             ['PP', 'Z', 'NP', 'NG', 'NG'],
             ['Z', 'NP', 'NG', 'NG', 'NG']]
    
    fam = FAM(memb_func_names, theta, theta_speed, f)
    
    for count1, name1 in enumerate(memb_func_names):  #se agregan las reglas a la fuzzy abstract machine
        for count2, name2 in enumerate(memb_func_names):
            fam.add_rule(name1, name2, rules[count1][count2])
    
    
    #simular variables
        
    t_max = 10
    dt = 0.0001
    theta_0 = -45
    v_0 = 0
    a_0 = 0
    
    x, a, v, t = Pendulo.simular(t_max, dt, theta_0, v_0, a_0, fam)
    
    return x, a, v, t, fam
    
    
    
if __name__ == '__main__':
    t1 = time.time()
    y, a, v, t, fam = run()
    t2 = time.time()
    print(t2-t1, 'seconds')