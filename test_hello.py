# test_hello.py
import unittest
from Hello import greet

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins!")

if __name__ == "__main__":
    unittest.main()
