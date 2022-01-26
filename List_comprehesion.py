"""
List Comprehesion

- Utlizando list comprehesion nós podemos gerar novas listas com dados processados a patir
de outro iterável

-Sintaxe da list comprehesion

[dado for dado in iterável]




# Exemplos

lista = [1, 2, 3, 4, 5,]

res = [numero * 10 for numero in lista]
print(res)

# Para entender melhor o que estamos fazendo devemos dividir a expressão em 2 partes:

# A primeria é for numero in lista 
# A segunda é numero * 10



# List comprehesion vesus loop

numeros = [1, 2, 3, 4, 5, 6 ]

numero_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numero_dobrados.append(numero_dobrado)

print(numero_dobrados)


# List Comprehesion
print([numero * 2  for numero in numeros] )


"""


# Outros exemplos


nome = 'João'

print([letra.upper() for letra in nome])

# Exemplo 2

amigos = ['lucas', 'matheus', 'joão', 'andré']

print([amigo.title() for amigo in amigos])

# Exemplo 3

print([numero *3 for numero in range(1, 10)])

# 4

print([str(numero) for numero in [1, 2, 3, 4, 5, 6, 7]])