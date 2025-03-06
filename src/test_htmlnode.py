import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html1(self):
        node = HTMLNode("h1", "This is the header")        
        self.assertEqual(node.props_to_html(), "")

    def test_html2(self):
        expected = ' href="https://lycanwaredevelopments.org"'

        node = HTMLNode("h2", "This is the second header", [], {"href": "https://lycanwaredevelopments.org",})
        self.assertEqual(node.props_to_html(), expected)

    def test_html3(self):
        node_props = {
            "href": "https://lycanwaredevelopments.org",
            "align": "center",
            "bgcolor": "black",
            "id": "dummy",
        }
        expected = ' href="https://lycanwaredevelopments.org" align="center" bgcolor="black" id="dummy"'

        node3 = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("h2", "This is the second header")
        node1 = HTMLNode("h1", "This is the header", [node2, node3], node_props)
        self.assertEqual(node1.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()