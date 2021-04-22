import random
from copy import copy

class Espacio:
    
    def __init__(self, rev, dx, dim):
        self.rev = rev
        self.dx = dx
        self.dim = dim
        self.fixed_coords = 2
        
        self.obstacles = []
        
    def create_obstacles(self, percent, n):
        temp = []
        obstacles_percent = round(percent*pow(self.rev/self.dx, self.dim - self.fixed_coords)/100)
        value = []
        index = []
        lst = []
        for i in range(n):
            for j in range(self.dim):
                lst.append(j)
            for j in range(self.fixed_coords):
                value.append(random.randrange(0, self.rev, self.dx))
                index.append(random.choice(lst))
                lst.remove(index[j])
                    
            for j in range(obstacles_percent):     
                for k in range(self.dim):          
                    temp.append(random.randrange(0, self.rev, self.dx))
                for k in range(self.fixed_coords):
                    temp[index[k]] = value[k]
                    
                self.obstacles.append(copy(temp))
                temp.clear()
            index.clear()
            value.clear()
            lst.clear()
        
        
        
    def find_neighbours(self, pos):
        neighbours = []
        for a in range(pos[0]- self.dx, pos[0]+2*self.dx, self.dx):
            for b in range(pos[1]- self.dx, pos[1]+2*self.dx, self.dx):
                for c in range(pos[2]- self.dx, pos[2]+2*self.dx, self.dx):
                    for d in range(pos[3]- self.dx, pos[3]+2*self.dx, self.dx):
                        for e in range(pos[4]- self.dx, pos[4]+2*self.dx, self.dx):
                            for f in range(pos[5]- self.dx, pos[5]+2*self.dx, self.dx):     
                                neighbours.append([a, b, c, d, e, f]) #todo delete actual position
        for j in neighbours:
            if j in self.obstacles:
                neighbours.remove(j)
                
        return neighbours
        
    def check_limits(self, n):
        if n > self.rev:
            return self.rev
        elif n < 0:
            return 0
        else: 
            return n

def combinations(pos, acc=[[]] * 3):
    if len(pos) == 0:
        return acc
    else:
        return combinations(pos[1:],
                            acc = \
                            [x + [y] for x in acc for y in pos[0]])