"""
 Módulo Collections - Name tuple 


# Recap tuplas

tupla = (1, 2, 3)

print(tupla[2])


Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Fazendo import

from collections import namedtuple

# Precisamos definir o nome e os parâmetros

# Forma 1 # Declaração Named Tuple

cachorro = namedtuple('cachorro', 'nome idade raça')

# Forma 2 # Declaração Named Tuple

cachorro = namedtuple('cachorro', 'nome, idade, raça')

# Forma 3 # Declaração Named Tuple

cachorro = namedtuple('cachorro', ['nome', 'idade', 'raça'])

ray = cachorro(nome='ray', idade=8, raça='Vira-Lata')


# Acessando dados

# Forma1
print(ray[1]) # idade

# Forma2
print(ray.idade) # idade
print(ray.count('Vira-Lata'))