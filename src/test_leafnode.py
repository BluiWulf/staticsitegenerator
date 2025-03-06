import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf0(self):
        expected = "<p>Hello, world!</p>"

        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), expected)

    def test_leaf1(self):
        expected = "<h1>This is the header</h1>"

        node = LeafNode("h1", "This is the header")        
        self.assertEqual(node.to_html(), expected)

    def test_leaf2(self):
        expected = '<h2 href="https://lycanwaredevelopments.org">This is the second header</h2>'

        node = LeafNode("h2", "This is the second header", {"href": "https://lycanwaredevelopments.org",})
        self.assertEqual(node.to_html(), expected)

    def test_leaf3(self):
        node_props = {
            "href": "https://lycanwaredevelopments.org",
            "align": "center",
            "bgcolor": "black",
            "id": "dummy",
        }
        expected = '<p href="https://lycanwaredevelopments.org" align="center" bgcolor="black" id="dummy">This is the paragraph</p>'

        node = LeafNode("p", "This is the paragraph", node_props)
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()