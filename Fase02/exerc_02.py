"""
Olá, este é o um exercício da fase 02. 
Exercício:
Faça um canal de consulta por discagem telefônica da seguinte forma:

Imprima na tela: “ Olá, seja bem vindo {nome da pessoa}, digite uma opção “
OP 1 = Consultar saldo
	Resposta: “ Seu saldo é { qtd de letras do nome * 2 }“
OP 2 = Consultar extrato
	Resposta: “Há { qtd de letras do nome * 4 }”
OP 3 = Consultar cartões de crédito
	Resposta: “Não há cartões em nome de {nome da pessoa}”
OP 4 = Informar erro
	Resposta: "Desculpe, nosso sistema de ouvidoria está indisponível “
OP 5 = Falar com atendente 
	Resposta: "Desculpe, não há atendente disponível no momento “
OP 0 = Sair do sistema

Todas as OP , exceto sair, devem retornar ao menu inicial após a resposta.
"""

nome_da_pessoa = input('Qual é o seu nome? ')
opcao = '1'

print(f'Olá, seja bem vindo {nome_da_pessoa.capitalize()}')

while opcao != '0':

	opcao = input('Digite a opção desejada: \n\t 1 = Consultar saldo \n\t 2 = Consultar extrato \n\t 3 = Consultar cartões de crédito \n\t 4 = Informar erro \n\t 5 = Falar com atendente  \n\t 0 = Sair do sistema\n')

	if opcao == '1':
		print(f'Seu saldo é {len(nome_da_pessoa) * 2 }')

	if opcao == '2':
		print(f'Há {len(nome_da_pessoa) * 4 }')

	if opcao == '3':
		print(f'Não há cartões em nome de {nome_da_pessoa}')

	if opcao == '4':
		print('Desculpe, nosso sistema de ouvidoria está indisponível ')

	if opcao == '5':
		print('Desculpe, não há atendente disponível no momento')

	if opcao >= '6':
		print('Desculpe, opção invalida')

print('Obrigado e volte sempre')