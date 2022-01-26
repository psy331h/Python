"""
listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também podem colocar QUALQUER tipo de dado.

Linguagem C/java;Arrays
    -Possuem tamanho e tipo de dado fix.
    Ou seja, nessas linguagens se você criar um do tipo int e com tamanho 5, esse array
    será SEMPRE do tipo inteiro e poderá SEMPRE ter no máximo 5 valores.

Já em Python:

-Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar uma lista e simplesmente ir adicionando elementos
-Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja podemos colocar qualquer tipo de dado.

As lista em Python são representadas por colcheites: []

type([])
lista1 = [1, 99, 55, 43, 62, 99, 25, 36, 94, 27, 99, 99]
lista2 = ["L", "u", "c", "a", "s", "", "D", "i", "a", "s"]
lista3 = []
lista4 = list(range(11))
lista5 = list("Lucas")




# Podemos facilmente checar se determinado valor está contido na lista.
num = 18
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print(f"Não encontrei {num}")

# Podemos facilmente ordenar um lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(99))
print(lista2.count("s"))

# Adicionar elementos a lista

Para adicionar elementos a lista usamos o append
print(lista1)
lista1.append(44)
print(lista1)
# Com append nós conseguimos adicionar apenas um elemento por vez
# lista1.append(44, 22, 54) # erro

lista1.append([2, 6, 8])
print(lista1)
if [2, 6, 8] in lista1: # Coloca a lista como elemento único (sublista)
    print("Encontrei a lista")
else:
    print("Não encotrei a lista")

lista1.extend([22, 44, 89]) # Coloca cad elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Isso não substitui o valor inicial. O mesmo será desloca do para a direita.
lista1.insert(2, "Novo valor")
print(lista1)

# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
# lista.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
#Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover facilmente o ultimo elemento de uma lista
# O pop não somente remove o ultimo número, mas também o retorna

lista1.pop()
print(lista1)

# Podemos remover um elemento de uma lista pelo índice
# OBS: os elementos da direita desse índice serão deslocados para a esquerda.
# OBS: Se não houver o elemneto no índice informado teremos o erro: IndexError
lista2.pop(4)
print(lista2)

# Podemos remover todos os elementos da lista (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para lista
# OBS: Por padrão o split separa os elementos da lista pelo espaço entre eles

# Exemplo1
curso = "Programação em Python"
print(curso)
curso = curso.split()
print()

# Exemplo2
curso = "Programação,em,Python"
print(curso)
curso = curso.split(",")
print(curso)

# Convertendo lista em string
lista6 = ["Programação", "em", "Python"]
print(lista6)

# Abaixo estamos dizendo: Pega a lista, coloque espaço entre os elementos e transforme em uma string

curso = " ".join(lista6)
print(curso)

# Iterando sobre lista

# Exemplo1
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2

carrinho = []
produto = ""
while produto != "sair":
    print("Adicione um produto no carrinho ou digite: 'sair' para sair:")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Fazemos acesso a elementos de forma indexada
#           0           1           2      3
cores = ["amarelo", "vermelho", "azul", "branco"]
print(cores[0])

# Fazemos acesso a elementos de forma indexada inversa
print(cores[-1])

# Soma, valor máximo, valor minimo e tamanho

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Podemos transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)

# Desenpacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista
print(num3)
print(num2)
print(num1)

# Copiando uma lista para outro (shallow copy e Deep copy)

# forma1
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(nova)

"""
# Forma 2 (Shallow copy)
lista = [1, 2, 3]
print(lista)
nova = lista
print(nova)
nova.append(4)
print(lista)
print(nova)
