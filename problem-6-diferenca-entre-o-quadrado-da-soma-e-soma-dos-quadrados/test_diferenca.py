import unittest

from diferenca import soma_dos_quadrados, quadrado_da_soma, diferenca

class DiferencaEntreQuadradoDaSomaESomaDosQaudrados(unittest.TestCase):

	# def test_encontrando_quadrado_de_um_numero(self):
	# 	self.assertEqual(9, quadrado_do_numero(3)) 
	
	def test_soma_dos_quadrados_de_dez_numeros(self):
		self.assertEqual(385, soma_dos_quadrados(11))

	def test_quadrado_da_soma(self):
		self.assertEqual(3025, quadrado_da_soma(11))

	def test_diferenca(self):
		self.assertEqual(2640, diferenca(11))

unittest.main()