""""
Docstrings


OBS: Podemos ter acesso á documentação de uma função utilizando
a propriedade especial __doc__

Podemos ainda fazer acesso à documentação da função com o help()
"""

def diz_oi():
    """ Uma função que retorna 'Oi!' """
    return 'Oi!'

print(diz_oi())

def exponecial(numero, exponen=2):
    """Uma função que retorna a potencia do numero escolhido"""
    return numero ** exponen

print(exponecial(3))