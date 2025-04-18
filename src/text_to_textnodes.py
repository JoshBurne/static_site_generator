from htmlnode import *
from textnode import *
from TextNodes_from_markdown import *

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)] 
    # creates a list called nodes 
    # adds a textnode object to the list using the "text" string argument 
    # assigns all the text.type to TEXT.

    nodes = split_nodes_image(nodes)
    # calls the split_nodes_image function to process the nodes list and
    # returns a new list of nodes with images extracted.

    nodes = split_nodes_link(nodes)
    # calls the split_nodes_link function to process the nodes list and
    # returns a new list of nodes with links extracted.

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # calls the split_nodes_delimiter function to process the nodes list and
    # returns a new list of nodes with code text extracted

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # calls the split_nodes_delimiter function to process the nodes list and
    # returns a new list of nodes with bold text extracted.

    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    # calls the split_nodes_delimiter function to process the nodes list and
    # returns a new list of nodes with italic text extracted.
    
    return nodes