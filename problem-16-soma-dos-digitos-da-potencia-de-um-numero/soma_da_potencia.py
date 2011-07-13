def potencia(numero, expoente):
	resultado = numero ** expoente
	return resultado

def soma_da_potencia(numero,expoente):
	soma = 0
	resultado = numero ** expoente
	arm_resultado = str(resultado) 

	for indices in arm_resultado:
		soma += int(indices)
	return soma

if __name__ == "__main__":
	print soma_da_potencia(2,1000)