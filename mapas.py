"""
Mapas -> conhecidos em Python por dicionários 
Dicionários em Python são representados por chaves



# Iterando sobre Dicionário



for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} receibi {receita[chave]}')

# acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])


# Acessando valores

print(receita.values())

for valor in receita.values():
    print(valor)


# Desempacotamento de chaves

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e valor = {valor}')

"""

receita = {'jan': 500, 'fev': 650, 'mar': 943}
print(receita)

# Soma, valor Maximo, valor Minimo e Tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

