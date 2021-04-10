"""
description
"""
import unittest

class Solution:
    def func(self, input: str) -> int:
        return 0





        
test_cases = (("", 0), ("g", 0))

class TestStringMethods(unittest.TestCase):
    def test(self):
        for test_case in test_cases:
            self.assertEqual(Solution().func(test_case[0]), test_case[1])

    """
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """

if __name__ == '__main__':
    unittest.main()
