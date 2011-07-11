import math

def eh_primo(numero):
	lista = []

	for verificador in range(1, int(math.sqrt(numero)+1)):
		if numero % verificador == 0:
			lista.append(verificador)
	return len(lista)<=1

def soma_dos_primos_ateh(maximo):
	numero = 2
	lista = []
	soma = 0

	for numero in range(2,maximo+1):
		if eh_primo(numero):
			lista.append(numero)
			soma += numero
			print numero
		numero += 1
	return soma

if __name__ == "__main__":
	print soma_dos_primos_ateh(2000000)