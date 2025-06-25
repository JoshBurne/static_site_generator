from textnode import *
from split_images_and_links import *
from text_from_markdown import *


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    #print(f"text_text_node = {nodes} \n")

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    #print(f"bold nodes = {nodes} \n")

    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)


    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    #print(f"code_nodes = {nodes} \n")

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    return nodes




    
    