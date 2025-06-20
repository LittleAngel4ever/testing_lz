import function as f
import unittest

class Tests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(f.logarifm(4, 3, 2), 5)
    
    def test_positive_f(self):
        self.assertEqual(f.logarifm(-2, 1, 3), "f must be positive, received f={f}")
    
    def test_dividing_zero(self):
        self.assertEqual(f.logarifm(5, 3, 1), "h - 1 = 0, division by zero")
    
    def test_error_input(self):
        self.assertEqual(f.logarifm(" ", " ", " "), "The line must contain forward")
        self.assertEqual(f.logarifm("a", "b", "c"), "The line must contain forward")


if __name__=="__main__":
    unittest.main()