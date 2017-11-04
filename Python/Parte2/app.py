# -*- coding: UTF-8 -*-

import re

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes: '
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Qual o nome você gostaria de remover?'
	nome = raw_input()
	nomes.remove(nome)

def alterar(nomes):
	print 'Qual nome vc gostaria de alterar?'
	nome = raw_input()
	if nome in nomes:
		index = nomes.index(nome)
		print 'Para qual nome você quer alterar?'
		novo_nome = raw_input()
		nomes[index] = novo_nome
		print 'Nome alterado'
	else:
		print 'Nome não existe'

def procurar(nomes):
	print 'Digite um nome a procurar:'
	nome_a_procurar = raw_input()
	if nome_a_procurar in nomes:
		print 'Nome %s está cadastrado' %(nome_a_procurar)
	else:
		print 'Nome %s não existe na lista' %(nome_a_procurar)

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite 1 para Cadastrar, 2 para Listar, 3 para Remover, 4 para Alterar, 5 para Procurar, 6 para Procurar por Expressão e 0 para Terminar'
		escolha = raw_input()
		
		if (escolha=='1'):
			cadastrar(nomes)

		if (escolha=='2'):
			listar(nomes)

		if (escolha=='3'):
			remover(nomes)

		if (escolha=='4'):
			alterar(nomes)

		if (escolha=='5'):
			procurar(nomes)

		if (escolha=='6'):
			procurar_regex(nomes)

menu()
