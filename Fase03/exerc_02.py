""" 
Olá, este é o um exercício da fase 03. 

Crie as funções a seguir:
    - Crie uma função que recebe uma lista de idades e retorna, numa tupla, somente a maior idade.
    - Crie uma função que recebe uma lista de idades e retorna um dicionário com as chaves "MAIOR_IDADE" E "MENOR_IDADE".
    - Crie uma função que recebe uma lista de idades e retorna uma tupla com as idade ordenadas de maneira crescente.
"""

def maior_idade_lista(idades):
    idades = sorted(idades)
    return (idades[-1], )

def maior_menor_idades_dicionario(idades):
    idades = sorted(idades)
    return {'MAIOR_IDADE': idades[-1], 'MENOR_IDADE': idades[0]}
    
def idades_tupla(idades):
    return tuple(sorted(idades))


idades = [1,10,100,17,7,14,2,5,21,19,22,32,13,42,73,80,96,56,87,99]

print(f'Maior idade: {maior_idade_lista(idades)} Tipo: {type(maior_idade_lista(idades))}\n')
print(f'{maior_menor_idades_dicionario(idades)} Tipo: {type(maior_menor_idades_dicionario(idades))}\n')
print(f'{idades_tupla(idades)} Tipo: {type(idades_tupla(idades))}\n')
