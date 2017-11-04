def processa_convite(nome_convidado):
	posicao_final = len(nome_convidado)
	posicao_inicial = posicao_final - 4
	parte1 = nome_convidado[0:4]
	parte2 = nome_convidado[posicao_inicial: posicao_final]
	nome = parte1 + ' ' + parte2
	return 'Enviando convite para ' + nome