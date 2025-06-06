from leafnode import LeafNode
from textnode import *

def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(value=self.text)
        if self.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE_TEXT:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href": self.url})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
        else:
            raise Exception ("Invalid text type")