"""
Recebendo dados de usuários

imput() -> Todo dado recebido via input é do tipo string

Ex: Em python, string é tudo que estiver entre:

- Aspas simples:
- Aspas duplas
- Aspas triplas:
- Aspas duplas triplas:

 Exemplos:

- Aspas simples -> 'Lucas Dias'
- Aspas duplas -> "Lucas Dias"
- Aspas triplas -> '''Lucas Dias'''
"""
# - Apsas duplas triplas -> """Lucas Dias """

# Entrada de dados
# print("Qual o seu nome?")
# nome = input() # Input -> entrada de dados

nome = input("Qual é o seu nome?")
# Exemplo de print 'antigo' 2.x:
# print("Seja bem-vindo %s" % nome)

# Exemplo de print 'moderno' 3.x:
# print("Seja bem-vindo {0}".format(nome))

# Exemplo de print 'atual' 3.7:
print(f"Seja bem-vindo {nome}")

# print("Qual a sua idade?")
# idade = input()
idade = int(input("Qual a sua idade?"))

# Processamento

# Saida

# Exemplo de print 'antigo' 2.x:
# print("Você s% em s% anos" % (nome,idade))

# Exemplo de print 'moderno' 3.x:
# print("Você, {0} tem {1} anos".format(nome,idade))

# Exemplo de print 'atual' 3.7:
print(f"Você {nome} tem {idade} anos")

"""
# int(idade) -> cast
Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f"Você {nome} nasceu em {2021 - idade}")

