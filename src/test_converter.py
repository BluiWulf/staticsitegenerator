import unittest

from converter import markdown_to_html_node

class TestInlineParser(unittest.TestCase):
    def test_heading(self):
        expected = "<div><h6>This is a <b>test</b> header</h6></div>"
        markdown = "###### This is a **test** header"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_code_block(self):
        expected = "<div><pre><code>This is a **code** block\nThis should have no _inline_ formatting</code></pre></div>"
        markdown = str("```\n" +
                       "This is a **code** block\n" +
                       "This should have no _inline_ formatting\n" +
                       "```")
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_quote(self):
        expected = "<div><blockquote>This is a <i>quote</i> block\nThis should have <b>inline</b> formatting</blockquote></div>"
        markdown = str(">This is a _quote_ block\n" +
                       ">This should have **inline** formatting")
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_ulist(self):
        expected = "<div><ul><li>This is the first <i>list</i> item</li><li>This is the second <b>list</b> item</li><li>This is the third <code>list</code> item</li></ul></div>"
        markdown = str("- This is the first _list_ item\n" +
                       "- This is the second **list** item\n" +
                       "- This is the third `list` item")
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_olist(self):
        expected = "<div><ol><li>This is the first <i>list</i> item</li><li>This is the second <b>list</b> item</li><li>This is the third <code>list</code> item</li></ol></div>"
        markdown = str("1. This is the first _list_ item\n" +
                       "2. This is the second **list** item\n" +
                       "3. This is the third `list` item")
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_paragraph(self):
        expected = "<div><p>This is just a simple <i>paragraph</i> with some\nadditional <b>formatting</b> added in.</p></div>"
        markdown = str("This is just a simple _paragraph_ with some\n" +
                       "additional **formatting** added in.")
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

if __name__ == "__main__":
    unittest.main()