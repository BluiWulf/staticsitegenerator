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
