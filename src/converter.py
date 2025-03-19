import re

from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_parser import *
from block_parser import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                children = text_to_children(block[block.index(" ") + 1:])
                html_nodes.append(ParentNode(f"h{len(block[:block.index(" ")])}", children))
            case BlockType.CODE:
                code_match = re.search(r"```\s*(.*?)\s*```", block, re.DOTALL)
                if code_match:
                    code = code_match.group(1).strip("\n")
                children = text_to_children(code, True)
                html_nodes.append(ParentNode("pre", children))
            case BlockType.QUOTE:
                quote = re.sub(r"\n>\s*", "\n", block[1:].lstrip())
                children = text_to_children(quote)
                html_nodes.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                items = list(map(lambda text: re.sub(r"-\s*", "", text), items))
                children = []
                for item in items:
                    granchildren = text_to_children(item)
                    children.append(ParentNode("li", granchildren))
                html_nodes.append(ParentNode("ul", children))
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                items = list(map(lambda text: re.sub(r"\d+\.\s*", "", text), items))
                children = []
                for item in items:
                    granchildren = text_to_children(item)
                    children.append(ParentNode("li", granchildren))
                html_nodes.append(ParentNode("ol", children))
            case BlockType.PARAGRAPH:
                children = text_to_children(block)
                html_nodes.append(ParentNode("p", children))

    return ParentNode("div", html_nodes, None)

def text_to_children(text, code_block = False):
    html_nodes = []

    if code_block == False:
        text_nodes = text_to_textnodes(text)
    else:
        text_nodes = [TextNode(text, TextType.CODE_TEXT)]

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes
