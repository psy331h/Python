""""
Funções com Retorno

OBS: Em Python, quando um função não retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valor, devem retornar esse valor com a palavra return



def quadrado_7():
    print(7**2)

# chamando execução

quadrado_7()

# Função sem retorno (None)

ret = quadrado_7()

print(f'retorno {ret}')



# Refaturando o código com return

def quadrado_7():
    return(7**2)

# chamando execução

quadrado_7()

# Função com retorno 

ret = quadrado_7()

print(f'retorno {ret}')


# Refaturando primeira função

def diz_oi():
    return 'Oi'

Alguem = 'Lucas'

print(diz_oi() , Alguem)


OBS: Sobre a palavra reservada return

1- Ela finaliza a função, ou seja, ela sai da execução da função  
2- Podemos ter, em uma função, diferentes return
3- Podemos em uma função retornar qualquer tipo de dado até mesmo  múltiplos valores 


# Exemplo 1

def diz_oi():
    print('estou sendo executado antes do retorno')
    return 'oi'
    print('estou sendo executado após o retorno')

print(diz_oi())



# Exemplo 2

def nova_função():
    variavel = input('qual a variável:')
    if variavel:
        return 'True'
    elif variavel is None:
        return '3.65'
    return 'b'

print(nova_função())




# Exemplo 3

def outra_função():
    return 2, 3, 4, 5

print(outra_função())
print(type(outra_função()))

"""

# Vamos criar uma função para jogar moeda

from random import random

def jogar():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print('Moeda deu:', jogar())
