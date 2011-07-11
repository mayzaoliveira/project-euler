import unittest

from fibonacci import fibonacci_abaixo_de, soma_fibonacci

class SomaParesFibonacciTestCase(unittest.TestCase):

	def test_soma_elementos_encontrados(self):
		self.assertEqual(44, soma_fibonacci(90))

	def test_fibonacci_abaixo_de(self):
		self.assertEqual([1, 2, 3, 5, 8, 13, 21, 34, 55, 89], fibonacci_abaixo_de(90))
unittest.main()
