from numeros_naturais import verifica_multiplos, soma_multiplos_abaixo_de

import unittest

class NumerosNaturaisTestCase(unittest.TestCase):

	def test_verificar_se_numero_e_multiplo_de_tres(self):
		assert verifica_multiplos(3)

	def test_verificar_se_numero_e_multiplo_de_cinco(self):
		assert verifica_multiplos(5)

	def test_verificar_se_numero_nao_e_multiplo(self):
		assert not verifica_multiplos(7)

	def test_somar_numeros_multiplos(self):
		self.assertEqual(23, soma_multiplos_abaixo_de(10))
	

unittest.main()