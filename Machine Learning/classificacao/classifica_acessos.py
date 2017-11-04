from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X, Y = carregar_acessos()

#primeiras 90 linhas
treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

#minha abordagem inicial foi
#1. Separar 90% oara treino e 10% para teste: 88.89$

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes) #treina de acordo com os seus dados

resultado = modelo.predict(teste_dados) #resultado do seu teste
diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d == 0] #acertos soma so quando nao teve diferenca com Y
total_de_acertos = len(acertos) #quantidade de Linhas que eu acertei
total_de_elementos = len(teste_dados) #quantidade de Linhas que eu treinei
taxa_de_acerto = 100.0 * total_de_acertos/total_de_elementos #taxa de acerto no final

print(taxa_de_acerto)
print(total_de_elementos)