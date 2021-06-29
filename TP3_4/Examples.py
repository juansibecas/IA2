import numpy as np
import matplotlib.pyplot as plt

def generar_mas_datos_clasificacion(cantidad_ejemplos, cantidad_clases):

    n = int(cantidad_ejemplos / 9)

    x = np.zeros((cantidad_ejemplos, 2))

    t = np.zeros(cantidad_ejemplos, dtype="uint8")

    randomgen = np.random.default_rng()
    
    shapes = ['square', 'square', 'square', 
              'circle', 'circle', 'circle', 
              'triangle', 'triangle', 'triangle']
    
    #shape 1
    center = [-0.25, 0.25]
    length = 0.2
    
    for shape in range(len(shapes)):
        
        if shape % 3 == 0:
            c = 1
        elif shape % 3 == 1:
            c = 2
        else:
            c = 3
        
        if shapes[shape] == 'square':
            x1, x2, classes = draw_square(center, length, randomgen, n, c)
        elif shapes[shape] == 'circle':
            x1, x2, classes = draw_circle(center, length, randomgen, n, c)
        elif shapes[shape] == 'triangle':
            x1, x2, classes = draw_triangle(center, length, randomgen, n, c)
        
        
        
        indices = range(shape * n, (shape + 1) * n)
        x[indices] = np.c_[x1, x2]
        t[indices] = classes
        
        if center[0] == 0.25:
            center[0] = -0.25
            center[1] -= 0.25
        else:
            center[0] += 0.25
        
    return x,t

def draw_square(center, length, randomgen, n, c):      
    n = int(n/c)
    x1 = []
    x2 = []
    classes = []
    x_center = center[0] - length*(c/2-0.5)/c
    d_center = length/c
    
    for i in range(c):
        x1 = np.append(x1, x_center + length/c*randomgen.uniform(-0.5, 0.5, n))
        x2 = np.append(x2, center[1] + length*randomgen.uniform(-0.5, 0.5, n))
        classes = np.append(classes, [i+1]*n)
        x_center += d_center
        
    return x1, x2, classes
        

def draw_circle(center, diameter, randomgen, n, c):
    n = int(n/c)
    x1 = []
    x2 = []
    theta = 0
    d_theta = 2*np.pi/c
    classes = []
    for i in range(c):
        angulos = randomgen.uniform(theta, theta + d_theta, n)
        random_nums = randomgen.uniform(0, 0.5, n)
        x1 = np.append(x1, center[0] + np.cos(angulos)*random_nums*diameter)
        x2 = np.append(x2, center[1] + np.sin(angulos)*random_nums*diameter)
        theta += d_theta
        classes = np.append(classes, [i+1]*n)
    
    return x1, x2, classes       
        
def draw_triangle(center, length, randomgen, n, c):
    y_base = center[1] - length/2
    
    x1 = center[0] + length*randomgen.uniform(-0.5, 0.5, n)
    x2 = np.zeros(n)
    for idx, x in enumerate(x1):
        if x <= center[0]:
            x2[idx] = y_base + np.tan(np.pi/3)*(x - (center[0] - length/2))*randomgen.uniform()

        else:
            x2[idx] = 1.5*y_base + length*np.cos(np.pi/6) - np.tan(np.pi/3)*(x - (center[0] + length/2))*randomgen.uniform()

    classes = [1]*n
    return x1, x2, classes
    
x, t = generar_mas_datos_clasificacion(cantidad_ejemplos = 27000, cantidad_clases = 3)


plt.scatter(x[:, 0], x[:, 1], c=t)
plt.title("Set Training")