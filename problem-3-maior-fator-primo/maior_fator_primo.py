import math

def eh_primo(numero):
	lista = []

	for verificador in range(1, int(math.sqrt(numero)+1)):
		if numero % verificador == 0:
			lista.append(verificador)
	return len(lista)<=1

def fatores_primos_de(maximo):
	numero = 2
	lista = []
	multiplicacao = 1

	while numero != (multiplicacao == maximo):
		if eh_primo(numero):
			if maximo % numero == 0:
				lista.append(numero)
				multiplicacao = multiplicacao * numero
				print numero
		numero += 1
	return lista[-1]

if __name__ == "__main__":
	print fatores_primos_de(13195)