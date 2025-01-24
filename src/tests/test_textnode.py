import unittest

from leafnode import LeafNode
from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node1 = TextNode("I am a text node", TextType.LINK)
        node2 = TextNode("I am a text node", TextType.LINK)
        node3 = TextNode("I am a text node", TextType.LINK, None)
        self.assertEqual(node1, node2)
        self.assertEqual(node1, node3)
        
    def test_not_eq(self):
        node1 = TextNode("I like baseball", TextType.BOLD)
        node2 = TextNode("I like soccer", TextType.BOLD)
        node3 = TextNode("I like baseball", TextType.IMAGE)
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, node3)
    
    def test_repr(self):
        node1 = TextNode("I like baseball", TextType.BOLD)
        self.assertEqual("TextNode(I like baseball, bold, None)", repr(node1))

    def test_text_node_to_html_node(self):
        node = text_node_to_html_node(TextNode("Filler words", TextType.NORMAL))
        self.assertIsInstance(node, LeafNode)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Filler words")
        
        node2 = text_node_to_html_node(TextNode("Filler words", TextType.BOLD))
        self.assertIsInstance(node2, LeafNode)
        self.assertEqual(node2.tag, "b")
        self.assertEqual(node2.value, "Filler words")

        node3 = text_node_to_html_node(TextNode("Filler words", TextType.ITALIC))
        self.assertIsInstance(node3, LeafNode)
        self.assertEqual(node3.tag, "i")
        self.assertEqual(node3.value, "Filler words")

        node4 = text_node_to_html_node(TextNode("Filler words", TextType.CODE))
        self.assertIsInstance(node4, LeafNode)
        self.assertEqual(node4.tag, "code")
        self.assertEqual(node4.value, "Filler words")

        node5 = text_node_to_html_node(TextNode("Link to Google", TextType.LINK, "google.com"))
        self.assertIsInstance(node5, LeafNode)
        self.assertEqual(node5.tag, "a")
        self.assertEqual(node5.value, "Link to Google")
        self.assertEqual(node5.props, {"href": "google.com"})

        node6 = text_node_to_html_node(TextNode("Some alt text", TextType.IMAGE, "imageSrc.com"))
        self.assertIsInstance(node6, LeafNode)
        self.assertEqual(node6.tag, "img")
        self.assertEqual(node6.value, "")
        self.assertEqual(node6.props, {"src": "imageSrc.com", "alt": "Some alt text"})


if __name__ == "__main___":
    unittest.main()