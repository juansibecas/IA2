from CSP import Graph
import copy
def create_disc(task,machine,total_time):
    # Asignamos los valores del dominio y vecinos de cada tarea.
    neighbors={}
    domain={}
    time_task={}
    for i in task:              
        listneighbors=[]    #listas vacias para ir guardando los valores de los vecinos y dominio
        listdomain=[]
        for j in machine:
            if i[2]==j[1]:
                for x in range(total_time-i[1]):  #Tenemos el ultimo valor al que puede tomar para no pasarle del tiempo total de produccion. en i[1] esta la duracion de la tarea
                    listdomain.append((j[0],x)) #Guardamos que maquina puede usar y los valores de inicio posibles
        for k in task: #Volvemos a recorrer tdas las tareas y verificamos con cuales otra tarea tiene restricciones para crear los vecinos.
            if i != k:
                if i[2]==k[2]:
                    listneighbors.append("T"+str(k[0]))
        neighbors.setdefault("T"+str(i[0]),listneighbors) #guardamos los valores en los diccionarios
        domain.setdefault("T"+str(i[0]),listdomain)
        time_task.setdefault("T"+str(i[0]),i[1])
    return domain,neighbors,time_task

def csp(index,graph,total_time,domain,neighbors,time_task,assignment,list_not_use):
    if not graph[index].domain:     #Cuando esta vacio quiere decir que termino de asignar todas las tareas
        return print(graph[index].assignment)
    graph.append(Graph(total_time,copy.deepcopy(domain),copy.deepcopy(neighbors),time_task,copy.deepcopy(assignment))) #Creamos grafos de reestriciones en cada iteracion por si queremos hacer backtracking         
    index=index+1
    variable,flag_allerror=graph[index].heuristic_MRV(list_not_use[index-1]) #Elegimos la variable con menor dominios para elegir (heuristica)
    if flag_allerror==1:    #Si todas las variables de ese arbol no llegan a ningun resultado tenemos que volver al nodo anterior
        list_not_use[index].append(graph[index].assignment[index]) #agregamos la asignacion usada que no llevaba a ninguna solucion para no usarla
        graph[index].pop()      #borramos el ultimo grafo
        index=index-1 
        list_not_use[index+1].pop() #borramos estas variables para volver al nodo anterior del arbol
        domain=graph[index].domain
        neighbors=graph[index].neighbors
        assignment=graph[index].assignment
    else:    
        domain,neighbors,assignment,flag_error=graph[index].inference(variable) #Borramos la variable eleiga y sus reestriciones con las demas y podamos el arbol
        if flag_error==1:      #Si esa variable variable da a una solucion no valida hacemos backtracking
            graph[index].pop()  #borramos el grafo ultimo
            index=index-1
            domain=graph[index].domain
            neighbors=graph[index].neighbors
            assignment=graph[index].assignment
            list_not_use[index].append(variable)          #variables para no usar 
        else:
            list_not_use.append([]) 
    csp(index,graph,total_time,domain,neighbors,time_task,assignment,list_not_use) #Iteramos

if __name__ == '__main__':
    task=[[1,10,1], [2,5,1],[3,10,1],[4,15,1],[5,3,2],[6,5,2],[7,10,2]] #Tareas de la forma: [ID, Duracion, Tipo de maquina]
    machine=[[1,1],[2,1],[3,2]] #Maquinas de la forma: [ID,Tipo de maquina]
    total_time=24               #Tomamos una produccion continua de 24 hs                    
    domain,neighbors,time_task=create_disc(task,machine,total_time)
    assignment=[]
    graph=[]
    list_not_use=[]     #hacemos una lista para las variables q no dan ningun resultado, y vamos guardando cada variable en cada nodo del arbol
    list_not_use.append([])
    graph.append(Graph(total_time,copy.deepcopy(domain),copy.deepcopy(neighbors),time_task,copy.deepcopy(assignment))) #Creamos el grafo de restrcciones inicial          
    result=csp(0,graph,total_time,domain,neighbors,time_task,assignment,list_not_use) #Satisfaccion de reestricciones
