import unittest

from soma_da_potencia import potencia, soma_da_potencia

class SomaDosDigitosDaPotenciaDeUmNumero(unittest.TestCase):
	def test_encontra_potencia_de_um_numero(self):
		self.assertEqual(32768, potencia(2,15))
	def test_soma_da_potencia(self):
		self.assertEqual(26, soma_da_potencia(2,15))
unittest.main()