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

if __name__ == "__main__":
    unittest.main()