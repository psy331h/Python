print("Seja bem-vindo!")
usu = input("Digite um nome de usuário:")
print(f"Muito bem {usu}")
idade = int(input(print(f"{usu}, em que ano você nasceu:")))
idade = idade - 2021
if idade > 18:
    print("Usuário aceito!")
elif idade == 18:
    print("Usuário aceito! ")
else:
    print(f"{usu}, nosso conteudos não saõ recomendados para menores de 18 anos ")
    term = ""
    while term != "sim":
        term = input(" voce concorda")