import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent0(self):
        expected = "<h1><p>Hello, world!</p></h1>"

        child_nodes = [LeafNode("p", "Hello, world!")]
        parent_node = ParentNode("h1", child_nodes)

        self.assertEqual(parent_node.to_html(), expected)

    def test_parent1(self):
        expected = "<h1><div><b>This is bold text</b><p>This is a paragraph</p></div></h1>"

        grandchild_nodes = [
            LeafNode("b", "This is bold text"),
            LeafNode("p", "This is a paragraph")
        ]
        child_node = [ParentNode("div", grandchild_nodes)]
        parent_node = ParentNode("h1", child_node)

        self.assertEqual(parent_node.to_html(), expected)

    def test_parent2(self):
        expected = '<h2 href="https://lycanwaredevelopments.org"><div><i>This is italic text</i><p>This is a paragraph</p></div></h2>'

        node_props = {"href": "https://lycanwaredevelopments.org",}
        grandchild_nodes = [
            LeafNode("i", "This is italic text"),
            LeafNode("p", "This is a paragraph")
        ]
        child_node = [ParentNode("div", grandchild_nodes)]
        parent_node = ParentNode("h2", child_node, node_props)

        self.assertEqual(parent_node.to_html(), expected)

    def test_parent3(self):
        expected = '<h3 href="https://lycanwaredevelopments.org" align="center" bgcolor="black" id="dummy"><div align="right" bgcolor="red"><p align="right" bgcolor="red">This is the paragraph</p><p>This is the 2nd paragraph</p></div></h3>'

        node_props = {
            "href": "https://lycanwaredevelopments.org",
            "align": "center",
            "bgcolor": "black",
            "id": "dummy",
        }
        child_node_props = {
            "align": "right",
            "bgcolor": "red",
        }
        grandchild_nodes = [
            LeafNode("p", "This is the paragraph", child_node_props),
            LeafNode("p", "This is the 2nd paragraph")
        ]
        child_node = [ParentNode("div", grandchild_nodes, child_node_props)]
        parent_node = ParentNode("h3", child_node, node_props)

        self.assertEqual(parent_node.to_html(), expected)

    def test_parent4(self):
        expected = '<h3 href="https://lycanwaredevelopments.org" align="center" bgcolor="black" id="dummy"><div align="right" bgcolor="red"><p align="right" bgcolor="red">This is the paragraph</p><p>This is the 2nd paragraph</p></div><div align="right" bgcolor="red"><p align="right" bgcolor="red">This is the paragraph</p><p>This is the 2nd paragraph</p></div></h3>'

        node_props = {
            "href": "https://lycanwaredevelopments.org",
            "align": "center",
            "bgcolor": "black",
            "id": "dummy",
        }
        child_node_props = {
            "align": "right",
            "bgcolor": "red",
        }
        grandchild_nodes = [
            LeafNode("p", "This is the paragraph", child_node_props),
            LeafNode("p", "This is the 2nd paragraph")
        ]
        child_node = [
            ParentNode("div", grandchild_nodes, child_node_props),
            ParentNode("div", grandchild_nodes, child_node_props)
        ]
        parent_node = ParentNode("h3", child_node, node_props)

        self.assertEqual(parent_node.to_html(), expected)

    def test_parent5(self):
        try:
            expected = "HTML tag required"

            child_nodes = [LeafNode("p", "No tag added")]
            ParentNode(None, child_nodes)
        except Exception as e:
            self.assertEqual(e, expected)

    def test_parent6(self):
        try:
            expected = "HTML child node(s) required"

            ParentNode("h1", None)
        except Exception as e:
            self.assertEqual(e, expected)

if __name__ == "__main__":
    unittest.main()