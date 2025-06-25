from Markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from HTMLNode import *
from Text_to_textNodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
import re

def markdown_to_html_node(markdown):
    list_of_blocks = markdown_to_blocks(markdown)

    block_nodes_list = []

    for block in list_of_blocks:
        block_type = block_to_block_type(block)

        if block_type is BlockType.CODE:
            code_content = block.strip("```").strip()
            code_node = HTMLNode("code", code_content, None)
            pre_node = HTMLNode("pre", None, [code_node])
            block_node = pre_node
            block_nodes_list.append(block_node)
        

        elif block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            

            for line in lines:
                if block_type == BlockType.UNORDERED_LIST:
                    # For unordered lists: remove *, -, or + followed by space
                    clean_line = re.sub(r'^[*\-+]\s+', '', line)
                elif block_type == BlockType.ORDERED_LIST:
                    # For ordered lists: remove number followed by . and space
                    clean_line = re.sub(r'^\d+\.\s+', '', line)

                line_children = text_to_children(clean_line)
                li_node = HTMLNode("li", None, line_children)
                li_nodes.append(li_node)
            tag = block_to_tag(block, block_type)
            block_node = HTMLNode(tag, None, li_nodes)

            block_nodes_list.append(block_node)

        
        else:
            if block_type == BlockType.HEADING:
                block = re.sub(r'^#{1,6}\s+', '', block)
            
            if block_type == BlockType.QUOTE:
                lines = block.split('\n')
                clean_lines = [line.lstrip('> ') for line in lines]
                block = '\n'.join(clean_lines)

            node_list = text_to_children(block)
            tag = block_to_tag(block, block_type)
            block_node = HTMLNode(tag, None, node_list)
            block_nodes_list.append(block_node)
        
    return HTMLNode("div", None, block_nodes_list)
        
        
        
    


        


def text_to_children(text):
    nodes = text_to_textnodes(text)
    HTMLNodes = []
    for textnode in nodes:
        HTML_node = text_node_to_html_node(textnode)
        HTMLNodes.append(HTML_node)
    return HTMLNodes




def block_to_tag(block, block_type):
    if block_type == BlockType.QUOTE:
        tag = "blockquote"
    elif block_type == BlockType.UNORDERED_LIST:
        tag = "ul"
    elif block_type == BlockType.ORDERED_LIST:
        tag = "ol"
    elif block_type == BlockType.CODE:
        tag = "pre"
    elif block_type == BlockType.HEADING:
        if block.startswith("# "):
            tag = "h1"
        elif block.startswith("## "):
            tag = "h2"
        elif block.startswith("### "):
            tag = "h3"
        elif block.startswith("#### "):
            tag = "h4"
        elif block.startswith("##### "):
            tag = "h5"
        elif block.startswith("###### "):
            tag = "h6"
    elif block_type == BlockType.PARAGRAPH:
        tag = "p"
    else:
        raise ValueError ("block_type not recoginised")
    return tag