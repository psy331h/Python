"""
Entendendo o *args

- O *argas é um parâmetro com outro qualquer. Isso significa que você 
pode chamar de qualaquer coisa, desde que começe com *

Exemplo

*xis

Mas por converção, utilizamos *args para defini-lo

Mas o que é *args?

Os Parãmetros *args utilizados em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplassão imutáveis



Exemplos

def soma(nu1, nu2, nu3):
    return nu1 + nu2 + nu3

print(soma(2, 5 ,3))



# Entendendo *args

def soma(*args):
    return sum(args)

print(soma())
print(soma(1, 5))
print(soma(5, 6, 8))
print(soma(5, 7, 9, 65))


# Outro exempplo de utilização do *args

def verifica_info(*args):
    if 'Lucas' in args and 'Dias' in args:
        return 'Bem-vindo Lucas!'
    return 'Não tenho certeza de quem você é ...'

print(verifica_info())
print(verifica_info(1, 3, True, 'Lucas'))
print(verifica_info(True, 5, 'Dias', 9, 'Lucas'))
"""


def soma(*args):
    return(sum(args))


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(soma(*numeros))



# OBS: O asteristico serve para que informemos ao Python que estamos 
# passando como argumento uma coleção de dados. Dessa forma ele saberá que 
# antes precisará desempacotar os dados