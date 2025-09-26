import unittest
from crawlerModule.core import functions as fns
from crawlerModule.services.http_client import HttpClient


class TestFetchPageAsText(unittest.TestCase):
    def test_fetch_page(self):
        client = HttpClient()
        url = fns.link_generator(12345)
        content = fns.fetch_page_as_text(client, url)
        self.assertIn("The Project Gutenberg", content)

    def test_fetch_page_invalid_url(self):
        client = HttpClient()
        url = "https://www.gutenberg.org/cache/epub/invalid/pginvalid.txt"
        with self.assertRaises(Exception):
            fns.fetch_page_as_text(client, url)

    def test_fetch_with_known_page(self):
        client = HttpClient()
        url = "https://www10.ulpgc.es"
        content = fns.fetch_page_as_text(client, url)
        self.assertIn("Universidad de Las Palmas de Gran Canaria", content)


class TestFetchPageAsJsonIntegration(unittest.TestCase):
    def test_fetch_page_as_json_real(self):
        client = HttpClient(timeout=30)
        url = "https://gutendex.com/books"
        response = fns.fetch_page_as_json(client, url)

        self.assertIn("count", response)
        self.assertIn("results", response)
        self.assertIsInstance(response["results"], list)
