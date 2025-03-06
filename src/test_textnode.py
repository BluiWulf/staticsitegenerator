import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_convert1(self):
        node = TextNode("This is a normal text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a normal text node")

    def test_convert2(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_convert3(self):
        node = TextNode("This is an italic text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_convert4(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_convert5(self):
        node = TextNode("This is a link text node", TextType.LINK_TEXT, "https://lycanwaredevelopments.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props_to_html(), ' href="https://lycanwaredevelopments.org"')

    def test_convert6(self):
        node = TextNode("This is an image text node", TextType.IMAGE_TEXT, "https://lycanwaredevelopments.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props_to_html(), ' src="https://lycanwaredevelopments.org" alt="This is an image text node"')

    def test_convert7(self):
        try:
            expected = "Invalid TextType provided"
            node = TextNode("This is an error", "other")
            text_node_to_html_node(node)
        except Exception as e:
            self.assertEqual(str(e), expected)

if __name__ == "__main__":
    unittest.main()