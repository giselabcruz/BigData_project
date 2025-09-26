import unittest
from unittest.mock import MagicMock

from crawlerModule.core import functions as fns


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
            fns.link_generator(12.34)  # type: ignore

    def test_link_generator_with_list(self):
        with self.assertRaises(TypeError):
            fns.link_generator([12345])  # type: ignore

    def test_link_generator_with_zero(self):
        with self.assertRaises(TypeError):
            fns.link_generator(0)

    def test_link_generator_with_negative_integer(self):
        with self.assertRaises(TypeError):
            fns.link_generator(-12345)

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
            fns.link_generator(None)  # type: ignore

    def test_link_generator_with_boolean(self):

        with self.assertRaises(TypeError):
            fns.link_generator(True)

    def test_link_generator_with_tuple(self):
        with self.assertRaises(TypeError):
            fns.link_generator((12345,))  # type: ignore

    def test_link_generator_with_dict(self):
        with self.assertRaises(TypeError):
            fns.link_generator({"id": 12345})  # type: ignore


class TestFetchPageAsTextUnit(unittest.TestCase):
    def test_fetch_page_as_text_success(self):
        client = MagicMock()
        fake_text = "The Project Gutenberg EBook of Some Book"
        client.get_as_text.return_value = fake_text

        url = "https://gutendex.com/fake"
        result = fns.fetch_page_as_text(client, url)

        self.assertIn("Gutenberg", result)

    def test_fetch_page_as_text_error(self):
        client = MagicMock()
        client.get_as_text.side_effect = Exception("Not found")

        url = "https://gutendex.com/invalid"
        with self.assertRaises(Exception):
            fns.fetch_page_as_text(client, url)


class TestFetchPageAsJson(unittest.TestCase):

    def test_fetch_page_as_json_success(self):

        client = MagicMock()
        fake_json = {"count": 2, "results": [{"id": 1}, {"id": 2}]}  # type: ignore
        client.get_as_json.return_value = fake_json
        url = "https://gutendex.com/books"
        response = fns.fetch_page_as_json(client, url)

        self.assertIn("count", response)
        self.assertIn("results", response)
        self.assertEqual(response["count"], 2)

    def test_fetch_page_as_json_error(self):
        client = MagicMock()
        client.get_as_json.side_effect = Exception("Invalid endpoint")

        url = "https://gutendex.com/invalid_endpoint"
        with self.assertRaises(Exception):
            fns.fetch_page_as_json(client, url)
