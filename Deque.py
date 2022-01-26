"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance
"""

# Fazendo import

from collections import deque

deq = deque('Lucas')

# Adicionando elementos no Deque

deq.append('d') # adicionando no final
print(deq)

deq.appendleft('d') # adicionando no começo
print(deq)

# Removendo elementos

print(deq.pop()) # remove o ultimo elemento e o retorna
print(deq)

print(deq.popleft()) # remove o primeiro elemento e o retorna 
print(deq)