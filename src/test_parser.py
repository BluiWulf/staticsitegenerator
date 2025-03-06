import unittest

from textnode import TextNode, TextType
from parser import *

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

    def test_image1(self):
        expected = [("One Punch Man", "https://tenor.com/ZyW9.gif")]

        markdown = "Have you seen ![One Punch Man](https://tenor.com/ZyW9.gif)?"
        images = extract_markdown_images(markdown)
        self.assertEqual(images, expected)

    def test_image2(self):
        expected = [("Solo Leveling", "https://tenor.com/cDopMbQJecV.gif"), ("Freiren", "https://tenor.com/lHwR5fhFMXX.gif")]

        markdown = "Two great animes are ![Solo Leveling](https://tenor.com/cDopMbQJecV.gif) and ![Freiren](https://tenor.com/lHwR5fhFMXX.gif)"
        images = extract_markdown_images(markdown)
        self.assertEqual(images, expected)

    def test_image3(self):
        expected = [
            ("Attack on Titan", "https://tenor.com/eKHRRoHDbqL.gif"),
            ("Dandadan", "https://tenor.com/nZqs80XWAHz.gif"),
            ("Chainsaw Man", "https://tenor.com/rv4ARHFlTtF.gif"),
            ("Demon Slayer", "https://tenor.com/ilMT2WIMnnA.gif"),
            ("Fire Force", "https://tenor.com/bVDBb.gif")
        ]

        markdown = str("Some of my recent favorite animes are " +
                       "![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif), " +
                       "![Dandadan](https://tenor.com/nZqs80XWAHz.gif), " +
                       "![Chainsaw Man](https://tenor.com/rv4ARHFlTtF.gif), " +
                       "![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif) and " +
                       "![Fire Force](https://tenor.com/bVDBb.gif)")
        images = extract_markdown_images(markdown)
        self.assertEqual(images, expected)

    def test_image4(self):
        expected = []

        markdown = "Is (https://tenor.com/twPO9rwLM1h.gif) a valid image?"
        images = extract_markdown_images(markdown)
        self.assertEqual(images, expected)

    def test_image5(self):
        expected = []

        markdown = "Is ![Full Metal Alchemist] a valid image?"
        images = extract_markdown_images(markdown)
        self.assertEqual(images, expected)

    def test_link1(self):
        expected = [("One Punch Man", "https://tenor.com/ZyW9.gif")]

        markdown = "Have you seen [One Punch Man](https://tenor.com/ZyW9.gif)?"
        images = extract_markdown_links(markdown)
        self.assertEqual(images, expected)

    def test_link2(self):
        expected = [("Solo Leveling", "https://tenor.com/cDopMbQJecV.gif"), ("Freiren", "https://tenor.com/lHwR5fhFMXX.gif")]

        markdown = "Two great animes are [Solo Leveling](https://tenor.com/cDopMbQJecV.gif) and [Freiren](https://tenor.com/lHwR5fhFMXX.gif)"
        images = extract_markdown_links(markdown)
        self.assertEqual(images, expected)

    def test_link3(self):
        expected = [
            ("Attack on Titan", "https://tenor.com/eKHRRoHDbqL.gif"),
            ("Dandadan", "https://tenor.com/nZqs80XWAHz.gif"),
            ("Chainsaw Man", "https://tenor.com/rv4ARHFlTtF.gif"),
            ("Demon Slayer", "https://tenor.com/ilMT2WIMnnA.gif"),
            ("Fire Force", "https://tenor.com/bVDBb.gif")
        ]

        markdown = str("Some of my recent favorite animes are" +
                       "[Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif), " +
                       "[Dandadan](https://tenor.com/nZqs80XWAHz.gif), " +
                       "[Chainsaw Man](https://tenor.com/rv4ARHFlTtF.gif), " +
                       "[Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif) and " +
                       "[Fire Force](https://tenor.com/bVDBb.gif)")
        images = extract_markdown_links(markdown)
        self.assertEqual(images, expected)

    def test_link4(self):
        expected = []

        markdown = "Is (https://tenor.com/twPO9rwLM1h.gif) a valid image?"
        images = extract_markdown_links(markdown)
        self.assertEqual(images, expected)

    def test_link5(self):
        expected = []

        markdown = "Is [Full Metal Alchemist] a valid image?"
        images = extract_markdown_links(markdown)
        self.assertEqual(images, expected)

    def test_split_img1(self):
        expected = [TextNode("This is a normal text node", TextType.NORMAL_TEXT)]

        old_nodes = [TextNode("This is a normal text node", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_img2(self):
        expected = [
            TextNode("Have you seen ", TextType.NORMAL_TEXT),
            TextNode("One Punch Man", TextType.IMAGE_TEXT, "https://tenor.com/ZyW9.gif"),
            TextNode("?", TextType.NORMAL_TEXT),
            TextNode("Two great animes are ", TextType.NORMAL_TEXT),
            TextNode("Solo Leveling", TextType.IMAGE_TEXT, "https://tenor.com/cDopMbQJecV.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("Freiren", TextType.IMAGE_TEXT, "https://tenor.com/lHwR5fhFMXX.gif")
        ]

        old_nodes = [
            TextNode("Have you seen ![One Punch Man](https://tenor.com/ZyW9.gif)?", TextType.NORMAL_TEXT),
            TextNode("Two great animes are ![Solo Leveling](https://tenor.com/cDopMbQJecV.gif) and ![Freiren](https://tenor.com/lHwR5fhFMXX.gif)", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_img3(self):
        expected = [
            TextNode("Some of my recent favorite animes are ", TextType.NORMAL_TEXT),
            TextNode("Attack on Titan", TextType.IMAGE_TEXT, "https://tenor.com/eKHRRoHDbqL.gif"),
            TextNode(", ", TextType.NORMAL_TEXT),
            TextNode("Dandadan", TextType.IMAGE_TEXT, "https://tenor.com/nZqs80XWAHz.gif"),
            TextNode(", ", TextType.NORMAL_TEXT),
            TextNode("Chainsaw Man", TextType.IMAGE_TEXT, "https://tenor.com/rv4ARHFlTtF.gif"),
            TextNode(", ", TextType.NORMAL_TEXT),
            TextNode("Demon Slayer", TextType.IMAGE_TEXT, "https://tenor.com/ilMT2WIMnnA.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("Fire Force", TextType.IMAGE_TEXT, "https://tenor.com/bVDBb.gif")
        ]
        markdown = str("Some of my recent favorite animes are " +
                       "![Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif), " +
                       "![Dandadan](https://tenor.com/nZqs80XWAHz.gif), " +
                       "![Chainsaw Man](https://tenor.com/rv4ARHFlTtF.gif), " +
                       "![Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif) and " +
                       "![Fire Force](https://tenor.com/bVDBb.gif)")

        old_nodes = [TextNode(markdown, TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_img4(self):
        expected = [TextNode("Is (https://tenor.com/twPO9rwLM1h.gif) a valid link?", TextType.NORMAL_TEXT)]

        old_nodes = [TextNode("Is (https://tenor.com/twPO9rwLM1h.gif) a valid link?", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_img5(self):
        expected = [TextNode("Is ![Full Metal Alchemist] a valid link?", TextType.NORMAL_TEXT)]

        old_nodes = [TextNode("Is ![Full Metal Alchemist] a valid link?", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_lnk1(self):
        expected = [TextNode("This is a normal text node", TextType.NORMAL_TEXT)]

        old_nodes = [TextNode("This is a normal text node", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_lnk2(self):
        expected = [
            TextNode("Have you seen ", TextType.NORMAL_TEXT),
            TextNode("One Punch Man", TextType.LINK_TEXT, "https://tenor.com/ZyW9.gif"),
            TextNode("?", TextType.NORMAL_TEXT),
            TextNode("Two great animes are ", TextType.NORMAL_TEXT),
            TextNode("Solo Leveling", TextType.LINK_TEXT, "https://tenor.com/cDopMbQJecV.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("Freiren", TextType.LINK_TEXT, "https://tenor.com/lHwR5fhFMXX.gif")
        ]

        old_nodes = [
            TextNode("Have you seen [One Punch Man](https://tenor.com/ZyW9.gif)?", TextType.NORMAL_TEXT),
            TextNode("Two great animes are [Solo Leveling](https://tenor.com/cDopMbQJecV.gif) and [Freiren](https://tenor.com/lHwR5fhFMXX.gif)", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_lnk3(self):
        expected = [
            TextNode("Some of my recent favorite animes are ", TextType.NORMAL_TEXT),
            TextNode("Attack on Titan", TextType.LINK_TEXT, "https://tenor.com/eKHRRoHDbqL.gif"),
            TextNode(", ", TextType.NORMAL_TEXT),
            TextNode("Dandadan", TextType.LINK_TEXT, "https://tenor.com/nZqs80XWAHz.gif"),
            TextNode(", ", TextType.NORMAL_TEXT),
            TextNode("Chainsaw Man", TextType.LINK_TEXT, "https://tenor.com/rv4ARHFlTtF.gif"),
            TextNode(", ", TextType.NORMAL_TEXT),
            TextNode("Demon Slayer", TextType.LINK_TEXT, "https://tenor.com/ilMT2WIMnnA.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("Fire Force", TextType.LINK_TEXT, "https://tenor.com/bVDBb.gif")
        ]
        markdown = str("Some of my recent favorite animes are " +
                       "[Attack on Titan](https://tenor.com/eKHRRoHDbqL.gif), " +
                       "[Dandadan](https://tenor.com/nZqs80XWAHz.gif), " +
                       "[Chainsaw Man](https://tenor.com/rv4ARHFlTtF.gif), " +
                       "[Demon Slayer](https://tenor.com/ilMT2WIMnnA.gif) and " +
                       "[Fire Force](https://tenor.com/bVDBb.gif)")

        old_nodes = [TextNode(markdown, TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_lnk4(self):
        expected = [TextNode("Is (https://tenor.com/twPO9rwLM1h.gif) a valid link?", TextType.NORMAL_TEXT)]

        old_nodes = [TextNode("Is (https://tenor.com/twPO9rwLM1h.gif) a valid link?", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes, expected)

    def test_split_lnk5(self):
        expected = [TextNode("Is [Full Metal Alchemist] a valid link?", TextType.NORMAL_TEXT)]

        old_nodes = [TextNode("Is [Full Metal Alchemist] a valid link?", TextType.NORMAL_TEXT)]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()