import unittest

from divisao_um_a_vinte import divisivel_por, menor_divisivel

class DivisaoEntreUmEVinte(unittest.TestCase):
	
	def test_verificar_se_o_numero_e_divisivel_por(self):
		self.assertTrue(divisivel_por(2520, 10))

	def test_encontrar_menor_divisivel(self):
		self.assertEqual(2520, menor_divisivel(10))

unittest.main()