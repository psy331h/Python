"""
Dicionarios

OBS: Em algumas linguagens de programação os dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários:
    -Chave e valor são separados por dois pontos 'Chave': 'Valor'
    -Tanto chave quanto valor podem ser de qualquer tipo de dado
    -Podemos misturar os tipos de dados


# Criação de dicionários

# Forma 1 (Mais comum)

paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")

print(paises)
print(type(paises))


# Acessando Elementos

# Forma 1 - Acessando via chave da mesma forma que lista/tuplas

print(paises["br"])
print(paises["py"])

# Forma 2 - Acessando via get - Recomendado

print(paises.get("br"))
print(paises.get("ru"))

# Podemos verificar se determinada chave se encontra em um dicionário

print("br" in paises)
print("ru" in paises)
print("Estados Unidos" in paises)

if "ru" in paises:
    Russia = paises["ru"]

# Tuplas como por exemplo são bastante interessantes de se uasar com chave de dicionários, 
# é imutável

# Podemos usuar qualquer tipo de dado como chave de um dicionário

localidades = {
    (40.4233, 25.2546): "Escritório em Tókio",
    (38.4783, 25.5883): "Escritório em Rio", 
    (35.4876, 25.4524): "Escritório em Brasília" 
}

print(localidades)
print(type(localidades))

-------------------------------------------------------------------------------
# Adicionar elementos em um dicionário

receita = {"jan": 100, "fev": 300, "mar": 450}
print(receita)
print(type(receita))

# Forma 1 -- Mais comum 
receita["abr"] = 900
prreceita.update(novo_dado) # recita.update({"mai": 600})
print(receita)

# Podemos atualizar dados em um dicionário

# Forma 1
receita["mai"] = 606
print(receita)

# Forma 2
receita.update({"mai": 610})
print(receita)

# Conclusão 1: A forma de adicionar e atualizar elementos em um dicionário é a mesma
# Conclusão 2: Em dicionários, NÂO podemos ter chaves repetidas 
int(receita)

# Forma 2
novo_dado = {"mai": 600}

---------------------------------------------------------------------------------

# Remover dados de um dicionário

receita = {"jan": 100, "fev": 300, "mar": 450}

# Forma 1
receita.pop("mar")
print(receita)

# Forma 2
del receita["fev"]
print(receita)
"""

# Imagine que voce tem um comercio eletrônico, onde temos um carrinho de compras que adicionamos produtos.

"""
Carrinho de compras:
    Produto 1:
        - nome:
        - quantidade:
        - preço:
    Produto2:
        - nome:
        - quantidade:
        - preço:


# 1 Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ["Fone", 1, 20.00]
produto2 = ["celular", 1, 3500.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.
#----------------------------------------------------------------------------

# 2 Poderiamos utilizar tuplas para isso? Sim

produto1 = ("Fone", 1, 20.00)
produto2 = ("celular", 1, 3500.00)

carrinho = (produto1, produto2)
print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.
#------------------------------------------------------------------------------

# Poderiamos utilizar um dicionário? Sim

carrinho = []
produto1 = {'nome': 'fone', 'quantidade': 1, 'preço': 20.00}
produto2 = {'nome': 'celular', 'quantidade': 1, 'preço': 3500.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.




# Metodos de dicionários 

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(type(d))


# Limpar o dicionário (zerar dados)

d.clear()
print(d)


# Copiando um dicionário para outro

# Forma 1
novo = d.copy() # Deep Copy

novo['d'] = 4

print(novo)

# Forma 2 # Shallow Copy

novo = d
novo['d'] = 4
print(d)
print(novo)

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'idade', 'pontos'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele irá gerar para cada valor do iterável uma chave e irá atribuir a esta chave ao valor informado.


