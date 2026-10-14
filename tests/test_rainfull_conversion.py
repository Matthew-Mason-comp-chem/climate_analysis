# test script

import unittest
from rainfull_conversion import inches_to_mm


class test_rainfall_conversion(unittest.TestCase):
	def check_is_number(self):
		result = inches_to_mm(10)

		self.assertIsInstance(result, (int, float))

if __name__ == "__main__":
    unittest.main()
