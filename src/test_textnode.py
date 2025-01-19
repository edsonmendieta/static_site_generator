import unittest

from textnode import TextType, TextNode

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


if __name__ == "__main___":
    unittest.main()