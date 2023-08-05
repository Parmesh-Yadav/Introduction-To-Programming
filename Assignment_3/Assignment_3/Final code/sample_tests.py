import unittest
import numpy as np
from unittest.mock import patch
import a3 as my

tolerance = 0.011

class TestPolygon(unittest.TestCase):
	# P1 is the square and P2 a pentagon
	inp = np.array([[1.0, 1.0, 1.0], [1.0, 5.0, 1.0], [5.0, 5.0, 1.0], [5.0, 1.0, 1.0]])
	P1 = my.Polygon(inp)
	inp2 = np.array([[2.0, 1.0, 1.0], [4.0, 1.0, 1.0], [5.0, 2.0, 1.0], [3.0, 3.0, 1.0], [1.0, 2.0, 1.0]])
	P2 = my.Polygon(inp2)
	
	def test_1(self):
		
		user_output = self.P1.rotate(90)
		exp_output = (np.array([1.0, 5.0, 5.0, 1.0]), np.array([-1.0, -1.0, -5.0, -5.0]))
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

	def test_2(self):

		user_output = self.P1.translate(2, 2)
		exp_output = (np.array([3.0, 7.0, 7.0, 3.0]), np.array([1.0, 1.0, -3.0, -3.0]))
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

	def test_3(self):

		user_output = self.P1.scale(3, 2)
		exp_output = (np.array([-1.0, 11.0, 11.0, -1.0]), np.array([3.0, 3.0, -5.0, -5.0]))
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

	def test_4(self):
		
		user_output = self.P2.rotate(-45)
		exp_output = (np.array([0.71, 2.12, 2.12, 0.0, -0.71]), np.array([2.12, 3.54, 4.95, 4.24, 2.12]))
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

	def test_5(self):

		user_output = self.P2.scale(0.5, 0.3)
		exp_output = (np.array([0.78, 1.48, 1.48, 0.42, 0.07]), np.array([3.01, 3.44, 3.86, 3.65, 3.01]))
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

class TestCircle(unittest.TestCase):

	C1 = my.Circle(2.0, 2.0, 3.0) # 2,2 is center and 3 is radius
	
	def test_1(self):
		
		user_output = self.C1.rotate(45)
		exp_output = (2.83, 0.0, 3)
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

	def test_2(self):

		user_output = self.C1.scale(0.5)
		exp_output = (2.83, 0.0, 1.5)
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

	def test_3(self):

		user_output = self.C1.translate(-3, 3)
		exp_output = (-0.17, 3.0, 1.5)
		np.testing.assert_allclose(exp_output, user_output, rtol=tolerance)

if __name__ == '__main__':
	unittest.main()
