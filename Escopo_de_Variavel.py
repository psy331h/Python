"""
Escopo de Variável

Dois tipos de escopo:

1-> Variáveis globais;
    Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2-> Variáveis locais;
    Variáveis locais são reconhecidas apenas no bloco onde foram declaradas,ou seja, seu escopo está limitado ao bloco
    onde foi declarada.

Para declararmos uma variável em python fazemos:

    nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de
dado dela. Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
 int numero = 42

Exemplo em Java:
 int numero = 42

"""

numero = 42  # Exemplo de Variavel global
print(numero)
print(type(numero))

numero = "Lucas Dias"
print("numero")
print(type(numero))

existo = "Oi"
print(existo)
print(type(existo))

numero = 2
novo = 3

if numero > 10:
    novo = numero + 10  # A variavel "novo" está declarada localmente dentro do bloco do if. Portanto, é local.
    print(novo)

print(novo)

