import unittest


class DummyTest(unittest.TestCase):
	def test_get(self):
		"""
		Dummy Test.
		"""
		a = 1+2
		self.assertEqual(a, 3, msg="Was not equal to 2")