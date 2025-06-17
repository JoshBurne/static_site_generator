import unittest

from split_images_and_links import split_nodes_image, split_nodes_link
from extract_markdown_images_from_text import extract_markdown_images, extract_markdown_links
from textnode import *

class TestSplit_images_and_links(unittest.TestCase):
    
    def test_split_nodes_single_image_func(self):
        text =  [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) on it's own.", TextType.TEXT)]
        function = split_nodes_image(text)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" on it's own.", TextType.TEXT)
        ]
        self.assertEqual(function, expected)

    def test_split_nodes_multi_image_func(self):
        text =  [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) with ![another image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)]
        function = split_nodes_image(text)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" with ", TextType.TEXT),
            TextNode("another image", TextType.IMAGE,"https://i.imgur.com/3elNhQu.png")
        ]
        self.assertEqual(function, expected)

    def test_split_multiple_nodes_multi_image_func(self):
        text =  [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) with ![another image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT), TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) with ![another image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)]
        function = split_nodes_image(text)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" with ", TextType.TEXT),
            TextNode("another image", TextType.IMAGE,"https://i.imgur.com/3elNhQu.png"),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" with ", TextType.TEXT),
            TextNode("another image", TextType.IMAGE,"https://i.imgur.com/3elNhQu.png")
        ]
        self.assertEqual(function, expected)

    def test_split_nodes_double_link_func(self):
        text =  [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)]
        function = split_nodes_link(text)
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(function, expected)