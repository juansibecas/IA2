

class Graph:
    """
    Clase para crear el grafo de restriccion. Se necesitan:
    _task: Diccionario con las tareas(variables) como Keys y su valor son la duracion de la tarea.
    _ domain: Diccionario con las tareas(variables) como Keys y su valor son los valores q puede tomar.
    _ neighbors: Diccionario con las tareas(variables) como Keys y su valor son las variables que tiene restriones.
    _ constraint: funcion que recibe dos variables y retorna True/False si se cumple la reestriccion o no.
    _ assignment: Lista con la Tarea su maquina y hora de inicio
    _ csp_act: Copiamos el grafo de restricciones actual para luego hacer el backtracking en caso de ser necesario
    """
    def __init__(self,total_time,domain,neighbors,time_task,assignment):
        self.time_task=time_task
        self.domain = domain
        self.neighbors = neighbors
        self.assignment = assignment
        self.total_time=total_time

    def heuristic_MRV(self):
        #la siguiente variable a asignar será aquella que tenga menos valores posibles en su dominio
        variable=['T0',0,0] #esta definida con (tarea,numero de maquina, hora inicio)
        nd= self.total_time+1 
        for var in self.domain:       #recorremos las tareas en el diccionario, que es una lista de tuplas de 2 elemtos
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
        return variable

    def inference(self,variable,domain,neighbors,assignments):
        domain.pop(variable[0])
        for x in range(variable[2]+self.time_task[variable[0]]):
            value=(variable[1],x)
            for var in domain:
                flag_delete=0
                for val in domain[var]:
                    if val[0]==variable[1]:
                        if flag_delete==0:
                            domain[var].remove(value)
                            flag_delete=1
        neighbors.pop(variable[0])
        for varn in neighbors: 
            if variable[0] in neighbors[varn]:
                neighbors[varn].remove(variable[0])          
        assignments.append(variable)
        self.domain=domain
        self.neighbors=neighbors
        self.assignment=assignments
        return domain,neighbors,assignments