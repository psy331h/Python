"""
Map

Com o map, fazemos o mapeamento dos valores para as funçoes 



import math
from typing import List

def area(r):
    # Calcula a area de um circula com o raio 'r' 
    return math.pi * (r ** 2)

print(area(3))
print(area(21))

raios = [12, 5, 23, 5.6, 0.3]

# Forma comum

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2

areas = map(area, raios )

print(areas)
print(type(areas))
print(list(areas))

# Forma 3 map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

"""

# Mais um exemplo 

cidades = [('Los Angeles', 26), ('Tokio', 27), ('Nova York', 30), ('Paris', 25), ('Buenos Ares', 29), 
('Rio de Janeiro', 35)]

# f= 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
