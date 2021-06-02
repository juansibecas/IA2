from CSP import Graph
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

def csp(total_time,domain,neighbors,time_task,assignments,index):
    if not domain:
        return print(assignments)
    graph.append(Graph(total_time,domain,neighbors,time_task,assignments))
    variable=graph[index].heuristic_MRV()
    domain,neighbors,assignments=graph[index].inference(variable,domain,neighbors,assignments)
    index=index+1
    csp(total_time,domain,neighbors,time_task,assignments,index)


if __name__ == '__main__':
    task=[[1,10,1], [2,5,1],[3,10,1],[4,15,1],[5,3,2],[6,20,2]] #Tareas de la forma: [ID, Duracion, Tipo de maquina]
    machine=[[1,1],[2,1],[3,2]] #Maquinas de la forma: [ID,Tipo de maquina]
    total_time=24               #Tomamos una produccion continua de 24 hs                    
    domain,neighbors,time_task=create_disc(task,machine,total_time)
    assignments=[]

    graph=[]
    graph.append(Graph(total_time,domain,neighbors,time_task,assignments)) #Creamos el grafo de restrcciones inicial          
    result=csp(total_time,domain,neighbors,time_task,assignments,1)