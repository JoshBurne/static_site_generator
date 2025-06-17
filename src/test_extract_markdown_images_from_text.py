import unittest
from extract_markdown_images_from_text import *


class TestExtract_markdown_images(unittest.TestCase):
    def test_extract_markdown_images_from_text(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        function = extract_markdown_images(text)
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertEqual(function, expected)

    def test_extract_markdown_links_from_text(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        function = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(function, expected)