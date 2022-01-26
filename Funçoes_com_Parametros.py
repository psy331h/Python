"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos 

Entrada -> Processamento -> Saída

Se a gente pensar em um função, sabemos que temos funções que:

Não possuem entrada
Não possuem saida
Possuem entrada, mas não possuem saida 
não possuem entrada, mas possuem saida
Possuem entrada e saida


# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(9))
print(quadrado(5))

ret = quadrado(6)

print(ret)

print(quadrado()) # TypeErro por não indicar o valor 



# Refatorando a função

def canta_parabens(aneversariante):
    print('Parabens pra você')
    print('Nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'Viva o {aneversariante}')

canta_parabens('Lucas')





# Funções podem ter n paraâmetros de entrada. Ou seja, podem receber como entrada
# em um fução quantos parâmetros forem necessários. Eles são separados por virgula 


# Exemplos

def soma(a, b):
    return a + b

def multiplicar(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 3))

print(multiplicar(6, 6))

print(outra(3, 6, ' Python'))




# Nomeando parâmetros 

def nome_completo(nome, sobrenome):
    return f'seu nome é {nome} {sobrenome}'

print(nome_completo('Lucas', 'Dias'))

# A diferença entre Parâmetro e Argumento

# Parâmetros são variaveis declaradas na definição da função
# Argumentos são dados passados durante a execução da função

# A ordem dos parâmetros importa!!

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parãmetros nos argumentos para informá-los,
# Podemos utilizar qualquer ordem 

print(nome_completo(sobrenome= 'Dias', nome= 'Lucas'))
"""

