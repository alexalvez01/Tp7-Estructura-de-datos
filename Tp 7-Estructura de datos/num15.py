from grafomaravillas import Graph


grafo = Graph()

#Maravillas arquitectonicas

grafo.add_wonder("Chichén Itzá", "México", "arquitectonica")
grafo.add_wonder("Christ the Redeemer", "Brasil", "arquitectonica")
grafo.add_wonder("Machu Picchu", "Perú", "arquitectonica")
grafo.add_wonder("Colosseum", "Italia", "arquitectonica")
grafo.add_wonder("Taj Mahal", "India", "arquitectonica")
grafo.add_wonder("Petra", "Jordania", "arquitectonica")
grafo.add_wonder("Great Wall", "China", "arquitectonica")

#Maravillas naturales
grafo.add_wonder("Grand Canyon", "Estados Unidos", "natural")
grafo.add_wonder("Great Barrier Reef", "Australia", "natural")
grafo.add_wonder("Mount Everest", "Nepal", "natural")
grafo.add_wonder("Aurora Boreal", ["Noruega", "Suecia", "Finlandia", "Canadá", "Islandia", "Rusia"], "natural")
grafo.add_wonder("Amazon Rainforest", ["Brasil", "Perú", "Colombia", "Venezuela", "Ecuador", "Bolivia", "Guyana", "Surinam"], "natural")
grafo.add_wonder("Iguazú Falls", ["Brasil","Argentina","Paraguay"], "natural")
grafo.add_wonder("Salar de Uyuni", "Bolivia", "natural")

#Distancias de las maravillas arquitectonicas

grafo.add_distance('Chichén Itzá', 'Christ the Redeemer', 5900)
grafo.add_distance('Chichén Itzá', 'Machu Picchu', 2500)
grafo.add_distance('Chichén Itzá', 'Colosseum', 12000)
grafo.add_distance('Chichén Itzá', 'Taj Mahal', 15000)
grafo.add_distance('Chichén Itzá', 'Petra', 18000)
grafo.add_distance('Chichén Itzá', 'Great Wall', 21000)
grafo.add_distance('Christ the Redeemer', 'Machu Picchu', 5000)
grafo.add_distance('Christ the Redeemer', 'Colosseum', 9000)
grafo.add_distance('Christ the Redeemer', 'Taj Mahal', 13000)
grafo.add_distance('Christ the Redeemer', 'Petra', 17000)
grafo.add_distance('Christ the Redeemer', 'Great Wall', 20000)
grafo.add_distance('Machu Picchu', 'Colosseum', 8000)
grafo.add_distance('Machu Picchu', 'Taj Mahal', 11000)
grafo.add_distance('Machu Picchu', 'Petra', 16000)
grafo.add_distance('Machu Picchu', 'Great Wall', 19000)
grafo.add_distance('Colosseum', 'Taj Mahal', 9500)
grafo.add_distance('Colosseum', 'Petra', 13000)
grafo.add_distance('Colosseum', 'Great Wall', 18000)
grafo.add_distance('Taj Mahal', 'Petra', 12000)
grafo.add_distance('Taj Mahal', 'Great Wall', 17000)
grafo.add_distance('Petra', 'Great Wall', 22000)

#Distancias de las maravillas naturales

grafo.add_distance("Grand Canyon", "Great Barrier Reef", 13000)
grafo.add_distance("Grand Canyon", "Mount Everest", 14000)
grafo.add_distance("Grand Canyon", "Aurora Boreal", 3000)
grafo.add_distance("Grand Canyon", "Amazon Rainforest", 5000)
grafo.add_distance("Grand Canyon", "Victoria Falls", 8000)
grafo.add_distance("Grand Canyon", "Salar de Uyuni", 11000)
grafo.add_distance("Great Barrier Reef", "Mount Everest", 16000)
grafo.add_distance("Great Barrier Reef", "Aurora Boreal", 8000)
grafo.add_distance("Great Barrier Reef", "Amazon Rainforest", 7000)
grafo.add_distance("Great Barrier Reef", "Victoria Falls", 18000)
grafo.add_distance("Great Barrier Reef", "Salar de Uyuni", 14000)
grafo.add_distance("Mount Everest", "Aurora Boreal", 14000)
grafo.add_distance("Mount Everest", "Amazon Rainforest", 19000)
grafo.add_distance("Mount Everest", "Victoria Falls", 22000)
grafo.add_distance("Mount Everest", "Salar de Uyuni", 20000)
grafo.add_distance("Aurora Boreal", "Amazon Rainforest", 3000)
grafo.add_distance("Aurora Boreal", "Victoria Falls", 12000)
grafo.add_distance("Aurora Boreal", "Salar de Uyuni", 15000)
grafo.add_distance("Amazon Rainforest", "Victoria Falls", 17000)
grafo.add_distance("Amazon Rainforest", "Salar de Uyuni", 20000)
grafo.add_distance("Victoria Falls", "Salar de Uyuni", 25000)

arbol_expansion_arquitectonicas= grafo.kruskal("arquitectonica")
arbol_expansion_naturales= grafo.kruskal("natural")


print(grafo.show_grafo)

print("---Arbol de expansión minimo de las maravillas arquitectonicas")
print(arbol_expansion_arquitectonicas)
print("---Arbol de expansión minimo de las maravillas naturales")
print(arbol_expansion_naturales)

ambas_maravillas,mas_de_una_maravilla= grafo.country_wonders()


print("---Los paises con ambos tipos de maravillas son:")
for pais in ambas_maravillas:
    print(f"-{pais}")
    
print("---Los paises con mas de una maravilla del mismo tipo son:")
for pais in mas_de_una_maravilla:
    print(f"-{pais}")