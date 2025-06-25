import unittest
from markdown_to_html_node import markdown_to_html_node
from HTMLNode import *
from parentnode import *
from leafnode import *



class TestMarkdown_to_html_node(unittest.TestCase):
    def test_paragraph(self):
        md = "This is a simple paragraph."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is a simple paragraph.</p></div>")
    
    def test_paragraph_with_formatting(self):
        md = "This has **bold** and _italic_ text."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This has <b>bold</b> and <i>italic</i> text.</p></div>")

    def test_heading(self):
        md = "# This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")

    def test_code_block(self):
        md = "```\nprint('hello world')\n```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><pre><code>print('hello world')</code></pre></div>")

    def test_quote(self):
        md = "> This is a quote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote</blockquote></div>")
    
    def test_unordered_list(self):
        md = "* Item 1\n* Item 2\n* Item 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>")

    def test_multiple_blocks(self):
        md = "# Heading\n\nThis is a paragraph.\n\n* List item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Heading</h1><p>This is a paragraph.</p><ul><li>List item</li></ul></div>")

    
# Code required for this to work - unexplained as of right now. DO NOT TOUCH
if __name__ == "__main__":
    unittest.main()