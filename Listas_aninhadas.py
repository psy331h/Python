"""
- Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (Java/C) possuem uma estrutura chamada de arrays:
    - Umidimesionais (Arrays/Vetores):
    - Multidimensionais (Matrizes)


- Em Python nós temos as listas 

list = [1, True, 2.45, 'b']





# Exemplos

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(lista)
print(type(lista))



# Como fazemos para acessar os dados?

print(lista [0] [1]) # Colocamos linhas e depois coluna, aqui estamos acessando o número 2




# Iterando com loops em uma lista

for list in lista:
    for num in list:
        print(num)


# List Comprehension

[[print(valor) for valor in li] for li in lista] 


"""

# Outros exemplos 

# Gerando um tabuleiro/matriz 3x3

tab = [[num for num in range(1, 4)] for lin in range(1, 4)]
print(tab)

# Gerando jogadas para jogo da velha 

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)