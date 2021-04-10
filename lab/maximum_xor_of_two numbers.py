"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
"""
import unittest
from typing import List

class Solution:
    # TODO tri 
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for el1 in nums:
            for el2 in nums:
                res = max(res, el1 ^ el2)
        return res





        
test_cases = (([3,10,5,25,2,8], 28), ([1,1], 0))

class TestStringMethods(unittest.TestCase):
    def test(self):
        for test_case in test_cases:
            self.assertEqual(Solution().findMaximumXOR(test_case[0]), test_case[1])

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
    fusion("")
