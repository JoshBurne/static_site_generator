import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):

    def test_eq_p(self):
        node = LeafNode("p", "Hello, World!")
        result = node.to_html()
        self.assertEqual(result, "<p>Hello, World!</p>")

    def test_eq_italic(self):
        node = LeafNode("i", "Hi, World!")
        result = node.to_html()
        self.assertEqual(result, "<i>Hi, World!</i>")
    
    def test_eq_link(self):
        node = LeafNode("a", "Search anything you like!", {"href": "https://www.google.com"})
        result = node.to_html()
        self.assertEqual(result, '<a href="https://www.google.com">Search anything you like!</a>')

    def test_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()