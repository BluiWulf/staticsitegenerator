import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node3 = TextNode("This is a link", TextType.LINK_TEXT, "https://www.boot.dev")
        node4 = TextNode("This is a link", TextType.LINK_TEXT, "https://www.boot.dev")
        self.assertEqual(node3, node4)

    def test_noteq(self):
        node5 = TextNode("This is italic text", TextType.ITALIC_TEXT)
        node6 = TextNode("This is a link", TextType.LINK_TEXT, "https://www.boot.dev")
        self.assertNotEqual(node5, node6)

    def test_noteq2(self):
        node7 = TextNode("This is a link", TextType.LINK_TEXT)
        node8 = TextNode("This is a link", TextType.LINK_TEXT, "https://www.boot.dev")
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()