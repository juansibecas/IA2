import logging

class FAM:
    
    def __init__(self, names, var1, var2, var_control):
        logging.basicConfig(format = '%(name)s - %(levelname)s - %(message)s',  #en el archivo FAM.log se puede observar que el controlador
                    filename = 'FAM2.log',                                      #funciona correctamente en base a las reglas designadas
                    level=logging.DEBUG)
        self.names = names
        self.var1 = var1              #var 1 t 2 son sensadas, var_control es la calculada por el controlador difuso
        self.var2 = var2
        self.var_control = var_control
        self.rules = {}
        
        for name1 in names:             #se crea el diccionario de reglas vacio
            self.rules[name1] = {}
            for name2 in names:
                self.rules[name1][name2] = ''
    
    def __str__(self):
        return f'theta is {self.value1}, theta_speed is {self.value2}.'
    
    def add_rule(self, name1, name2, name_result): #metodo para llenar las reglas
        self.rules[name1][name2] = name_result
        
    def get_f(self, var1_real_value, var2_real_value, it):  #metodo principal del algoritmo para obtener el valor de f en cada instante
        self.value1 = var1_real_value
        self.value2 = var2_real_value
        
        self.var1.singleton_fuzzifier(var1_real_value) #entradas reales -> fuzzy
        self.var2.singleton_fuzzifier(var2_real_value) #estos metodos afectan a var.names_and_values
        
        rules_to_use = {}         #diccionario con las reglas que se activan en el instante en analisis, por ej si theta y theta' son Z, f es Z     
        
        for name1 in self.var1.names_and_values:        #se buscan todas las combinaciones de los nombres de var1 y var 2  
            for name2 in self.var2.names_and_values:    #por ej si theta es Z y NP, y theta' es PG y PP, obtenemos Z-PG, Z-PP, NP-PG y NP-PP  
                rule_result = self.rules[name1][name2]  #se comparan esas combinaciones con las reglas de la FAM, y se obtiene el resultado
                self.str = f'theta is {name1}, theta_speed is {name2}, then f is {rule_result}'
                
                value = min(self.var1.names_and_values[name1], self.var2.names_and_values[name2])   #para 2 valores de la misma regla
                                                                                                    #se usa el minimo (conjuncion)
                if it % 1000 == 0:  #cada 1000 iteraciones loguea una entrada
                    logging.info(f'{self} {self.str}, {it}')
                    
                try:
                    if rules_to_use[rule_result] < value:   #si se encuentran 2 reglas con el mismo consecuente, se usa el valor maximo de las 2
                        rules_to_use[rule_result] = value   #try-except hace falta para la primera vez, que el valor no va a existir
                except:
                    rules_to_use[rule_result] = value
                
        return self.var_control.defuzzify(rules_to_use)     #se devuelve el valor de f defuzified