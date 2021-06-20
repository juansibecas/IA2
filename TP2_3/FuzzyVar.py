from Membership_F import triangle_membership_function
import math

class FuzzyVar:
    
    def __init__(self, name, start, end, overlap_percent, dx, ammount_of_membership_functions, memb_func_names):
        self.name = name
        self.start = start
        self.end = end
        self.overlap_percent = overlap_percent
        self.dx = dx
        self.decimals = int(-math.log10(self.dx))
        self.ammount_of_membership_functions = ammount_of_membership_functions
        self.membership_functions = []
        self.names_and_values = {}
        self.memb_func_names = memb_func_names
    
    
        
    def init_membership_functions(self):            #inicializa las n funciones de pertenencia de la variable fuzzy
        n = self.ammount_of_membership_functions
        not_overlapped_memb_functions = n/2 - 0.5 + (n-1)*(0.5 - self.overlap_percent/100)  #calcula cuantos triangulos sin solaparse entran en el dominio
        memb_func_width = (self.end - self.start)/not_overlapped_memb_functions             #se obtiene el ancho de cada triangulo
        center = self.start
        for i in range(self.ammount_of_membership_functions): #se le va pasando valores de start, end y center para cada funcion de pertenencia
            start = center - memb_func_width/2
            end = center + memb_func_width/2
            name = self.memb_func_names[i]
            if i == 0:
                flag = 'first'
            elif i== self.ammount_of_membership_functions-1:
                flag = 'last'
            else:
                flag = 'middle'
            self.membership_functions.append(triangle_membership_function(name, center, start, end, self.dx, flag))
            self.membership_functions[i].init_values()
            center += (self.end - self.start)/(self.ammount_of_membership_functions-1)
            
            
    def singleton_fuzzifier(self, real_value):
        self.names_and_values = {}
        real_value = round(real_value, self.decimals)
        
        for memb_func in self.membership_functions:
            
            case1 = real_value >= memb_func.start and real_value <= memb_func.end   #si se encuentra entre start y end
            case2 = real_value <= memb_func.start and memb_func.flag == 'first'     #si se encuentra antes de start, y es la primer memb_func
            case3 = real_value >= memb_func.end and memb_func.flag == 'last'        #si se encuentra despues de end y es la ultima memb_func
            
            if case1 or case2 or case3: #si se cumple cualquiera de los 3 casos, se aplica el singleton a real_value, para memb_func
                self.names_and_values[memb_func.name] = memb_func.singleton_fuzzifier(real_value) #singleton. x -> y

    def defuzzify(self, rules_to_use): #defuzzifier por promedio ponderado
        num = 0
        den = 0
        for name in rules_to_use:
            den += rules_to_use[name]                       #den es la suma de los valores de las funciones de pertenencia
            for memb_func in self.membership_functions:
                if name == memb_func.name:
                    num += rules_to_use[name]*memb_func.center      #num es la suma de los valores de las funciones de pertenencia
        return num/den                                              #multiplicados por su correspondiente centro en dominio de f
            
            
        