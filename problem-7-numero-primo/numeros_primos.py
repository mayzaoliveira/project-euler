import math

def eh_primo(numero):
	lista = []
	
	for verificador in range(1, int(math.sqrt(numero)+1)):
		if numero % verificador == 0:
			lista.append(verificador)
	return len(lista)<=1

def elemento_primo(maximo):
	numero = 2
	lista = []
	pos = 1
	while len(lista) < maximo:
		if eh_primo(numero):
			print pos
			pos += 1
		 	lista.append(numero)
		numero+=1
	return lista[-1]

if __name__ == "__main__":
	print elemento_primo(10001)