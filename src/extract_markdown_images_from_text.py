import re

def extract_markdown_images(text):
    # takes raw markdown text and returns a LIST of TUPLES, each tuple should -
    # contain the, 1. alt-text, and 2. URL, of any markdown images.
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):  
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
