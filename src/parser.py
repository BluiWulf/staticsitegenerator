from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
        else:
            splits = node.text.split(delimiter)
            if len(splits) == 1:
                raise Exception("Node contains invalid Markdown syntax")
            new_nodes.extend([
                TextNode(splits[0], TextType.NORMAL_TEXT),
                TextNode(splits[1], text_type),
                TextNode(splits[2], TextType.NORMAL_TEXT)
            ])

    return new_nodes
