import unittest
from unittest.mock import patch, call

from dynamic_recursive.parens import print_all_parens


class MyTestCase(unittest.TestCase):
    @patch("builtins.print")
    def test_3(self, mock_print):
        print_all_parens(3)
        self.assertEqual(5, mock_print.call_count)
        mock_print.assert_has_calls(
            [
                call("((()))"),
                call("(()())"),
                call("(())()"),
                call("()(())"),
                call("()()()"),
            ],
            any_order=True,
        )
