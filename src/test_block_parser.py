import unittest

from textnode import TextNode, TextType
from block_parser import *

class TestBlockParser(unittest.TestCase):
    def test_blocks1(self):
        expected = [
            "Anime is really `fun to watch` and some of my recent\n_favorite animes_ are listed below:",
            "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)",
            "These are all very **fantastic** with a lot of _great stories_"
        ]
        markdown = str("Anime is really `fun to watch` and some of my recent\n" +
                       "_favorite animes_ are listed below:\n\n" +
                       "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n" +
                       "-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n" +
                       "-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)\n\n" +
                       "These are all very **fantastic** with a lot of _great stories_\n")

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected)

    def test_blocks2(self):
        expected = [
            "Anime is really `fun to watch` and some of my recent\n_favorite animes_ are listed below:",
            "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)",
            "These are all very **fantastic** with a lot of _great stories_"
        ]
        markdown = str("Anime is really `fun to watch` and some of my recent\n" +
                       "_favorite animes_ are listed below:\n\n\n\n" +
                       "\n\n" +
                       "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n" +
                       "-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n" +
                       "-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)\n\n\n\n" +
                       "\n\n" +
                       "These are all very **fantastic** with a lot of _great stories_\n")

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected)

    def test_blocks3(self):
        expected = [
            str("Anime is really `fun to watch` and some of my recent\n" +
                "_favorite animes_ are listed below:\n" +
                "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n" +
                "-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n" +
                "-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)\n" +
                "These are all very **fantastic** with a lot of _great stories_")
        ]
        markdown = str("Anime is really `fun to watch` and some of my recent\n" +
                       "_favorite animes_ are listed below:\n" +
                       "-![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif)\n" +
                       "-![Dandadan](https://tenor.com/nZqs80XWAHz.gif)\n" +
                       "-![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif)\n" +
                       "These are all very **fantastic** with a lot of _great stories_\n")

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected)

    def test_type1(self):
        markdown = "# This is a heading"
        expected = BlockType.HEADING

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type2(self):
        markdown = "###### This is a heading"
        expected = BlockType.HEADING

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type3(self):
        markdown = "######## This is a heading"
        expected = BlockType.PARAGRAPH

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type4(self):
        markdown = "```\nThis is a code block\n```"
        expected = BlockType.CODE

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type5(self):
        markdown = "```This is a code block```"
        expected = BlockType.CODE

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type6(self):
        markdown = "```\nThis is a code block\n"
        expected = BlockType.PARAGRAPH

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type7(self):
        markdown = "`\nThis is a code block\n`"
        expected = BlockType.PARAGRAPH

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type8(self):
        markdown = str("```\n" +
                       "This is a code block\n" +
                       "with multiple lines\n" +
                       "```")
        expected = BlockType.CODE

        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type9(self):
        markdown = ">This is a quote block"
        expected = BlockType.QUOTE
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type10(self):
        markdown = ">    This is a quote block"
        expected = BlockType.QUOTE
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type11(self):
        markdown = str(">This is a quote line\n" +
                       ">This is a second quote line\n" +
                       ">This is a third quote line")
        expected = BlockType.QUOTE
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type12(self):
        markdown = str(">This is a quote line\n" +
                       "This is a second quote line\n" +
                       ">This is a third quote line")
        expected = BlockType.PARAGRAPH
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type13(self):
        markdown = str("- This is a list item\n" +
                       "- This is a second list item\n" +
                       "- This is a third list item")
        expected = BlockType.UNORDERED_LIST
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type14(self):
        markdown = str("- This is a list item\n" +
                       "-This is a second list item\n" +
                       "- This is a third list item")
        expected = BlockType.PARAGRAPH
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type15(self):
        markdown = str("- This is a list item\n" +
                       " This is a second list item\n" +
                       "- This is a third list item")
        expected = BlockType.PARAGRAPH
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type16(self):
        markdown = str("1. This is a list item\n" +
                       "2. This is a second list item\n" +
                       "3. This is a third list item")
        expected = BlockType.ORDERED_LIST
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type17(self):
        markdown = str("1. This is a list item\n" +
                       ". This is a second list item\n" +
                       "3. This is a third list item")
        expected = BlockType.PARAGRAPH
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type18(self):
        markdown = str("1. This is a list item\n" +
                       "3. This is a second list item\n" +
                       "2. This is a third list item")
        expected = BlockType.PARAGRAPH
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

    def test_type17(self):
        markdown = str("- This is a list item\n" +
                       "2. This is a second list item\n" +
                       "3. This is a third list item")
        expected = BlockType.PARAGRAPH
    
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, expected)

if __name__ == "__main__":
    unittest.main()