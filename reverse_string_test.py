from  main import (
    reverse_string
)


class TestReverseString(reverse_string.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")


    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string("hello, world!"), "!dlrow ,olleh")

if __name__ == '__main__':
    reverse_string.main()
