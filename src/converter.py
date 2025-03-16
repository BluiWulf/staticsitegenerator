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
                children = text_to_children(block)
                heading = extract_markdown_headers(block)
                html_nodes.append(HTMLNode(f"h{len(heading[0][0])}", None, children, None))
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass
            case BlockType.PARAGRAPH:
                pass

    return HTMLNode("div", None, html_nodes, None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes
