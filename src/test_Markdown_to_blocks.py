import unittest
from Markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_block_to_blocktype(self):
        block = "#### This is a heading."
        function = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(function, expected)

    def test_ordered_list_to_blocktype(self):
        block = "1. This is an ordered list. \n2. This is the second line"
        function = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(function, expected)