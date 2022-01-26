import datetime

# Ano atual 

ano = datetime.date.today().year

# Nome 

nome = input('Qual o seu nome?').title()

print(f'Olá {nome}!')

print(f'{nome} esse é um software que calcula seu tempo para o alistamento militar.')


idade = int(input('Em que ano você nasceu?'))

idade = ano - idade

if idade > 18:
    print(f'{nome}, vc deve procurar uma junta mais proxima da sua casa o mais rapido possível para o processo de alistamento militar')

elif idade < 18:
    print(f'{nome}, falatam ainda mais {idade - 18} anos para seu alistamento.')

else:
    print(f'{nome}, procure uma junta mais proxima da sua casa.')