import unittest

from maior_numero_palindromo import palindromo

class MaiorNumeroPalindromo(unittest.TestCase):
	def test_verifica_se_o_numero_eh_palindromo(self):
		self.assertTrue(palindromo(9009))

	def test_encontra_maior_palindromo_feito_de_um_numero_de_tres_digitos(self):
		self.assertEqual()
	
unittest.main()