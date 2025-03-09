import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        splits = node.text.split(delimiter)
        sections = []
        if len(splits) % 2 == 0:
            raise Exception("Node contains invalid Markdown syntax")
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                sections.append(TextNode(splits[i], TextType.NORMAL_TEXT))
            else:
                sections.append(TextNode(splits[i], text_type))
        new_nodes.extend(sections)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text == "":
            continue
        images = extract_markdown_images(node.text)
        if len(images) < 1:
            new_nodes.append(node)
            continue
        sections = re.split(r'(!\[.*?\]\(.*?\))', node.text)
        splits = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                splits.append(TextNode(sections[i], TextType.NORMAL_TEXT))
            else:
                image = extract_markdown_images(sections[i])[0]
                splits.append(TextNode(image[0], TextType.IMAGE_TEXT, image[1]))
        new_nodes.extend(splits)
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text == "":
            continue
        links = extract_markdown_links(node.text)
        if len(links) < 1:
            new_nodes.append(node)
            continue
        sections = re.split(r'(\[.*?\]\(.*?\))', node.text)
        splits = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                splits.append(TextNode(sections[i], TextType.NORMAL_TEXT))
            else:
                link = extract_markdown_links(sections[i])[0]
                splits.append(TextNode(link[0], TextType.LINK_TEXT, link[1]))
        new_nodes.extend(splits)
    
    return new_nodes

def text_to_textnodes(text):
    new_nodes = []
    old_node = [TextNode(text, TextType.NORMAL_TEXT)]

    new_nodes = split_nodes_image(old_node)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD_TEXT)
    new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC_TEXT)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE_TEXT)

    return new_nodes

# Helper Functions

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
