import unittest
import divisible
class DivisibleTestCase(unittest.TestCase):
    def test_divisible(self):
        self.assertTrue(divisible.divisible_by(10,2))
        # self.assertTrue(divisible.divisible_by(10,3))
        self.assertFalse(divisible.divisible_by(10,3))
        # TODO: how to check exception in unittest
        #self.assertRaises(ZeroDivisionError, divisible.divisible_by(10,0))





if __name__ == "__main__":
    unittest.main()