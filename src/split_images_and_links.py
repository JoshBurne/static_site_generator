from textnode import *
from extract_markdown_images_from_text import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    count = 0 # debug line
    new_nodes = []
    #print(f"1. old nodes = {old_nodes}")
    #print(f"new_nodes = {new_nodes}\n\n")
    for node in old_nodes:
        
        count += 1 #debug line
        #print(f"2. node {count} = {node}")
        #print(f"new_nodes = {new_nodes}\n\n")

        if node.text_type != TextType.TEXT:
            #print(f"3. node {node}.text_type is not TEXT")
            #print(f"APPENDING NODE")
            new_nodes.append(node)
            #print(f"new_nodes = {new_nodes}\n\n")
            continue
        
        remaining_text = node.text
        
        extracted_image_tuple_list = extract_markdown_images(remaining_text)
        #print(f"6. extracted_image_tuple_list = {extracted_image_tuple_list}")
        #print(f"new_nodes = {new_nodes}\n\n")
        
        if len(extracted_image_tuple_list) == 0:
            new_nodes.append(node)
            #print(f"7. len(extracted_image_tuple_list) == 0 \n APPENDING NODE")
            #print(f"new_nodes = {new_nodes}\n\n")
            continue
        
        if not extracted_image_tuple_list:
            #print(f"8. node is not extracted_image_tuple_list")
            #print(f"APPENDING NODE")
            new_nodes.append(node)
            #print(f"new_nodes = {new_nodes}\n\n")

        tuple_count = 0 # debug line
        for tuple in extracted_image_tuple_list:
            tuple_count += 1 # debug line
            #print(f"9. tuple {tuple_count} is {tuple} in {extracted_image_tuple_list}")
            #print(f"new_nodes = {new_nodes}\n\n")

            parts = remaining_text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            #print(f"10. parts = {parts}")
            #print(f"new_nodes = {new_nodes}\n\n")
            
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
                
            
            if parts [0] != "":
                #print(f"11. {parts}[0] is not empty")
                #print(f"new_nodes = {new_nodes}\n\n")
                #print(f"APPENDING NODE")
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                #print(f"new_nodes = {new_nodes}\n\n")
            #print(f"APPENDING NODE")
            new_nodes.append(TextNode(tuple[0],TextType.IMAGE, tuple[1],))
            #print(f"13. tuple[0] = {tuple[0]}, tuple[1] = {tuple[1]}. \n appending a TextNode({tuple[0]},TextType.IMAGE, {tuple[1]},) ")
            #print(f"new_nodes = {new_nodes}\n\n")
            remaining_text = parts[1]
            #print(f"14. remaining text = {remaining_text}")
            #print(f"new_nodes = {new_nodes}\n\n")

        if remaining_text != "":
            #(f"15. remaining text not equal to empty")
            #print(f"new_nodes = {new_nodes}\n\n")
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            #print(f"16. appending a TextNode({remaining_text}, TextType.TEXT), to new_nodes ")
            #print(f"new_nodes = {new_nodes}\n\n")

    #print(f"FINAL_new_nodes = {new_nodes}\n\n")
    return new_nodes
    





def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


