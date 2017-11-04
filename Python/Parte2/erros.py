from models import *
arquivo = None
try:	
	arquivo = open('perfis.csv', 'r')
	valores = arquivo.readline().split(',')
	Perfil(*valores)
	print('Arquivo foi aberto')
	arquivo.close()
except (IOError, TypeError) as erro:
	print('Deu erro %s' %erro)

finally:
	if (arquivo is not None):
		print('Fechando arquivo')
		arquivo.close()