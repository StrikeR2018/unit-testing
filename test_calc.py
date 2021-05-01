import unittest
import calc

class TestCase(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(2, 2), 4)
    
    def test_add_(self):
        self.assertEqual(calc.add(3, 6), 18)

    def test_sub(self):
        self.assertEqual(calc.sub(6, 4), 2)

    def test_sub_(self):
	      self.assertEqual(calc.sub(9, 3), 6)

    def test_mul(self):
        self.assertEqual(calc.mul(5, 6), 11)
    
    def test_mul_(self):
        self.assertEqual(calc.mul(4, 2), 8)
        
    def test_div_1(self):
        self.assertEqual(calc.div(14, 7), 2)

    def test_div_2(self):
        self.assertEqual(calc.div(10, 0), None)

if __name__ == '__main__':
    unittest.main()
