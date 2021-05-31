from CSP import Graph

if __name__ == '__main__':
    task=[[1,10,1], [2,5,1],[3,10,1],[4,15,1],[5,3,2],[6,20,2]] #Tareas de la forma: [ID, Duracion, Tipo de maquina]
    machine=[[1,1],[2,1],[3,2]] #Maquinas de la forma: [ID,Tipo de maquina]
    total_time=24               #Tomamos una produccion continua de 24 hs                    
    graph=Graph(total_time)           
    graph.set_graph(task,machine)    #Creamos el grafo de restrcciones
    graph.search()
