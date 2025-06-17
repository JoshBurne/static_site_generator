from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        split_nodes = []
        new_list = node.text.split(delimiter)

        if len(new_list) % 2 == 0:
            raise Exception ("Node requires a closing delimiter")
        
        for i in range(len(new_list)):
            if new_list[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(new_list[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(new_list[i], text_type))
        
        new_nodes.extend(split_nodes)
    return new_nodes
        

        




        

