from grafo import Graph


ambientes = [
    "cocina", "comedor", "cochera", "quincho", 
    "baño 1", "baño 2", "habitación 1", 
    "habitación 2", "sala de estar", "terraza", "patio"
]

grafo = Graph(dirigido=False)
for ambiente in ambientes:
    grafo.insert_vertice(ambiente)


grafo.insert_arista("cocina", "comedor", 3)
grafo.insert_arista("cocina", "cochera", 5)
grafo.insert_arista("cocina", "baño 1", 5)
grafo.insert_arista("comedor", "quincho", 4)
grafo.insert_arista("comedor", "habitación 1", 6)
grafo.insert_arista("comedor", "sala de estar", 6)
grafo.insert_arista("cochera", "baño 2", 8)
grafo.insert_arista("quincho", "terraza", 5)
grafo.insert_arista("habitación 1", "habitación 2", 4)
grafo.insert_arista("habitación 2", "patio", 2)
grafo.insert_arista("sala de estar", "terraza", 7)
grafo.insert_arista("terraza", "patio", 6)




arbol_expansion = grafo.kruskal("cocina")
print("Árbol de expansión mínima:", arbol_expansion)


total_distancia = 0

for arista in arbol_expansion:
    if "-" in arista:
        
        subaristas = arista.split(";")
        
       
        for subarista in subaristas:
            partes = subarista.split("-")
            peso = int(partes[-1])  
            total_distancia += peso
    else:
    
        continue

print("Total de distancia en metros de cables necesarios para conectar todos los ambientes:", total_distancia)


camino = grafo.dijkstra('habitación 1')
destino = 'sala de estar'
distancia_total = None


while camino.size() > 0:
    value = camino.pop()

    if value[1][0] == destino:
        if distancia_total is None:
            distancia_total = value[0]


print("Distancia mínima de cable de red para conectar el router con el SmartTV:", distancia_total)
