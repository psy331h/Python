"""
Reduce

OBS: A partir do Python 3 a função reduce() não é mais uma função integrada (built-in). Agora temos 
que importar e utilizar essa função a partir do modulo 'functools'

Guido Van Rossum: Utilize a função reduce() se realmente precisar dela. Em todo caso, 
99% das vezes um loop for é mais legível.

para entender o reduce()

# Imagine que você tem uma coleção de dados.

dados = [a1, a2, a3, ... an]

e você tem uma função que recebe dois paramentros:

def funcao(x,y):
    return x * y



Assim como as funções map() e filter(), a reduce() recebe dois parametros a função e o iteravel 

reduce(funcao, dados)

# A função reduce() funciona da seguinte forma:

    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elemnetos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1
    mais o terceiro elemento e guarda o resultado 

    Isso é repetido até o final 





"""

from functools import reduce

dados = [22, 45, 98, 66, 1, 21, 34, 36, 71, 2,]

mult = lambda x, y: x * y

res = reduce(mult, dados)

print(res)

# utilizando lopp normal 

res = 1
for n in dados:
    res = res * n

print(res)