"""
Tipo Float

Tipo real, decimal
Casas decimais
OBS: O separador de casas decimais na programação é o ponto e não virgula.
"""

# Errado do ponto de vista do Float, mas gera uma Tupla
valor = 1, 44
print(valor)
print(type(valor))
# Certo
valore = 1.44
print(valore)
print(type(valore))

# É possivel fazer dupla atribuição
nome, roma = 1, 44
print(nome)
print(type(nome))
print(roma)
print(type(roma))

# Podemos converter um Float para int
"""
OBS: Ao converter um float para int perdemos precisão.
"""
resu = int(valore)
print(type(resu))

# Podemos trabalhar com numeros complexos
variavel = 5j
