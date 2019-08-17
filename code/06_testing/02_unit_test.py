# import the class, module to be unit tested.
import mult
import unittest

# unit test should always subclass from unittest.TestCase
class TestMultiply(unittest.TestCase):
    # test case name should start with test_
    def test_multiply(self):
        test_x = 5
        test_y = 10
        # assertion is from the unit test assertion file.
        self.assertEqual(mult.multiply(test_x, test_y), 50, msg=f"The multiplication of {test_x} and {test_y} should be {test_x * test_y}")


if __name__ == "__main__":
    # invoke unit test by calling the main() method.
    unittest.main()