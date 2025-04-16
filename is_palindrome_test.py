from  main import (
    is_palindrome
)

class TestPalindrome(is_palindrome.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_case_sensitive(self):
        self.assertFalse(is_palindrome("Madam"))


    def test_with_spaces(self):
        self.assertTrue(is_palindrome("a man a plan a canal panama".replace(" ", "")))
        self.assertFalse(is_palindrome("a man a plan a canal panama"))



if __name__ == '__main__':
    is_palindrome.main()