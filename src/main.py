from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    html_node = HTMLNode("h1", "This is a header", [HTMLNode("p", "This is a paragraph"), HTMLNode("p", "This is a second paragraph")], {"href": "https://www.google.com", "target": "_blank",})
    print(html_node.__repr__())

if __name__ == "__main__":
    main()