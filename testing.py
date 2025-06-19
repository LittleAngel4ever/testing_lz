import function as f
import unittest

class Tests(unittest.TestCase):
    def test_integer_positive_numbers(self):
        self.assertEqual(f.logarimf(1, 2, 3), -0.5)
    
    def test_y_lower_than_x(self):
        self.assertEqual(f.logarimf(2, 1, 3), "")
    
    def test_z_like_x(self):
        self.assertEqual(f.logarimf(1, 3, 1), "")
    
    def test_error_input(self):
        self.assertEqual(f.logarimf(" ", " ", " "), "The line must contain forward")
        self.assertEqual(f.logarimf("a", "b", "c"), "The line must contain number")

if __name__=="__main__":
    unittest.main()