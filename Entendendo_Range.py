"""
Ranges
- Precisamos conhecer o loop for para ultilizar os ranges
- Precisamos conhecer o range para trabalhar melhor com o loop for

Ranges são ultilizados para gerar sequências numéricas, não de formar aleatória.
Mas sim de maneira especificada.

Formas gerais:

#Forma 1

 range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1 )

# Exemplo forma 1
for num in range(11):
    print(num)

#Forma 2
 range(valor_de_inicio, valor_de_parada)


 OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1 )
  # Exemplo forma 2
  for num in range(2, 10):
      print(num)

# Forma 3
 OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário )
 # Exemplo 3
 for num in range(1,51,2):
     print(num)

# Forma 4
OBS: valor_de_parada não inclusive (valor_final especificado pelo usuário, e passo especificado pelo usuário )
#Exemplo 4
for num in range(10,0,-1):
    print(num)

"""
