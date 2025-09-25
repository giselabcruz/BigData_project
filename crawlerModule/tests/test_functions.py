import unittest
import crawlerModule.functions as fns


class TestLinkGeneration(unittest.TestCase):
    def test_link_generator_with_integer(self):
        self.assertEqual(
            fns.link_generator(12345),
            "https://www.gutenberg.org/cache/epub/12345/pg12345.txt",
        )

    def test_link_generator_with_string(self):
        self.assertEqual(
            fns.link_generator("67890"),
            "https://www.gutenberg.org/cache/epub/67890/pg67890.txt",
        )

    def test_link_generator_with_invalid_string(self):
        with self.assertRaises(TypeError):
            fns.link_generator("abc123")

    def test_link_generator_with_float(self):
        with self.assertRaises(TypeError):
            fns.link_generator(12.34)

    def test_link_generator_with_list(self):
        with self.assertRaises(TypeError):
            fns.link_generator([12345])

    def test_link_generator_with_zero(self):
        self.assertEqual(
            fns.link_generator(0),
            "https://www.gutenberg.org/cache/epub/0/pg0.txt",
        )

    def test_link_generator_with_negative_integer(self):
        self.assertEqual(
            fns.link_generator(-123),
            "https://www.gutenberg.org/cache/epub/-123/pg-123.txt",
        )

    def test_link_generator_with_empty_string(self):
        with self.assertRaises(TypeError):
            fns.link_generator("")

    def test_link_generator_with_whitespace_string(self):
        with self.assertRaises(TypeError):
            fns.link_generator("   ")

    def test_link_generator_with_large_integer(self):
        self.assertEqual(
            fns.link_generator(999999999),
            "https://www.gutenberg.org/cache/epub/999999999/pg999999999.txt",
        )

    def test_link_generator_with_numeric_string_with_leading_zeros(self):
        self.assertEqual(
            fns.link_generator("000123"),
            "https://www.gutenberg.org/cache/epub/123/pg123.txt",
        )

    def test_link_generator_with_special_characters_in_string(self):
        with self.assertRaises(TypeError):
            fns.link_generator("123@#")

    def test_link_generator_with_none(self):
        with self.assertRaises(TypeError):
            fns.link_generator(None)

    def test_link_generator_with_boolean(self):

        with self.assertRaises(TypeError):
            fns.link_generator(True)

    def test_link_generator_with_tuple(self):
        with self.assertRaises(TypeError):
            fns.link_generator((12345,))

    def test_link_generator_with_dict(self):
        with self.assertRaises(TypeError):
            fns.link_generator({"id": 12345})
