import unittest
from Turtle.turtle_lsystem_tree import generate

class MyFunctionTest(unittest.TestCase):
   def test_myfunction1(self):
      a = 'F'
      expected_result = "FF+[+F-F-F]-[-F+F+F]"
      self.assertEqual(generate(a), expected_result)

if __name__ == '__main__':
    unittest.main()