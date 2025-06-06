import unittest

from textnode import TextNode, TextType

# Creates a class which is designed to run unit tests.
class TestTextNode(unittest.TestCase):
    
    # Defines a method to test equal *(must start with "test_" to be discoverable by test.sh)
    def test_eq(self):
        # Create two TextNode objects that should be identical
        node = TextNode("this is a test text", TextType.BOLD_TEXT)
        node2 = TextNode("this is a test text", TextType.BOLD_TEXT)
        # test that the objects are identical
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        # Test whether the default setting of URL to "None" is working.
        node = TextNode("this is a test text", TextType.BOLD_TEXT, None)
        node2 = TextNode("this is a test text", TextType.BOLD_TEXT)
        
        self.assertEqual(node, node2)

    def test_not_eq_text_content(self):
        # Test whether the text content being different is working as intended.
        node = TextNode("this is text", TextType.BOLD_TEXT)
        node2 = TextNode("this is different text", TextType.BOLD_TEXT)
        # Confirm that the two nodes are NOT equal
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        # Test whether the text type being different is working as intedned.
        node = TextNode("this is a test text", TextType.BOLD_TEXT)
        node2 = TextNode("this is a test text", TextType.ITALIC_TEXT)
        # Confirm that the two nodes are NOT equal
        self.assertNotEqual(node, node2)




# Code required for this to work - unexplained as of right now. DO NOT TOUCH
if __name__ == "__main__":
    unittest.main()