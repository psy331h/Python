"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O bloco while será repetido enquanto a expressão booleana for verdadeira.

exemplo:

num = 5
num < 5

# Exemplo 1
num = 3

while num < 10:
    print(num)
    num = num +1

#OBS: Em um loop while é importante que cuidemos do critério deparada para não causar um loop infinito.
"""
#Exemplo 2
resposta = ""
while resposta != "sim":
    resposta = input("Já acabou Jéssica?")
