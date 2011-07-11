def soma_fibonacci(maximo):
	soma = 0
	primeiro = 1
	segundo = 1

	while segundo < maximo:
		if segundo % 2 == 0:
			soma = soma + segundo
		primeiro, segundo = segundo, primeiro+segundo
	return soma

def fibonacci_abaixo_de(maximo):
	primeiro = 1
	segundo = 1
	fibonacci = []
	while segundo < maximo:
		fibonacci.append(segundo)
		primeiro, segundo = segundo, primeiro+segundo
	return fibonacci

	
if __name__== "__main__" :
	print soma_fibonacci(4000000) 