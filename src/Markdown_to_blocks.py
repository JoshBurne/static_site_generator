from enum import Enum
import re

def find_heading(input):
    return re.findall(r"\#+ ", input)

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(string):
    stripped_string = string.strip()

    raw_blocks = stripped_string.split("\n\n")

    final_blocks = []
    for block in raw_blocks:
        stripped_block = block.strip()
        if stripped_block:
            final_blocks.append(stripped_block)
    return final_blocks

def block_to_block_type(block):
    quoteblock = False
    unordered_listblock = False


    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith ("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return BlockType.HEADING

    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    elif block.startswith('>'):
        lines = block.split("\n")
        for line in lines:
            if line.startswith('>'):
                quoteblock = True
            else:
                return BlockType.PARAGRAPH
        if quoteblock == True:
            return BlockType.QUOTE
    
    elif block.startswith("- ") or block.startswith("* ") or block.startswith("+ "):
        lines = block.split("\n")
        for line in lines:
            if line.startswith("- ") or line.startswith("* ") or line.startswith("+ "):
                unordered_listblock = True
            else:
                return BlockType.PARAGRAPH
        if unordered_listblock == True:
            return BlockType.UNORDERED_LIST
    
    elif block.startswith("1. "):
        
        lines = block.split("\n")

        for i, line in enumerate(lines):
            expected_number = i + 1
            if not line.startswith(f"{expected_number}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
        
    else:
        return BlockType.PARAGRAPH





   
  



