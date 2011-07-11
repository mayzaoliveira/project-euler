def divisivel_por(numero, maximo):
	# l = range(1,maximo+1)
	l = [20,19,18,17,16,15,14,13,12,11]
	for divisor in l:
		if numero % divisor != 0:
			return False
	return True

def menor_divisivel(maximo):
	numero = 2520
	while not divisivel_por(numero, maximo):
		numero += 1
	return numero

if __name__ == "__main__":
	print menor_divisivel(20)