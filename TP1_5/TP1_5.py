from CSP import Graph
import copy

def create_disc(task,machine,total_time):
    # Asignamos los valores del dominio, vecinos y tiempo de ejecucion de cada tarea. Asignamos cada tarea en un tipo de maquina
    tasks = {} #diccionario con key:tarea, values:(dominio,vecinos,tiempo de ejecucion)
    machines={}
    mac=0
    for m in range(len(machine)):  #guardamos las tareas dentro de cada tipo de maquina
        if machine[m][1] != mac:
            machines.setdefault(machine[m][1],[])
            print(machines)     
    for i in task:              
        listneighbors=[]    #listas vacias para ir guardando los valores de los vecinos y dominio
        listdomain=[]
        for j in machine:
            if i[2]==j[1]:
                if "T"+str(i[0]) not in machines[j[1]] :
                    machines[j[1]].append("T"+str(i[0]))
                for x in range(total_time-i[1]):  #Tenemos el ultimo valor al que puede tomar para no pasarle del tiempo total de produccion. en i[1] esta la duracion de la tarea
                    listdomain.append((j[0],x)) #Guardamos que maquina puede usar y los valores de inicio posibles
        for k in task: #Volvemos a recorrer tdas las tareas y verificamos con cuales otra tarea tiene restricciones para crear los vecinos.
            if i != k:
                if i[2]==k[2]:
                    listneighbors.append("T"+str(k[0]))
        value=(listdomain,listneighbors,i[1])
        tasks.setdefault("T"+str(i[0]),value)   #guardamos los valores en el diccionario
    return tasks,machines

def csp(index,graph,total_time,tasks,assignment,list_not_use,machines):
    flag_allerror=0
    flag=0
    machine_complete=copy.deepcopy(machines)
    while flag==0:      #Iteramos
        if not machines:     #Cuando esta vacio quiere decir que termino de asignar todas las tareas
            flag=1
        else:
            graph.append(Graph(total_time,copy.deepcopy(tasks),copy.deepcopy(assignment))) #Creamos grafos de reestriciones en cada iteracion por si queremos hacer backtracking         
            index=index+1
            variable=graph[index].heuristic_MRV(list_not_use[index-1],machines) #Elegimos la variable con menor dominios para elegir (heuristica)    
            tasks,assignment,flag_error,machines=graph[index].inference(variable,machines) #Borramos la variable eleiga y sus reestriciones con las demas y podamos el arbol
            print(list_not_use)
            if flag_error==1:      #Backtracking: Si esa variable variable da a una solucion no valida hacemos backtracking
                graph.pop()  #borramos el grafo ultimo y volvemos a asignar las variables anteriores para eliminar las erroneas
                index=index-1
                tasks=graph[index].tasks
                assignment=graph[index].assignment
                list_not_use[index].append(variable[0])          #variables para no usar
                if len(list_not_use[index])==len(machines) and len(machines)!=0 : #Backtracking: Si todas las variables de ese arbol no llegan a ningun resultado tenemos que volver al nodo anterior
                    flag_allerror = 1
                while flag_allerror==1: #Por si tenemos que seguir volviendo a nodos anteriores
                    index=index-1
                    list_not_use[index].append(graph[index+1].assignment[index][0]) #agregamos la asignacion usada que no llevaba a ninguna solucion para no usarla
                    machines.append(graph[index+1].assignment[index][0])
                    graph.pop()      #borramos el ultimo grafo
                    list_not_use.pop() #borramos estas variables para volver al nodo anterior del arbol
                    tasks=graph[index].tasks
                    assignment=graph[index].assignment
                    if len(list_not_use[index])!=len(machines):
                        flag_allerror=0
                    if len(list_not_use[index]) == len(machine_complete): #si llegamos a que no podemos tener 
                        return "error","error","error" 
            else:
                list_not_use.append([]) 
    return index,tasks,assignment     

if __name__ == '__main__':
    task=[[1,10,1], [2,5,1],[3,17,1],[4,13,1],[5,1,2],[6,11,2],[7,10,2]] #Tareas de la forma: [ID, Duracion, Tipo de maquina]
    machine=[[1,1],[2,1],[3,2]] #Maquinas de la forma: [ID,Tipo de maquina]
    total_time=24               #Tomamos una produccion continua de 24 hs                    
    tasks,machines=create_disc(task,machine,total_time)
    assignment=[]
    graph=[]
    list_not_use=[]     #hacemos una lista para las variables q no dan ningun resultado, y vamos guardando cada variable en cada nodo del arbol
    list_not_use.append([])
    graph.append(Graph(total_time,copy.deepcopy(tasks),copy.deepcopy(assignment))) #Creamos el grafo de restrcciones inicial          
    index=0
    for mach in machines:
        index,tasks,assignment=csp(index,graph,total_time,tasks,assignment,list_not_use,machines[mach]) #Satisfaccion de reestricciones
        if assignment=="error":
            print("No se pueden asignar completamente esas tareas en la maquina de tipo: "+ str(mach))
            break
    if assignment == "error":
        print("No se pueden asignar completamente esas tareas")
    else:
        print("La asignacion completa de la forma ['Tarea','numero de maquina','tiempo de inicio'] es: \n")
        print(assignment)


        
    
            
