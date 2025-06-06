import unittest

from HTMLNode import HTMLNode

# Creates a class which is designed to run unit tests.
class TestHTMLNode(unittest.TestCase):

    def test_eq_empty_node(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_tag_node(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node, node2)

    def test_noteq_tag_node(self):
        node = HTMLNode("p")
        node2 = HTMLNode("h1")
        self.assertNotEqual(node, node2)
    
    def test_eq_tag_value(self):
        node = HTMLNode("p", "hello world")
        node2 = HTMLNode("p", "hello world")
        self.assertEqual(node, node2)

    def test_noteq_tag_value(self):
        node = HTMLNode("p", "hello world")
        node2 = HTMLNode("p", "goodbye world")
        self.assertNotEqual(node, node2)
    
    def test_eq_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        result = node.props_to_html()
        expected = ' href="https://www.google.com"'
        self.assertEqual(result, expected)
    
    def test_noteq_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        result = node.props_to_html()
        expected = ' href="https://www.google.co.uk"'
        self.assertNotEqual(result, expected)
        
    def test_eq_props_to_html_multi(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(' '))
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)




# Code required for this to work - unexplained as of right now. DO NOT TOUCH
if __name__ == "__main__":
    unittest.main()