from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from parser import *

import re

def main():
    node_props = {
        "href": "https://lycanwaredevelopments.org",
        "align": "center",
        "bgcolor": "black",
        "id": "dummy",
    }
    htmlnode_children = [
        HTMLNode("p", "This is a paragraph"),
        HTMLNode("p", "This is a second paragraph")
    ]
    parentnode_children = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

    text_node = TextNode("This is some anchor text", TextType.LINK_TEXT, 'https://www.boot.dev')
    html_node = HTMLNode("h1", "This is a header", htmlnode_children, node_props)
    leaf_node = LeafNode("h2", "This is a 2nd header", node_props)
    parent_node = ParentNode("p", parentnode_children, node_props)

    print(f"{text_node.__repr__()}\n")
    print(f"{html_node.__repr__()}\n")
    print(f"{leaf_node.to_html()}\n")
    print(f"{parent_node.to_html()}\n")

    print(split_nodes_delimiter([TextNode("This is a **bold text** node", TextType.NORMAL_TEXT)], "**", TextType.BOLD_TEXT))
    print(extract_markdown_images('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'))
    print(extract_markdown_links('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)'))
    print(split_nodes_image([TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.NORMAL_TEXT)]))
    print(split_nodes_link([TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.NORMAL_TEXT)]))

if __name__ == "__main__":
    main()