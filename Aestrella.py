import math
def heuristica(actual, final): #función heuristica
    h=0
    for x in range(len(actual)):
        h+=(actual[x]-final[x])**2
    return math.sqrt(h)