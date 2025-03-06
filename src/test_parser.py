import unittest

from textnode import TextNode, TextType
from parser import split_nodes_delimiter

class TestParser(unittest.TestCase):
    def test_split1(self):
        expected = [TextNode("This is a normal text node", TextType.CODE_TEXT)]

        old_nodes = [TextNode("This is a normal text node", TextType.CODE_TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, " ", TextType.NORMAL_TEXT)
        self.assertEqual(new_nodes, expected)

    def test_split2(self):
        expected = [
            TextNode("This is a ", TextType.NORMAL_TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode(" node", TextType.NORMAL_TEXT)
        ]

        old_nodes = [TextNode("This is a **bold text** node", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, expected)

    def test_split3(self):
        expected = [
            TextNode("This is a ", TextType.NORMAL_TEXT),
            TextNode("italic text", TextType.ITALIC_TEXT),
            TextNode(" node", TextType.NORMAL_TEXT)
        ]

        old_nodes = [TextNode("This is a _italic text_ node", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, expected)

    def test_split4(self):
        expected = [
            TextNode("This is a ", TextType.NORMAL_TEXT),
            TextNode("code text", TextType.CODE_TEXT),
            TextNode(" node", TextType.NORMAL_TEXT)
        ]

        old_nodes = [TextNode("This is a `code text` node", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, expected)

    def test_split5(self):
        try:
            expected = "Node contains invalid Markdown syntax"

            old_nodes = [TextNode("This is a `code text` node", TextType.NORMAL_TEXT)]
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD_TEXT)
        except Exception as e:
            self.assertEqual(str(e), expected)

if __name__ == "__main__":
    unittest.main()