def palindromo(numero):

	lista = list(str(numero))

	if lista == list(reversed(lista)): 
		lista = int("".join(lista))
		print lista
		return True 
	return False

	#lista.reverse()
	#print lista


def maior_palindromo():
	lista = []
	for numero in range(999,100,-1):
		for segundo_numero in range(999,100,-1):
			if palindromo(numero*segundo_numero):
				# print "%d - %d" % (numero, segundo_numero)
				lista.append(numero*segundo_numero)

	return max(lista)
if __name__ == "__main__":
	print maior_palindromo()