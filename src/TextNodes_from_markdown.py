from operator import index
from textnode import *
from htmlnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter,text_type):
    new_nodes = [] # This will hold the processed nodes
    for node in old_nodes:

         # If the node is not of type TextType.TEXT, skip the splitting
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # If there is no delimiter in the text, add the node unchanged
        if delimiter not in node.value:
            new_nodes.append(node)
            continue

        # Split the node's value by the delimiter
        split_parts = node.value.split(delimiter)
        
        # Check for mismatched delimiters (odd number of parts => invalid syntax)
        if len(split_parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.value}")

        # Iterate through each part, alternating between text types
        for index, part in enumerate(split_parts):
            if part:  # Skip empty parts (e.g., leading/trailing delimiters)
                if index % 2 == 0:  # Even index => outside delimiters
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:  # Odd index => inside delimiters
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes
        

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    # !\[ matches the exclamation mark and opening square bracket
    # (.*?) is a capture group that matches any character (lazily) inside the square brackets
    # \]\( matches the closing square bracket and opening parenthesis
    # (.*?) is another capture group that matches any character (lazily) inside the parentheses
    # \) matches the closing parenthesis
    return matches
    
def extract_markdown_links(text):

    # If the node is not of type TextType.TEXT, skip the splitting
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.Text:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text # Start processing the entire node's text
        matches = extract_markdown_images(node.text) # Get all images from the text

        for alt, url in matches:
        # Process each match sequentially
            markdown_syntax = f"![{alt}]({url})"
            # Locate the full markdown string
            start_index = remaining_text.find(markdown_syntax) # find where the image syntax starts

            if index == -1:
                # If the syntax isn't found (unexpected), stop processing this match
                continue

            # Split the text into three parts: before, the image, and after
            before_text = remaining_text[:start_index]
            after_text = remaining_text[start_index + len(markdown_syntax):]
            # Create a new TextNode for the text before the image
            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            # Create a new TextNode for the image
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            # Update remaining_text to the text after the image
            remaining_text = after_text
        # After processing all images, if there's any text left, add it as a TextNode
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.Text:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        matches = extract_markdown_links(node.text)
        for text, url in matches:
            # Process each match sequentially
            markdown_syntax = f"[{text}]({url})"
            # Locate the full markdown string
            start_index = remaining_text.find(markdown_syntax)
            if start_index == -1:
                # If the syntax isn't found (unexpected), stop processing this match
                continue
            # Split the text into three parts: before, the link, and after
            before_text = remaining_text[:start_index]
            after_text = remaining_text[start_index + len(markdown_syntax):]
            # Create a new TextNode for the text before the link
            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            # Create a new TextNode for the link
            new_nodes.append(TextNode(text, TextType.LINK, url))
            # Update remaining_text to the text after the link
            remaining_text = after_text
        # After processing all links, if there's any text left, add it as a TextNode
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )




def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://example.com)"
    )
    self.assertListEqual([("link", "https://example.com")], matches)

def test_extract_markdown_links_and_images(self):
    text = (
        "This is text with a [link](https://example.com) and an "
        "![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    links = extract_markdown_links(text)
    images = extract_markdown_images(text)
    self.assertListEqual([("link", "https://example.com")], links)
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], images)