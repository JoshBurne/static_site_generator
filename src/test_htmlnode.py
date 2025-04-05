import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)
    

    def test_parent_node_with_props(self):
        child = LeafNode("p", "paragraph text")
        parent = ParentNode("section", [child], {"id": "section1", "class": "main-content"})
        self.assertEqual(
            parent.to_html(),
            '<section id="section1" class="main-content"><p>paragraph text</p></section>'
        )

    def test_deeply_nested_structure(self):
        # Create a structure with 4 levels of nesting
        text_node = LeafNode(None, "Click me")
        button_text = ParentNode("span", [text_node], {"class": "btn-text"})
        button = ParentNode("button", [button_text], {"type": "submit"})
        form_group = ParentNode("div", [button], {"class": "form-group"})
        form = ParentNode("form", [form_group], {"action": "/submit", "method": "post"})
        
        self.assertEqual(
            form.to_html(),
            '<form action="/submit" method="post"><div class="form-group"><button type="submit"><span class="btn-text">Click me</span></button></div></form>'
        )

class test_text_node_to_html_node(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")