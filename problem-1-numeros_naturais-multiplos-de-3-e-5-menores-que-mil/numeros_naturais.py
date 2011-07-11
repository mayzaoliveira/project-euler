def verifica_multiplos(numero):
	if (numero % 3 == 0 or numero % 5 == 0):
		return True
	return False
		
def soma_multiplos_abaixo_de(maximo):
	soma = 0
	for numero in range(3,maximo):
		if verifica_multiplos(numero):
			soma = soma + numero
	return soma

if __name__ == "__main__":
	print soma_multiplos_abaixo_de(1000)