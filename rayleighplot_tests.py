import unittest
import random

from rayleighplot import *

class EchoPDFTests(unittest.TestCase):
	def test_echo_pdf_randomly(self):
		echo = echo_pdf(.1, TOTAL_THERMAL_NOISE_POWER_kTB)
		for i in range(1000):
			random_probability = echo(random.uniform(0, 10000)*10e-8)
			print(i, random_probability)
			self.assertGreaterEqual(random_probability, 0)
			self.assertLess(random_probability, 1)

if __name__ == '__main__':
	unittest.main()