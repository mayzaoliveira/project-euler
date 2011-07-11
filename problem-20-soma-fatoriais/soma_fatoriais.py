def fatorial(maximo):
	numero = maximo
	fatorial = 1
	while numero != 0:
		fatorial = fatorial * numero
		numero = numero - 1
	return fatorial

def soma_dos_digitos_do_resultado_do_fatorial_de(maximo):
	soma = 0
	resultado = fatorial(maximo)
	arm_resultado = str(resultado)
	for letra in arm_resultado:
		soma += int(letra)
	return soma

if __name__ == "__main__":
	print soma_dos_digitos_do_resultado_do_fatorial_de(100)