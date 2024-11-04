
class Graph:
    def __init__(self):
        self.wonders = {}
    
    def add_wonder(self, nombre, pais, tipo):
        self.wonders[nombre] = {
            'nombre': nombre,
            'pais': pais,
            'tipo': tipo,
            'aristas': []
        }

    def add_distance(self, nombre1, nombre2, distancia):
        if nombre1 in self.wonders and nombre2 in self.wonders:
            self.wonders[nombre1]['aristas'].append({'value': nombre2, 'distance': distancia})
            self.wonders[nombre2]['aristas'].append({'value': nombre1, 'distance': distancia})  

    def kruskal(self, tipo):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = []
        aristas = []

        
        for nodo in self.wonders:
            if self.wonders[nodo]['tipo'] == tipo:
                bosque.append(nodo)
                adjacentes = self.wonders[nodo]['aristas']
                for adjacente in adjacentes:
                    if self.wonders[adjacente['value']]['tipo'] == tipo:
                        aristas.append((nodo, adjacente['value'], adjacente['distance']))

        aristas.sort(key=lambda x: x[2])

        resultado = []  

        while len(bosque) > 1 and aristas:
            arista = aristas.pop(0) 
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])

            if origen is not None and destino is not None:
                if origen != destino:
                    vertice_ori = bosque[origen]
                    vertice_des = bosque[destino]

                   
                    nuevo_vertice = f'{vertice_ori}-{vertice_des}-{arista[2]}'
                    bosque.pop(max(origen, destino))  
                    bosque.pop(min(origen, destino))   
                    bosque.append(nuevo_vertice)       

                    resultado.append(arista)  

        return resultado
                
    def country_wonders(self):
        type_count = {}


        for wonder in self.wonders:
            paises = self.wonders[wonder]['pais']
            tipo = self.wonders[wonder]['tipo']
            
            if not isinstance(paises, list):
                paises = [paises] 
                
            for pais in paises:
                if pais not in type_count:
                    type_count[pais] = {'natural': 0, 'arquitectonica': 0}
                type_count[pais][tipo] += 1  

        countries_with_both = []
        countries_with_more_of_same_type = []
        for pais, counts in type_count.items():
            if counts['natural'] > 0 and counts['arquitectonica'] > 0:
                countries_with_both.append(pais)
            if counts['natural'] > 1 or counts['arquitectonica'] > 1:
                countries_with_more_of_same_type.append(pais)

        return countries_with_both,countries_with_more_of_same_type 

    def show_grafo(self):
        for wonder in self.wonders:
            print(f"{wonder["nombre"]} conectado a: {wonder["aristas"]}")