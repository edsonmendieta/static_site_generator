import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "I am a paragraph of text.")
        node2 = LeafNode("a", "Click here!", {"href": "google.com"})
        self.assertEqual(node.to_html(), "<p>I am a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), "<a href=\"google.com\">Click here!</a>")