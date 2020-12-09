import math 

def distancia_euclidiana (x_1, y_1, x_2, y_2): 
    return math.sqrt(pow(x_2-x_1,2)+pow(y_2-y_1,2))

def busqueda_profundidad(grafo,origen):

    print('\n\nBusqueda en profundidad')  
    visitados = []
    pila = []

    pila.append(origen)
    while len(pila) > 0:
        actual = pila.pop()
        if actual not in visitados:
            print(actual)   
            visitados.append(actual)
        for key in grafo[actual]:
            if key not in visitados:
                pila.append(key)                          
    return " "   

def busqueda_amplitud(grafo,origen):

    print('\n\nBusqueda en amplitud')  
    visitados = []
    cola =[]

    cola.append(origen)
    while len(cola) > 0:
        actual = cola.pop(0)
        if actual not in visitados:
            print(actual)   
            visitados.append(actual)
        for key in grafo[actual]:
            if key not in visitados:
                cola.append(key)                          
    return " "     