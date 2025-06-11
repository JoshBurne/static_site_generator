from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if text_type is TextType.TEXT:
            new_nodes.append(node)
            continue
    
        new_list = node.text.split(delimiter)

        if len(new_list) % 2 == 0:
            raise Exception ("Node requires a closing delimiter")
        
        new_nodes.append(TextNode(new_list[0], TextType.TEXT))
        new_nodes.append(TextNode(new_list[1], text_type))
        new_nodes.append(TextNode(new_list[2], TextType.TEXT))
        
    return new_nodes
        

        




        

