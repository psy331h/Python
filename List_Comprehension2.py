"""
List Comprehension

- Nós podemos adicionar estruturas condicionais logicas à List Comprehension


"""


# Exemplos 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando 


# Qualquer numero par módulo de 2 é 0 e 0 em Python é False. not False = True
pares2 = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1 e 1 em Python é True
impares2 = [numero for numero in numeros if numero % 2]

print(pares2)
print(impares2)


# Exemplo 02

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)