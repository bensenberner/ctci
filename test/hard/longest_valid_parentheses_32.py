import unittest

from hard.longest_valid_parentheses_32 import longestValidParentheses


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(0, longestValidParentheses(")"))
        self.assertEqual(2, longestValidParentheses("()"))
        self.assertEqual(2, longestValidParentheses("(()"))
        self.assertEqual(4, longestValidParentheses(")()())"))

    def test_middle(self):
        self.assertEqual(2, longestValidParentheses("()(()"))

    def test_long(self):
        self.assertEqual(22, longestValidParentheses(")(((((()())()()))()(()))("))
