import unittest

from generatepage import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title1(self):
        markdown = "# This is a multiline\nh1 header"
        expected = "This is a multiline"

        title = extract_title(markdown)
        self.assertEqual(title, expected)

    def test_extract_title2(self):
        markdown = str("# This is markdown with multiple h1 headers\n" +
                       "# This is the second h1 header")
        expected = "This is markdown with multiple h1 headers"

        title = extract_title(markdown)
        self.assertEqual(title, expected)

    def test_extract_title3(self):
        markdown = str("### This is markdown with multiple h1 headers\n" +
                       "# This is the first h1 header\n" +
                       "####### This isn't a header\n" +
                       "# This is the second h1 header")
        expected = "This is the first h1 header"

        title = extract_title(markdown)
        self.assertEqual(title, expected)

if __name__ == "__main__":
    unittest.main()