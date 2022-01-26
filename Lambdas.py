"""
Lambdas: Comhecidas como exepressões lambdas ou simplesmente lambdas,
são funções sem nomes, ou seja, dunções anônimas.

# Função em Python

def funcao(x):
    return 3 * x * 2

print(funcao(5))
print(funcao(9))

# Expressão Lambda

lambda x: 3 * x * 2

# Como utilizar a expressão lambda?
calc = lambda x: 3 * x * 2

print(calc(5))
print(calc(9))



# Podemos ter expressões lambdas com mutiplas entradas 

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('   lucas', 'dias   '))


# Em Python podemos ter funções com nenhuma ou varias entradas. Em Lambdas também

amar = lambda: 'Como não amar Python?'
uma = lambda x: 3 * 9 + x
duas = lambda x, y: 3 + x * 2 + y
tres = lambda x, y, z: 6 + y / 0.5 + z

print(amar)
print(uma(2))
print(duas(7, 9))
print(tres(2, 5, 29))

# Outros Exemplos

nomes = ['Lucas Dias', 'Gabriel Custódio', 'Matheus Araujo', 'Luan Gonçalves', 'Alisson Pimentel']

print(nomes)

nomes.sort(key= lambda sobrenome: sobrenome.split(' ') [-1].lower())
print(nomes)


"""
# Função quadratica com Lambda 

def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b + x + c

teste = funcao_quadratica(5, 6, 39)

print(teste(3))
print(teste(63))
