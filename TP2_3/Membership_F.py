import math
    
class triangle_membership_function:
    
    def __init__(self, name, center, start, end, dx, flag):
        self.name = name
        self.center = center
        self.start = start
        self.end = end
        self.dx = dx
        self.decimals = math.log10(1/self.dx)
        self.length = int((self.end - self.start)/self.dx + 1)
        self.flag = flag
        self.width = self.end-self.start
        self.slope = 2/(self.end-self.start)
        self.x = []
        self.y = []
    
        
    
    def init_values(self):      #se usa solamente para graficar en realidad
        
        if self.flag == 'first':
            for n in range(1000):                                       #antes de center en la primer memb_func, y(x)=1
                self.x.append(self.start+self.dx*(n-1000))
                self.y.append(1)
        
        for n in range(self.length):
            
            value = round(self.start+n*self.dx, int(self.decimals))     #valor del dominio
            self.x.append(value)
            
            if value <= self.center:                                    #antes del centro, la recta es creciente
                n = self.slope*(value - self.start)
                if self.flag == 'first':                                #si es la primera, antes del centro y(x)=1
                    n = 1
                self.y.append(n)
                
            if value> self.center:                                      #despues del centro, la recta es decreciente  
                n = 1 - self.slope*(value-(self.start+(self.width)/2))
                if self.flag == 'last':                                 #si es la ultima, despues del centro y(x)=1
                    n = 1
                self.y.append(n)
    
        if self.flag == 'last':                                         #despues de center en la ultima memb_func, y(x)=1
            for n in range(1000):
                self.x.append(self.end+n*self.dx)
                self.y.append(1)
    

    def singleton_fuzzifier(self, real_value):          #mismo razonamiento que arriba, se vuelven a calcular porque los anteriores
                                                        #generaban problemas de redondeo
        if real_value <= self.center:                   
            n = self.slope*(real_value - self.start)    #antes del centro la recta es creciente, y si es la primera memb_func, y(x)=1
            if self.flag == 'first':
                n = 1
            return n
            
        if real_value > self.center:                    #despues del centro la recta es decreciente, y si es la ultima memb_func, y(x)=1
            n = 1 - self.slope*(real_value-(self.start+(self.width)/2))
            if self.flag == 'last':
                n = 1
            return n
    
    
    
