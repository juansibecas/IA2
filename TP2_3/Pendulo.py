import numpy as np
import matplotlib.pyplot as plt
from scipy import constants


CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

# Simula el modelo del carro-pendulo.
# Parametros:
#   t_max: tiempo maximo (inicia en 0)
#   delta_t: incremento de tiempo en cada iteracion
#   theta_0: Angulo inicial (grados)
#   v_0: Velocidad angular inicial (radianes/s)
#   a_0: Aceleracion angular inicial (radianes/s2)
def simular(t_max, delta_t, theta_0, v_0, a_0, object_to_get_f_from):
  theta = (theta_0 * np.pi) / 180
  v = v_0
  a = a_0

  # Simular
  ac = []
  vel = []
  y = []
  applied_force = []
  x = np.arange(0, t_max, delta_t)
  it = 0 
  for t in x:
    f = -object_to_get_f_from.get_f(theta, v, it)    #se agrego el objeto para obtener la fuerza 
    a = calcula_aceleracion(theta, v, f)
    v = v + a * delta_t
    theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
    
    #obtencion de datos para graficar y analizar
    y.append(theta) 
    vel.append(v)
    ac.append(a)
    applied_force.append(f)
    it += 1
  fig, ax = plt.subplots()
  ax.plot(x, y, label = 'Theta')
  #ax.plot(x, vel, label = 'Velocidad')
  ax.plot(x, ac, label = 'Aceleración')
  #ax.plot(x, applied_force, label = 'Fuerza Aplicada')
  ax.legend()
  ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
  ax.grid()
  
  plt.show()
  
  return y, ac, x, vel

# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador


