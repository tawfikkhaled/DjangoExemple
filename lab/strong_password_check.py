"""
https://leetcode.com/problems/strong-password-checker/
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
"""
import unittest

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        moves = 0
        length = len(password)
        newLength = length
        added = 0
        lower = False
        capital = False
        digit = False
        replaced = 0

        modifIndex = -3

        i = 0
        while (i<length):
            repeated = 0
            while True:
                if (97 <= ord(password[i]) <=122):
                    lower = True
                if (65 <= ord(password[i]) <=90):
                    capital = True
                if (48 <= ord(password[i]) <=57):
                    digit = True
                repeated += 1
                if ( i == 0 or i>=length or password[i] != password[i-1]):
                    break
                i += 1

            if (i>=2):
                if ( repeated > 2)i#() - modifIndex > 2 and password[i] == password[i-1] and password[i] == password[i-2]):

                    # add something to consider possibilty of removing or replace+remove
                    #combinaison optimale de replace remove
                    # TODO problème sac à dos
                    modifIndex = i
                    if (newLength<6):
                        newLength += 1
                        added += 1
                    elif (newLength>20):
                        newLength -= 1
                    else :
                        replaced += 1
                    moves += 1
            i += 1


        if (newLength<6):
            added += 6 - newLength
            moves += 6 - newLength
        return moves + max( 3 - (lower + capital + digit + added + replaced), 0) + max(0, newLength - 20)





        
test_cases = (("1337C0d3",0), ("aA1", 3), ("a", 5), ("aaa123", 1), ("1111111111", 3), ("bbaaaaaaaaaaaaaaacccccc", 8))

class TestStringMethods(unittest.TestCase):
    def test(self):
        for test_case in test_cases:
            self.assertEqual(Solution().strongPasswordChecker(test_case[0]), test_case[1])

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
