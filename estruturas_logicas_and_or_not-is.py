"""
Estruturas Logicas: and (e), is (é), not (não), or (ou)

Operadores unários:
   - not
Operadore binários:
   - and, is , or

Para o "and", ambos os valores precisam ser True
Para o "or", um ou outro valor precisa ser True
Para o "is", o valor é comparado ao segundo
Para o "not" o valor do booleano é invertido ,ou seja, se for True vira False, se for False vira True
"""
Ativo = True
logado = False

if Ativo:
    print("Bem vindo usuário!")
else:
    print(" Você precisa ativar sua conta. Por favor, verifique seu e-mail.")
