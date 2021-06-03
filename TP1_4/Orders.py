class Order:
    def __init__(self, name, init_pos):
        self.name = name
        self.products = []
        self.order_length = 0
        self.init_pos = init_pos

    def setorder(self, products):
        self.products = products
        self.order_length = len(self.products)
    
    def getorder(self):
        print(self.products)
        
    def calculate_mapped_order(self, individual, shelves):
        mapped_order = []        #a la orden hay que sumarle el inicio y la vuelta a un deposito {self.init_pos}
        mapped_order.append(self.init_pos)
        
        for i in range(self.order_length):
            pos = shelves[individual.index(self.products[i])]
            mapped_order.append(pos) #este es el mapeo
            
        mapped_order.append(self.init_pos) #annealing no esta funcionando cuando tiene esto
        return mapped_order
        
        



        
