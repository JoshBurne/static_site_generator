import unittest
from Text_to_textNodes import *

class TestTexttoTextnodes(unittest.TestCase):
    def test_basic_test(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        function = text_to_textnodes(text)
        expected = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD_TEXT),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC_TEXT),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(function, expected)

if __name__ == "__main__":
    unittest.main()
        

