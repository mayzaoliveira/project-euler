import unittest

from maior_fator_primo import eh_primo, fatores_primos_de

class SomaDosPrimos(unittest.TestCase):
	def test_verifica_se_o_numero_eh_primo(self):
		self.assertTrue(eh_primo(2))

	# def test_encontra_fatores_primos_de_um_numero(self):
	# 	self.assertEqual([5, 7, 13, 29], fatores_primos_de(13195))

	def test_encontra_o_ultimo_fator_primo_de_um_numero(self):
		self.assertEqual(29, fatores_primos_de(13195))

unittest.main()