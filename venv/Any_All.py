"""
Any e All


All -> Retorna TRUE se todos os elementos do iteravel for verdadeiros ou ainda se o itaravel estiver vazio.



"""


# Exemplo All()

#print(all([0, 1, 2, 3, 4])) #todos os numeros são verdadeiros? Não, então retornará FALSE 

# List Comprehension


nomes = ['Lucas', 'Luan', 'Larissa', 'Lorenzo']

print(all([nome[0] == 'L' for nome in nomes])) # Retorna TRUE