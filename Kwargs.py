"""
**Kwargs

Poderiamos chamar esse parâmetro de xis, mas por convenção chamamos de **Kwargs

Este é só mais um parâmetro, mas diferente do args que coloca os valores
extras em uma tupla. O **kwargs exige que utilizemos parâmetros nomeados, e transforma 
esses parâmetros extras em dicionários 



# Exemplos 

def cores_favoritas(**kwargs):
    for pessoa, cores in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cores} ')


cores_favoritas(lucas= 'Preto', marcos= 'Azul', luane= 'Vermelho')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()

cores_favoritas(mateus= 'Verde')




def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['Geek'] == 'Python':
        return 'Você recebeu um cumprimetos pythônico!'
    elif 'Geek' in kwargs:
        return f"{kwargs['Geek']} 'Geek!"
    return 'Não tem certeza de quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(Geek= 'Python'))
print(cumprimento_especial(Geek = 'Oi'))
print(cumprimento_especial(Geek= 'especial'))



# Nas nossas funções, podemos ter (nessa ordem):

- Parâmetros obrigatórios
- *args
- Parâmetros default (não obrigatórios)
- **kwargs




def minha_função(nome, idade, *args, solteiro= False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_função('Lucas', 21)
minha_função('Matheus', 14, 5, 4, 6, solteiro= True)
minha_função('Luan', 22, 3, 4, 5, solteiro=False)
minha_função('Carla', 9, 3, eu= 'Não', Java= True, Python= False)





# Entendendo o por quê é importante manter a ordem dos parâmetros na declaração 

# Odem correta 
#def mostra(a, b, *args, instrutor= 'Geek', **kwargs):
    #return [a, b, args, instrutor, kwargs]

# Ordem errada
def mostra(a, b, instrutor= 'Geek',*args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra(1, 2, 3, sobrenome= 'Dias', cargo= "instrutor"))



"""


# Desempacotar com **kwargs

def mostra_nome(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {'nome': 'Lucas', 'sobrenome': 'Dias' }

print(mostra_nome(**nomes))
