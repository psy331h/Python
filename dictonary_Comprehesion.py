"""
Dictionary Comprehesion

Pense no seguinte:

Se quisermos criar uma lista:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um Set:

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

{Chave: Valor for in valor iterável}
[valor for in valor iterável]


# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)


---------------------------------------------------------------------------------------------


lista = [1, 2, 3, 4]

quadrado = {valor: valor ** 2 for valor in lista}

print(quadrado)

----------------------------------------------------------------------------------------------


chave = 'abcde'
valor = [1, 2, 3, 4, 5]

mistrura = {chave[i]: valor[i] ** 2 for i in range(len(chave))}

print(mistrura)

-----------------------------------------------------------------------------------------------
"""


# Exemplo usando lógica condicional

numeros = [1, 2, 3, 4, 5, 6]

res = {chave: ('par' if chave % 2 == 0 else 'impar') for chave in numeros}

print(res)


