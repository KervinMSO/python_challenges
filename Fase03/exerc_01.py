"""
Olá, este é o um exercício da fase 03. 

Exercícios: 
1-Crie uma função que:
    Cria e imprime um dicionário através de seus parâmetros nomeados.
    Cria e imprime uma tupla com os parâmetros não nomeados
2- Crie uma função que:
    Receba 2 parâmetros: 'nome_pessoa_a' e 'nome_pessoa_b' e da maneira 
    mais rápida possível, mostre a intersecção de caracteres dos 2 conjuntos

"""

def funcao_1(paramentro_1, paramentro_2, paramentro_3, paramentro_4, paramentro_5):
    dicionario = dict(a=paramentro_1, b=paramentro_2, c=paramentro_3, d=paramentro_4, e=paramentro_5)
    print('Os paramentros recebidos de forma nomeados foram: ')
    print(f'\t{dicionario}, do Tipo: {type(dicionario)}\n')


def funcao_2(paramentro_1, paramentro_2, paramentro_3, paramentro_4, paramentro_5):
    tupla = (paramentro_1, paramentro_2, paramentro_3, paramentro_4, paramentro_5)
    print('Os paramentros recebidos de forma não nomeados foram: ')
    print(f'\t{tupla}, do Tipo: {type(tupla)}\n')


def intersecção(nome_1, nome_2):
    nome_1_set = set(nome_1)
    nome_2_set = set(nome_2)
    nome_intersecção = nome_1_set.intersection(nome_2_set)
    print(f'A intersecção de caracteres dos 2 conjuntos são: {nome_intersecção}\n')


funcao_1(paramentro_1=1, paramentro_2=2, paramentro_3=3, paramentro_4=4, paramentro_5=5)

funcao_2(1,2,3,4,5)

intersecção('nome_pessoa_a', 'nome_pessoa_b')
