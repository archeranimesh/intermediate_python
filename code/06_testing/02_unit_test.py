import mult
import unittest

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(mult.multiply(test_x, test_y), 50, msg=f"The multiplication of {test_x} and {test_y} should be {test_x * test_y}")


# if __name__ == "__main__":
#    unittest.main()