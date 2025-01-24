import unittest

from typing import List
from leafnode import LeafNode
from textnode import TextType, TextNode 
from helper_funcs import split_node_strings, split_nodes_delimiter

class TestHelperFuncs(unittest.TestCase):

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