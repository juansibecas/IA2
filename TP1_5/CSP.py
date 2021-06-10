

class Graph:
    """
    Clase para crear el grafo de restriccion. Se necesitan:
    _tasks: Diccionario con las tareas(variables) como Keys y su valor es una tupla con los valores q puede tomar,
    variables que tiene restriones y tiempo de ejecución de la maquina. 
    _ assignment: Lista con la Tarea su maquina y hora de inicio
    """
    def __init__(self,total_time,tasks,assignment):
        self.tasks=tasks
        self.assignment = assignment
        self.total_time=total_time

    def heuristic_MRV(self,not_use,machine):
        #la siguiente variable a asignar será aquella que tenga menos valores posibles en su dominio, pero no las q estan en not_use como backtracking
        variable=['T0',0,0] #esta definida con (tarea,numero de maquina, hora inicio)
        nd= self.total_time+1
        for var in machine:       #recorremos las tareas en el diccionario, que es una lista de tuplas de 2 elemtos
            if var not in not_use:
                nmachine=self.tasks[var][0][0][0]     #Numero de la maquina para luego comparar.
                list_domain=[]
                for value in self.tasks[var][0]:      
                    if value[0]==nmachine:           #Para separar las tareas que pueden usar dos maquinas
                        list_domain.append(value)
                        ndomain=len(list_domain)
                    else:                               
                        if ndomain < nd:    #guardamos los valores en las variables
                            timeini=list_domain[0][1]
                            variable=[var,nmachine,timeini]
                            ndomain=nd
                        list_domain=[]
                        nmachine=value[0]           #Para separar las tareas que pueden usar dos maquinas
                        list_domain.append(value)
                        ndomain=len(list_domain)
                if ndomain < nd:
                        timeini=list_domain[0][1]
                        variable=[var,nmachine,timeini]
                        nd=ndomain
        return variable

    def inference(self,variable,machines): #variable :(tarea,numero de maquina, hora inicio)
        flag_error=0
        time_task=self.tasks[variable[0]][2]
        self.tasks.pop(variable[0])    #Borramos la variable del conjunto
        machines.remove(variable[0])
        for x in range(variable[2],variable[2]+time_task):#Iteramos desde el tiempo de inicio de cada variable hasta el tiempo final
            value=(variable[1],x)   #para borrar los valores del dominio que uso esa tarea en la maquina
            for var in machines: #iteramos en las variables resantes
                flag_delete=0
                for val in self.tasks[var][0]:    #iteramos todos los valores de cada dominio para borralos        
                    if val[0]==variable[1]:     #para ver si usan la misma maquina y borrarlo, pq algunas tareas pueden usar distintas maquinas      
                        self.tasks[var][0].remove(value)
                        break   #solo tenemos que borrar un valor del dominio a la vez
                if self.tasks[var][0]==[]:
                    flag_error=1
        for varn in machines:         #Borramos las reestricciones de esa variable en las demas      
            if variable[0] in self.tasks[varn][1]:
                self.tasks[varn][1].remove(variable[0])          
        self.assignment.append(variable)    #asigamos la variable
        if flag_error==1:
            machines.append(variable[0])
        return self.tasks,self.assignment,flag_error,machines

