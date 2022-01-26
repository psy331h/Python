"""
Conjuntos 

- Conjuntos em qualquer linguagem de programação, estamos fazem referência à Teoria dos Conjuntos 
da matemática.

- Aqui no Python os conjuntos são chamados de Sets

Dito isto, da mesma forma que na matemática

- Sets (Conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessiveis via índice, ou seja, elementos não são indexados 

Conjuntos são bons para se utilizar quando precisamos armazenar elememtos, mas não nos importamos com a 
ordenação deles. Quando não precisamos se importar com chaves, valores e itens duplicados.

Os conjuntos Sets são referenciados em Python com chaves {}

Diferença entre conjuntos(Sets) e mapas(Dicionários) em Python


- Um Dicionário tem chave/valor
- Conjunto tem apenas valor  


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 1, 3, 2}) # Repare que temos valores repetidos 

print(s)
print(type(s))

# OBS: Ao criar um conjunto caso seja adicionado um valor já existente, o mesmo 
# será ignorado sem gerar erro e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))


# Pdemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


    # Importante lembrar que  além de não temos valores duplicados também não tem ordem

lista = [99, 23, 2, 4, 5, 12, 99, 5, 12]
print(f'lista: {lista} com {len(lista)} de elementos')

tupla = (99, 23, 2, 4, 5, 12, 99, 5, 12)
print(f'tupla: {tupla} com {len(tupla)} de elementos')

dicionário = {}.fromkeys([99, 23, 2, 4, 5, 12, 99, 5, 12] , 'dict')
print(f'Dicionário: {dicionário} com {len(dicionário)} de elementos')

conjunto = {99, 23, 2, 4, 5, 12, 99, 5, 12}
print(f'Conjuntos: {conjunto} com {len(conjunto)} de elementos')


# Podemos colocar qualquer tipo de dado no conjunto 

s = {2, 4.4, 9, False, 'a'}
print(s)
print(type(s))

# Iterando sobre Set(conjunto)

for valor in s:
    print(valor)



# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes de uma feira ou museu
# e os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, já que uma lista pode adicionar novos elementos
# # e permite repetições.


cidades = ['Itaboraí', 'Niterói', 'Maricá', 'Niterói', 'São Gonçalo', 'Maricá', 'Casemiro', 'São Pedro']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades destintas temos.

# Podemos utilizar o Set para isso:

print(len(set(cidades)))


# Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
print(s)




# Remover elementos em um conjunto


# Forma 1
s = {1, 2, 3}
print(s)

s.remove(3)
print(s)


# Forma 2
s.discard(2)
print(s)


# Copiando um conjunto para outro  

# Forma 1 - Deep Copy

novo = s.copy()
novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy
print(s)
novo = s

novo.add(4)
print(novo)
print(s)

# Podemos remover todos os elementos de um conjunto
s.clear()
print(s)



# Juntar um conjunto com o outro 

# Imagine que existem dois conjuntos de alunos matriculados em dois cursos diferentes

# Forma 1

curso1 = {'Lucas', 'Caio', 'Marcela', 'Pedro'}
curso2 = {'Luan', 'Matheus', 'Mara', 'Lucas', 'Marcela'}

total = curso1.union(curso2)

print(total)

# Forma 2 # Utilizando o caractere  pipe |

total2 = curso1 | curso2
print(total2)



# Gerar um conjunto quem o estudantes estão em ambos os cursos

# Forma 1 - Utilizando o intersection

ambos = curso1.intersection(curso2)
print(ambos)

# Forma 2 - Utilizando o &

ambos2 = curso1 & curso2
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro curso

so_curso1 = curso1.difference(curso2)

so_curso2 = curso2.difference(curso1)

print(so_curso1)
print(so_curso2)
"""


# Soma, Máximo, Minimo, Total

s = {1, 2, 3, 4, 5, 6, 7}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

