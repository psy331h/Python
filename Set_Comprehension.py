"""
Set Comprehension

"""

# Exemplos 

numeros = {num for num in range(1,7)}
print(numeros)

# Exemplo 2 

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Exemplo 3

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Exemplo 4

letras = {letra for letra in 'Lucas Dias'}
print(letras)