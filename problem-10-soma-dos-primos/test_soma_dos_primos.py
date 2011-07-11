import unittest

from soma_dos_primos import eh_primo, soma_dos_primos_ateh

class SomaDosPrimos(unittest.TestCase):
	def test_verifica_se_o_numero_eh_primo(self):
		self.assertTrue(eh_primo(3))
	
	def test_soma_dos_primos_ateh(self):
		self.assertEqual(17, soma_dos_primos_ateh(10))

unittest.main()