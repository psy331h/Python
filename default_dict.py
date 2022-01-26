"""

Módulo Collections - Default Dict

# Recap Dicionários

dicionário = {'nome': 'Lucas Dias'}

print(dicionário)
print(dicionário['nome'])

default dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. esse valor será utilizado sempre que não houver 
um valor definido. caso tentamos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

OBS: Lambda são funções sem nomes, que podem ou não receber parâmetros de entrada
e retornar valores
"""
# Fazendo o import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['nome'] = 'Lucas Dias'

print(dicionario)

print(dicionario['outro'])  # keyErro no dicionário comum, mas aqui não!!

print(dicionario)
