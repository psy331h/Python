"""
Tuplas (tuples)

Tuplas são bastantes parecidas com lista.

Basicamente existem duas diferenças:

1-> As tuplas são representadas por parênteses ()
2-> As tuplas são imutaveis: Isso signifíca que ao criar uma trupla não é não se pode alterar mais.
Toda operação em uma tupla gera uma nova tuple


# CUIDADO 1. As tuplas são representadas por parênteses, mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2. Tuplas com um elemento:

tupla3 = 4
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

# CONCLUSÂO: Podemos concluir que tuplas são definidas pelo uso da virgula e não do parêntese

# Podemos gerar uma tupla dinâmicamente com o range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desenpacotamento de tuplas
tupla = ("Lucas", "Dias")
nome, sobrenome = tupla

print(nome)
print(sobrenome)

# Soma, valor máximo, valor minimo e tamanho
# Se todos os elementos forem int

tupla1 = (1, 2, 3, 4, 5, 6)
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))


# Concatenação de de tuplas
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)

print(tupla2 + tupla1)  # São imutáveis

# As tuplas não se alteraram
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Podemos sobrescrever  seus valores
print(tupla1)


# Podemos verificar se determinado valor está na tupla
tupla1 = (1, 2, 3)
print(3 in tupla1)

# Iterando sobre tuplas

tupla1 = (1, 2, 3)
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)


# Contando elementos dentro de uma tupla
tupla = ("a", "b", "c", "d", "e", "a", "b")
print(tupla.count("a"))

nome = "lucas Dias"
print(tuple(nome))
print(nome.count("a"))

# O acesso a elementos de uma trupla é semelhante a de uma lista
print(meses[5])

# Iterando com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1


"""
# Dica de utilização dde tuplas
# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos na coleção

# Exemplo1:

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# Verificando em qual indice o elemento está na tupla
print(meses.index("Junho"))
