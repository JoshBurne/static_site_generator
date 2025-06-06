import unittest

from parentnode import ParentNode
from leafnode import LeafNode


# Creates a class which is designed to run unit tests.
class TestParentNode(unittest.TestCase):
    def test_basic_eq(self):
        child_node = LeafNode("p", "Hello World!")
        parent_node = ParentNode("h1", [child_node])
        self.assertEqual(parent_node.to_html(), "<h1><p>Hello World!</p></h1>")

    def test_layered_eq(self):
        child_node = LeafNode("p", "Hello World!")
        parent_node = ParentNode("h1", [child_node])
        grandparent_node = ParentNode("i",[parent_node])
        self.assertEqual(grandparent_node.to_html(), "<i><h1><p>Hello World!</p></h1></i>")

    def test_no_tag(self):
        child_node = LeafNode("p", "Hello World!")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_no_children(self):
        parent_node = ParentNode("h1", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()




# Code required for this to work - unexplained as of right now. DO NOT TOUCH
if __name__ == "__main__":
    unittest.main()