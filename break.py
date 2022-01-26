"""
Saindo de loops com breaks
 funciona da mesma forma da linguagem C e Java

Ultilizamos o break para sair do loop de maneira projetada
"""

# exemplo 1
for numero in range (1,11):
     if numero == 6:
         break
     else:
         print(numero)
print("Sai do loop")

#exemplo

while True:
    comando = input("digite 'sair' para sair ")
    if comando == "sair":
        break