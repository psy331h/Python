"""
Filter() -> Serve para filtrar dados de uma coleção


# Biblioteca para trabalhar com dados estatisticos 

import statistics

# dados coletados de algum sensor 

dados = [1.5, 0.7, 7.7, 3.4, -0.2, 4.9]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f'Média: {media}')

# Assim como map(), a função filter() recebe dois parametros 
# sendo uma função e o outro iterável 

res = filter(lambda x: x > media, dados)
print(list(res))

--------------------------------------------------------------------------------------


# Filtrando uma lista para remover espaços vazios 

paises = ['', 'Argentina', 'Brasil', '', 'Colombia', 'Chile', '', 'Equador', 'China', '', '']

print(paises)

res = filter(None, paises)
print(list(res))

------------------------------------------------------------------------------------------




# Exemplo mais complexo:

usuarios = [
    {'username': 'Lucas', 'tweets': ['Eu adoro Python!', 'Programar é bom!']},
    {'username': 'Matheus', 'tweets': ['Estou pra baixo.', 'É complicado!']},
    {'username': 'Marcos', 'tweets': []},
    {'username': 'Jojo', 'tweets': ['Vou sair hoje!', 'Cinema!!!']},
    {'username': 'Carlos', 'tweets': ['Vida louca!']},
    {'username': 'Paulo', 'tweets': []},
]

# Forma 1
#inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))

print(inativos)
"""

# Combinar map() com filter() 

nomes = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
