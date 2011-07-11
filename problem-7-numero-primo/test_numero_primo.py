import unittest

from numeros_primos import eh_primo, elemento_primo

class NumeroPrimo(unittest.TestCase):
	def test_verifica_se_o_numero_e_primo(self):
		self.assertTrue(eh_primo(2))	

	def test_verifica_se_tres_eh_primo(self):
		self.assertTrue(eh_primo(3))

	def test_verifica_se_quatro_eh_primo(self):
		self.assertFalse(eh_primo(4))

	def test_verifica_se_dezenove_eh_primo(self):
		self.assertTrue(eh_primo(19))

	def test_encontra_o_sexto_elemento_primo(self):
		self.assertEqual(13, elemento_primo(6))
	
unittest.main()