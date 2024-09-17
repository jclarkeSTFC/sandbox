import unittest
import random

class example_test(unittest.TestCase):
    def test_passes(self):
        print("pass test_passes")

    def test_fails(self):
        assert(False)
        
    def test_fails_sometimes(self):
        assert(random.random() < 0.5)

if __name__ == "__main__":
    unittest.main()