import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_valid_value(self):
        node1 = HTMLNode("a", "google-link", props={"href": "https://www.google.com"})
        node2 = HTMLNode(props={"href": "sun.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), f" href=\"https://www.google.com\"")
        self.assertEqual(node2.props_to_html(), f" href=\"sun.com\" target=\"_blank\"")

    def test_props_to_html_with_no_props(self):
        node1 = HTMLNode(props={})
        node2 = HTMLNode()
        self.assertEqual(node1.props_to_html(), "") 
        self.assertEqual(node2.props_to_html(), "")

    def test_repr(self):
        node1 = HTMLNode()
        node1_string = f"""
        --------- HTMLNode ---------
        Tag: None
        Value: None
        Children: None
        Props: None
        ----------------------------
        """
        node2 = HTMLNode("a", "google-link", [node1], {"href": "https://www.google.com"})
        node2_string = f"""
        --------- HTMLNode ---------
        Tag: a
        Value: google-link
        Children: [
        --------- HTMLNode ---------
        Tag: None
        Value: None
        Children: None
        Props: None
        ----------------------------
        ]
        Props: {{'href': 'https://www.google.com'}}
        ----------------------------
        """
        self.assertEqual(repr(node1), node1_string)
        self.assertEqual(repr(node2), node2_string)


if __name__ == "__main__":
    unittest.main()