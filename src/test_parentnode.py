import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Some bold text"), 
                LeafNode(None, "Some normal text"), 
                LeafNode("i", "Some italic text"), 
                LeafNode(None, "Some more normal text")
            ]
        )
        node2 = ParentNode(
            "p", 
            [
                LeafNode("b", "Some bold text", {"ball": "soccerBall"}), 
                LeafNode(None, "Some normal text"), 
                LeafNode("i", "Some italic text"), 
                LeafNode(None, "Some more normal text")
            ]
        )
        node3 = ParentNode(
            "p", 
            [
                LeafNode("b", "Some bold text", {"ball": "soccerBall"}), 
                LeafNode(None, "Some normal text"), 
                LeafNode("i", "Some italic text", {"ball": "tennisBall", "fruit": "orange"}), 
                LeafNode(None, "Some more normal text")
            ], 
            {"ball": "footBall", "color": "skyBlue"}
        )
        node4 = ParentNode(
            "p", 
            [
                LeafNode("b", "Some bold text", {"ball": "soccerBall"}), 
                LeafNode(None, "Some normal text"), 
                ParentNode(
                    "p", 
                    [
                        LeafNode("b", "Hi", {"sport": "baseball"}),
                        ParentNode("p", [LeafNode(None, "Hello I'm a leaf node")])
                    ]
                ),
                LeafNode("i", "Some italic text", {"ball": "tennisBall", "fruit": "orange"}), 
                LeafNode(None, "Some more normal text")
            ], 
            {"ball": "footBall", "color": "skyBlue"}
        )
        self.assertEqual(node.to_html(), "<p><b>Some bold text</b>Some normal text<i>Some italic text</i>Some more normal text</p>")
        self.assertEqual(node2.to_html(), "<p><b ball=\"soccerBall\">Some bold text</b>Some normal text<i>Some italic text</i>Some more normal text</p>")
        self.assertEqual(node3.to_html(), "<p ball=\"footBall\" color=\"skyBlue\"><b ball=\"soccerBall\">Some bold text</b>Some normal text<i ball=\"tennisBall\" fruit=\"orange\">Some italic text</i>Some more normal text</p>")
        self.assertEqual(
            node4.to_html(), 
            "<p ball=\"footBall\" color=\"skyBlue\"><b ball=\"soccerBall\">Some bold text</b>Some normal text<p><b sport=\"baseball\">Hi</b><p>Hello I'm a leaf node</p></p><i ball=\"tennisBall\" fruit=\"orange\">Some italic text</i>Some more normal text</p>"
        )


    def test_to_html_value_error(self):
        
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Some bold text", {"ball": "soccerBall"}), 
                LeafNode(None, "Some normal text"), 
                ParentNode(
                    "", # Empty Tag string ValueError 
                    [
                        LeafNode("b", "Hi", {"sport": "baseball"}),
                        ParentNode("p", [LeafNode(None, "Hello I'm a leaf node")])
                    ]
                ),
                LeafNode("i", "Some italic text", {"ball": "tennisBall", "fruit": "orange"}), 
                LeafNode(None, "Some more normal text")
            ], 
            {"ball": "footBall", "color": "skyBlue"}
        )
        node2 = ParentNode(
            "p", 
            [
                LeafNode("b", "Some bold text", {"ball": "soccerBall"}), 
                LeafNode(None, "Some normal text"), 
                ParentNode(
                    "p", 
                    [
                        LeafNode("b", "Hi", {"sport": "baseball"}),
                        ParentNode(None, [LeafNode(None, "Hello I'm a leaf node")]) # Tag-value of None ValueError
                    ]
                ),
                LeafNode("i", "Some italic text", {"ball": "tennisBall", "fruit": "orange"}), 
                LeafNode(None, "Some more normal text")
            ], 
            {"ball": "footBall", "color": "skyBlue"}
        )
        self.assertRaises(ValueError, node.to_html)
        self.assertRaises(ValueError, node2.to_html)

if __name__ == "__main___":
    unittest.main()