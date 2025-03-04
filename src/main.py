from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    node_children = [
        HTMLNode("p", "This is a paragraph"),
        HTMLNode("p", "This is a second paragraph")
    ]
    node_props = {
        "href": "https://lycanwaredevelopments.org",
        "align": "center",
        "bgcolor": "black",
        "id": "dummy",
    }

    text_node = TextNode("This is some anchor text", TextType.LINK_TEXT, 'https://www.boot.dev')
    html_node = HTMLNode("h1", "This is a header", node_children, node_props)
    leaf_node = LeafNode("h2", "This is a 2nd header", node_props)

    print(f"{text_node.__repr__()}\n")
    print(f"{html_node.__repr__()}\n")
    print(f"{leaf_node.to_html()}\n")

if __name__ == "__main__":
    main()