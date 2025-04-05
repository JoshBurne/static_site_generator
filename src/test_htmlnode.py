import unittest

from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' href="https://example.com" target="_blank"')

    def test_props_to_html_not_equal(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        html_props = node.props_to_html()
        self.assertNotEqual(html_props, ' href="https://example.com" target="not_blank"')
    
    def test_repr(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        testrepr = repr(node)
        expected_repr = "tag = None, value = None, children = None, props = {'href': 'https://example.com', 'target': '_blank'}"
        self.assertEqual(testrepr, expected_repr)