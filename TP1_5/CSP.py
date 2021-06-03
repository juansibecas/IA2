

class Graph:
    """
    Clase para crear el grafo de restriccion. Se necesitan:
    _task: Diccionario con las tareas(variables) como Keys y su valor son la duracion de la tarea.
    _ domain: Diccionario con las tareas(variables) como Keys y su valor son los valores q puede tomar.
    _ neighbors: Diccionario con las tareas(variables) como Keys y su valor son las variables que tiene restriones.
    _ assignment: Lista con la Tarea su maquina y hora de inicio
    """
    def __init__(self,total_time,domain,neighbors,time_task,assignment):
        self.time_task=time_task
        self.domain = domain
        self.neighbors = neighbors
        self.assignment = assignment
        self.total_time=total_time

    def heuristic_MRV(self,not_use):
        #la siguiente variable a asignar será aquella que tenga menos valores posibles en su dominio, pero no las q estan en not_use como backtracking
        variable=['T0',0,0] #esta definida con (tarea,numero de maquina, hora inicio)
        nd= self.total_time+1
        flag_allerror=1 
        for var in self.domain:       #recorremos las tareas en el diccionario, que es una lista de tuplas de 2 elemtos
            if self.domain[var] not in not_use:
                flag_allerror=0
                nmachine=self.domain[var][0][0]     #Numero de la maquina para luego comparar.
                list_domain=[]
                for value in self.domain[var]:      
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
        return variable,flag_allerror

    def inference(self,variable): #variable :(tarea,numero de maquina, hora inicio)
        flag_error=0
        self.domain.pop(variable[0])    #Borramos la variable del conjunto
        for x in range(variable[2],variable[2]+self.time_task[variable[0]]):#Iteramos desde el tiempo de inicio de cada variable hasta el tiempo final
            value=(variable[1],x)   #para borrar los valores del dominio que uso esa tarea en la maquina
            for var in self.neighbors[variable[0]]: #iteramos en las variables que tiene resticciones
                flag_delete=0
                for val in self.domain[var]:    #iteramos todos los valores de cada dominio para borralos        
                    if val[0]==variable[1]:     #para ver si usan la misma maquina y borrarlo, pq algunas tareas pueden usar distintas maquinas      
                        self.domain[var].remove(value)
                        break   #solo tenemos que borrar un valor del dominio a la vez
                if self.domain[var]==[]:
                    flag_error=1
        self.neighbors.pop(variable[0])     #Borramos la variable de las reestricciones
        for varn in self.neighbors:         #Borramos las reestricciones de esa variable en las demas      
            if variable[0] in self.neighbors[varn]:
                self.neighbors[varn].remove(variable[0])          
        self.assignment.append(variable)    #asigamos la variable
        return self.domain,self.neighbors,self.assignment,flag_error

