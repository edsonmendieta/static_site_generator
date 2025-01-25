import unittest
import re

from typing import List
from src.leafnode import LeafNode
from src.textnode import TextType, TextNode 
from src.helper_funcs import split_node_strings, split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestHelperFuncs(unittest.TestCase):

    def test_extract_markdown_links(self):
        text1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text2 = "This is text with a link [to boot dev]sadflj(https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        self.assertEqual(
            extract_markdown_links(text1), 
            [
                ('to boot dev', 'https://www.boot.dev'), 
                ('to youtube', 'https://www.youtube.com/@bootdotdev')
            ]
        )
        self.assertEqual(
            extract_markdown_links(text2), 
            [
                ('to youtube', 'https://www.youtube.com/@bootdotdev')
            ]
        )

    def test_extract_markdown_images(self):
        text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text2 = "This is text with a !![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan]asdf(https://i.imgur.com/fJRm4Vk.jpeg)"

        self.assertEqual(
            extract_markdown_images(text1), 
            [
                ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), 
                ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')
            ]
        )
        self.assertEqual(
            extract_markdown_images(text2), 
            [
                ('rick roll', 'https://i.imgur.com/aKaOqIh.gif')
            ]
        )
    
    def test_split_node_strings(self):
        node1 = TextNode("Hello **my** name is **baseball**, ice.", TextType.NORMAL)
        node2 = TextNode("some words. more words **more words**", TextType.NORMAL)
        node3 = TextNode("**bold words** more words more words", TextType.NORMAL)
        node4 = TextNode("**bold words****bold too** more words more words", TextType.NORMAL)
        node5 = TextNode("hi *what**is* your favorite type of ice cream *if*.", TextType.NORMAL)
        node6 = TextNode("my favorite animal ** is a dog", TextType.NORMAL)
        node7 = TextNode("here is a `bit of code` for Christmas", TextType.NORMAL)

        self.assertEqual(split_node_strings(node1, "**"), ['Hello ', '**my**', ' name is ', '**baseball**', ', ice.'])
        self.assertEqual(split_node_strings(node2, "**"), ['some words. more words ', '**more words**']) 
        self.assertEqual(split_node_strings(node3, "**"), ['**bold words**', ' more words more words'])
        self.assertEqual(split_node_strings(node4, "**"), ['**bold words**', '**bold too**', ' more words more words'])
        self.assertEqual(split_node_strings(node5, "*"), ['hi ', '*what*', '*is*', ' your favorite type of ice cream ', '*if*', '.'])
        self.assertEqual(split_node_strings(node6, "*"), ['my favorite animal ', ' is a dog'])
        self.assertEqual(split_node_strings(node7, "`"), ['here is a ', '`bit of code`', ' for Christmas'])

    def test_split_nodes_delimiter(self):
        node1 = TextNode("This is text with a `code block` word", TextType.NORMAL)
        node2 = TextNode("Hello **my** name is **baseball**, ice.", TextType.NORMAL)
        node3 = TextNode("This is text with an unclosed `code block word", TextType.NORMAL)

        self.assertEqual(
            split_nodes_delimiter([node1, node2], "`", TextType.CODE), 
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
                TextNode("Hello **my** name is **baseball**, ice.", TextType.NORMAL)
            ]
        )

        self.assertRaises(Exception, split_nodes_delimiter, [node3], "`", TextType.CODE)



if __name__ == "__name__":
    unittest.main()