from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_parser import *
from block_parser import *
from converter import *

import re

def main():
    # This section is being used for very quick unit testing before creating addition tests
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

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    test_nodes = text_to_textnodes(text)

    print("\n")
    for node in test_nodes:
        print(f"{node}")

    markdown = str("Anime is really `fun to watch` and some of my recent\n" +
                   "_favorite animes_ are listed below:\n\n\n\n" +
                   "\n\n" +
                   "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n" +
                   "-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n" +
                   "-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)\n\n\n\n" +
                   "\n\n" +
                   "These are all very **fantastic** with a lot of _great stories_\n")
    
    print(markdown_to_blocks(markdown))
    print(block_to_block_type("###### This is a test header"))
    print(block_to_block_type("```\nThis is a code block\nwith multiple lines\n```"))
    print(block_to_block_type(">This is a quote line\n>This is a second quote line"))
    print(block_to_block_type("- This is an unordered list item\n- This is another list item\n- This is another list item"))
    print(block_to_block_type("1. This is an unordered list item\n2. This is another list item"))

    print()
    html_test_node = markdown_to_html_node("###### This is a **test** header")
    print(html_test_node.to_html())

    print()
    code_md = str("```\n" +
                  "This is a **code** block\n" +
                  "This should have no _inline_ formatting\n" +
                  "```")
    html_test_node = markdown_to_html_node(code_md)
    print(html_test_node.to_html())

if __name__ == "__main__":
    main()