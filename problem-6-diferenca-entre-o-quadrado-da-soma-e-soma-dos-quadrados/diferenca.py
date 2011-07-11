# def quadrado_do_numero(numero):
# 	quadrado = numero * numero
# 	return quadrado

def soma_dos_quadrados(maximo):
	soma = 0
	numero = 1
	quadrado = 0
	for numero in range(1,11):
	# while numero <= maximo:
		quadrado = numero ** 2
		soma = soma + quadrado
		# numero = numero + 1
	return soma

def quadrado_da_soma(maximo):
	soma = 0
	numero = 1
	quadrado = 0
	for numero in range(1,11):
		soma = soma + numero
	quadrado = soma * soma
	return quadrado

def diferenca(maximo):
	soma = soma_dos_quadrados(maximo)
	quadrado = quadrado_da_soma(maximo)
	result = quadrado - soma
	return result

if __name__ == "__main__":
	print diferenca(100)