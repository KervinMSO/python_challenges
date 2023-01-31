"""
Olá, este é o um exercício da fase 02. 
        Construa o Game Labirinto Eureka!
Descrição do exercício:

O desafiante participará de um Game, O Labirinto Eureka. Ele inicia o game com 5 vidas e deve responder
algumas perguntas. Cada pergunta vale uma quantidade de vidas a ser adicionadas se respondido 
corretamente ou retiradas caso contrário. Ao fim do labirinto ele deve responder a pergunta final que 
decidirá o fim do game.

Na pergunta final caso ele escolha a RedPill um laço de repetição deve retirar 1 vida ,a cada iteração,
para o total de letras de seu nome. Caso ele escolha BluePill um laço de repetição deve retirar 1 vida
por iteração até que seu score seja menor ou igual a zero. 
Escolha o laço adequado para cada situação. 

Se em qualquer momento do jogo o score de vidas estiver menor ou igual a zero, o jogo deve ser finalizado
e uma mensagem de Game Over deve aparecer ao desafiante. 

As 3 primeiras perguntas:

(Valendo 1 vida)
1- A inspiração para o nome da empresa Senfio é a tecnologia Wireless que significa:
    1) Sem Fio
    2) Senfio
    3) Cabos
    4) Nenhuma das alternativas
    
(Valendo 2 vidas)
2- Como vai a matemática? Responda, 77+33 =?
    1) 100
    2) 110
    3) 010
    4) 001

(Valendo 3 vidas)
3-Imagine que seu Pai tem 5 filhos, gaga, gege, gigi, gogo e ?
    1) Gugu Liberato
    2) Pintinho Amarelinho
    3) Gugu
    4) *{nome do desafiante}*

Pergunta final- Muito bem, espero que você tenha acumulado vidas para a pergunta final. 
                Se você deseja sair do labirinto Eureka e descobrir a verdade, qual pílula deve escolher?
    1) RedPill
    2) BluePill


"""

print('Labirinto Eureka!')

nome_do_desafiante = input('Qual é o seu nome? ')

vidas = 5
game_over = 0

while vidas > game_over:

    pergunta_1 = input(' \n(Valendo 1 vida) \n 1- A inspiração para o nome da empresa Senfio é a tecnologia Wireless que significa: \n\t 1) Sem Fio \n\t 2) Senfio \n\t 3) Cabos \n\t 4) Nenhuma das alternativas \n')
    
    if pergunta_1 == '1':
        vidas += 1
        print(f'Resposta Correta, suas vidas totais agora é: {vidas}.')
    else: 
        vidas -= 1
        print(f'Resposta Errada, suas vidas totais agora é: {vidas}.')

    pergunta_2 = input(' \n(Valendo 2 vida) \n 2- Como vai a matemática? Responda, 77+33 =? \n\t 1) 100 \n\t 2) 110 \n\t 3) 010 \n\t 4) 001 \n')

    if pergunta_2 == '2':
        vidas += 2
        print(f'Resposta Correta, suas vidas totais agora é: {vidas}.')
    else:
        vidas -= 2
        print(f'Resposta Errada, suas vidas totais agora é: {vidas}.')

    pergunta_3 = input(f' \n(Valendo 3 vida) \n 3-Imagine que seu Pai tem 5 filhos, gaga, gege, gigi, gogo e ? \n\t 1) Gugu Liberato \n\t 2) Pintinho Amarelinho \n\t 3) Gugu \n\t 4) {nome_do_desafiante.capitalize()} \n')

    if pergunta_3 == '4':
        vidas += 3
        print(f'Resposta Correta, suas vidas totais agora é: {vidas}.')
    else:
        vidas -= 3
        print(f'Resposta Errada, suas vidas totais agora é: {vidas}.')

    if vidas <= game_over:
        break

    while True:
        pergunta_final = input(' \nPergunta final- Muito bem, espero que você tenha acumulado vidas para a pergunta final. \n\t Se você deseja sair do labirinto Eureka e descobrir a verdade, qual pílula deve escolher? \n\t 1) RedPill \n\t 2) BluePill \n')

        if pergunta_final == '1':
            print('Então você escolheu a RedPill, perca 1 vida pra cada letra do seu nome.')
            for element in nome_do_desafiante:
                vidas -=1
            break
        elif pergunta_final == '2':
            print('Você escolheu a BluePill, pessima escolha!')
            while (vidas>0):
                vidas-=1
            break
        else:
            print('Desculpe, opção invalida.')
    break

if vidas > game_over:
    print(f'Parabéns, você finalizou o jogo com o total de {vidas} vidas.')
else:
    print('Game Over')
        