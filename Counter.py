"""
Módulos Collections - Counter (contador)

Counter -> Recebe um iteravel como pâmentro e cria um objeto do tipo Collections Counter que é 
parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor
a quantidade de ocorrências desse elemento.


# Exemplo 1

# Realizando o import
from collections import Counter

# Podemos utilizar qualquer iteravel, aqui utilizamos um lista

lista = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 66, 66, 66, 66, 77, 77, 77, 5, 5, 5, 5]

# Utilizando o Counter

res = Counter(lista)

print(type(res))
print(res)


# Forma 2

print(Counter('Lucas Custodio Dias'))

"""

from collections import Counter

# Forma 3

texto = """Big Data é o termo em Tecnologia da Informação (TI) que trata sobre grandes conjuntos
 de dados que precisam ser processados e armazenados, o conceito do Big Data se iniciou com 3 Vs 
 : Velocidade, Volume e Variedade.

Hoje, todas as pessoas que converso e que sabem que atuamos com Business Intelligence na Cetax Consultoria,
 me perguntam: E esse Big Data, hein, Marco? Eu vi até na Veja… Está todo mundo falando disso! ou “Vi que o
  Cientista de Dados é a profissão do futuro”, “Eu quero ser Cientista de Dados”.

Existem perfis diferentes de trabalho em big data ( vamos falar isso mais para o final do artigo ), 
mas encontramos : Engenheiros de Dados, Cientistas de Dados, Administradores de Big Data, etc."""

res = texto.split()

#print(res)

palavras = Counter(res)

print(palavras)

# Encontrando as 5 palavras com mais ocorrência no texto

print(palavras.most_common(5))






