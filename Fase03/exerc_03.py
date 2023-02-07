""" 
Olá, este é o um exercício da fase 03.

Crie uma função que recebe um dicionário com os nomes dos alunos reprovados e aprovados em cada matéria.
(exemplo de entrada)
{
    "MATEMÁTICA": {"APROVADOS": [A,B,C], "REPROVADOS": [D,E,F,G,H]},
    "FÍSICA": {"APROVADOS": [A,B,C], "REPROVADOS": [D,E,F,G,H]}, 
    ...
}
Após receber a entrada, retorne um dicionário com as chaves "APROVADOS_EM_TODAS" com os alunos numa tupla ordenada 
alfabeticamente, a chave "REPROVADOS" com uma tupla também ordenada alfabeticamente e por fim uma
chave "DETALHES" com um dicionário que mostra os alunos reprovados ordenados pela quantidade de 
matérias reprovadas. 
(exemplo da chave detalhes)
{
    1: {"nome":[ matérias, reprovadas,...]},
    2: {"nome":[ matérias, reprovadas,...]},
    ...
}

"""

def alunos_aprovados_reprovados(materias):
    dicionario = {"APROVADOS_EM_TODAS": (), "REPROVADOS": (), "DETALHES": {}}
    list_aprovados = list()
    list_reprovados = list()
    detalhes = dict()
    detalhes2 = dict()

    for materia, aprovado in materias.items():
        list_aprovados.append(set(aprovado["APROVADOS"]))
        list_reprovados.append(aprovado["REPROVADOS"])

        for det in aprovado["REPROVADOS"]:
            if det not in detalhes:
                detalhes[det] = [materia]
            elif det in detalhes:
                detalhes[det].append(materia)

    for aprov in range(1, len(list_aprovados)):
        list_aprovados[0] = list_aprovados[0].intersection(list_aprovados[aprov])

    for repro in list_reprovados:
        list_reprovados[0].extend(repro)

    for ordem in sorted(detalhes, key= detalhes.get):
        detalhes2[ordem] = detalhes[ordem]

    dicionario['APROVADOS_EM_TODAS'] = tuple(sorted(list_aprovados[0]))
    dicionario['REPROVADOS'] = tuple(sorted(set(list_reprovados[0])))
    dicionario['DETALHES'] = detalhes2

    print(f'{dicionario}\n')

    print(f'Aprovado em Todas: {dicionario["APROVADOS_EM_TODAS"]}\n')
    print(f'Reprovados: {dicionario["REPROVADOS"]}\n')
    print('Detalhes das reprovações: ')
    
    for item in dicionario["DETALHES"].items():
        print(f'\t{item[0]} = {item[1]}')

    
entrada = {
"MATEMÁTICA": {"APROVADOS": ['A','B','C'], "REPROVADOS": ['D','E','F','G','H']},
"FÍSICA": {"APROVADOS": ['A','B','C', 'D'], "REPROVADOS": ['E','F','G','H']}, 
"QUIMICA": {"APROVADOS": ['A','B','C', 'D', 'E'], "REPROVADOS": ['F','G','H']},
"HISTORIA": {"APROVADOS": ['A','B','D', 'H'], "REPROVADOS": ['C', 'E','F','G']}
}

alunos_aprovados_reprovados(entrada)
