import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    sections = []
    blocks = []

    sections = markdown.split("\n\n")
    for section in sections:
        if section != "":
            blocks.append(section.strip())

    return blocks

def block_to_block_type(block):
    if len(extract_markdown_headers(block)) != 0:
        return BlockType.HEADING
    if len(extract_markdown_code(block)) != 0:
        return BlockType.CODE
    if len(extract_markdown_quote(block)) == len(block.split("\n")):
        return BlockType.QUOTE
    if len(extract_markdown_unordered_list(block)) == len(block.split("\n")):
        return BlockType.UNORDERED_LIST
    
    ordered = extract_markdown_ordered_list(block)
    if len(ordered) == len(block.split("\n")):
        line = ordered[0]
        if line[0] == "1. ":
            for i in range(1, len(ordered)):
                line = ordered[i]
                if line[0] != f"{i + 1}. ":
                    return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

# Helper Functions

def extract_markdown_headers(text):
    return re.findall(r"^(#{1,6})\s(.*)", text, re.MULTILINE)

def extract_markdown_code(text):
    return re.findall(r"(```)(\s*.*\s*)(```)", text, re.DOTALL)

def extract_markdown_quote(text):
    return re.findall(r"^(>)(.*)", text, re.MULTILINE)

def extract_markdown_unordered_list(text):
    return re.findall(r"^(-\s)(.*)", text, re.MULTILINE)

def extract_markdown_ordered_list(text):
    return re.findall(r"^(\d+\.\s)(.*)", text, re.MULTILINE)
