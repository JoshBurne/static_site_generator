        for image_info in extracted_image_tuple_list:
        # for every tuple in extracted_image_tuple_list
        
            image_alt = image_info[0] # the alt text
            image_link = image_info[1] # the link itself

            remaining_text = node.text
            print(f"remaining text = {remaining_text}")

            parts = remaining_text.split(f"![{image_alt}]({image_link})", 1)
       
            new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            