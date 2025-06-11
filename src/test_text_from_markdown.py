import unittest

from text_from_markdown import *
from textnode import *



class TestText_from_markdown(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        old_nodes = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        actual = split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD_TEXT),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_split_nodes_delimiter_italic(self):
        old_nodes = [TextNode("This is text with a _italic phrase_ in the middle", TextType.TEXT)]
        actual = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC_TEXT),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)
    
    def test_split_nodes_delimiter_code(self):
        old_nodes = [TextNode("This is text with a `code phrase` in the middle", TextType.TEXT)]
        actual = split_nodes_delimiter(old_nodes, "`", TextType.CODE_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code phrase", TextType.CODE_TEXT),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

