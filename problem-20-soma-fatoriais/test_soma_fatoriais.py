import unittest

from soma_fatoriais import fatorial, soma_dos_digitos_do_resultado_do_fatorial_de

class SomaDosFatoriais(unittest.TestCase):
	def test_encontra_fatorial_de_dez(self):
		self.assertEqual(3628800, fatorial(10))

	def test_soma_dos_fatoriais(self):
		self.assertEqual(27, soma_dos_digitos_do_resultado_do_fatorial_de(10))

unittest.main()