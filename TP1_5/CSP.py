

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
    def __init__(self,total_time):
        self.task={}
        self.domain = {}
        self.neighbors = {}
        self.assignment = []
        self.csp_act=[]
        self.total_time=total_time

    def set_graph(self,task,machine):
        # Asignamos los valores del dominio y vecinos de cada tarea.
    
        for i in task:              
            listneighbors=[]    #listas vacias para ir guardando los valores de los vecinos y dominio
            listdomain=[]
            for j in machine:
                if i[2]==j[1]:
                    for x in range(self.total_time-i[1]):  #Tenemos el ultimo valor al que puede tomar para no pasarle del tiempo total de produccion. en i[1] esta la duracion de la tarea
                        listdomain.append((j[0],x)) #Guardamos que maquina puede usar y los valores de inicio posibles
            for k in task: #Volvemos a recorrer tdas las tareas y verificamos con cuales otra tarea tiene restricciones para crear los vecinos.
                if i != k:
                    if i[2]==k[2]:
                        listneighbors.append("T"+str(k[0]))
            self.neighbors.setdefault("T"+str(i[0]),listneighbors) #guardamos los valores en los diccionarios
            self.domain.setdefault("T"+str(i[0]),listdomain)
            self.task.setdefault("T"+str(i[0]),i[1])
        self.csp_act.append((self.assignment))
        #print(self.csp_act)

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

    def inference(self,variable):
        self.domain.pop(variable[0])
        for x in range(0,variable[2]+self.task[variable[0]]):
            value=(variable[1],x)
            for var in self.domain:
                flag_delete=0
                for val in self.domain[var]:
                    if val[0]==variable[1]:
                        if flag_delete==0:
                            self.domain[var].remove(value)
                            flag_delete=1          
        self.assignment.append(variable)
        self.csp_act.append((self.assignment))
        self.search()

    def search(self):
        if not self.domain:
            return print(self.assignment)
        variable=self.heuristic_MRV()
        self.inference(variable)
            

    

