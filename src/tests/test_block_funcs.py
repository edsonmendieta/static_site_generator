import unittest

from src.block_funcs import markdown_to_blocks, block_to_block_type, is_heading, is_code, is_unordered_list, is_ordered_list


class TestBlockFuncs(unittest.TestCase):

    def test_markdown_to_blocks(self):
        test_str = """ # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item """
        test_str2 = """ # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item     """
        test_str3 = """ # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item     """

        self.assertEqual(
            markdown_to_blocks(test_str), 
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]
        )
        self.assertEqual(
            markdown_to_blocks(test_str2), 
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]
        )
        self.assertEqual(
            markdown_to_blocks(test_str3), 
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]
        )
    
    def test_block_to_block_type(self):
        test_str = "### A heading\nalsd;fj\nas;ldf"
        test_str2 = "```;lajfldl\n;aksjdf; alsdkfj\n ;ajf a;jf```"
        test_str3 = """* wlfhh a;lkfj  a;fj\n- aflk;jaf;lkjaf ;lakf \n* aflkjafjl alfj"""
        test_str4 = """1. asdl;fkjasdf\n2. asl;dfkja;sdf as;dja\n3. lkj; alskjf lkajf;"""
        test_str5 = "as;ldkf asdl;fkj ;alkdfj als;kdjf ;adf"

        self.assertEqual(block_to_block_type(test_str), "heading")
        self.assertEqual(block_to_block_type(test_str2), "code")
        self.assertEqual(block_to_block_type(test_str3), "unordered_list")
        self.assertEqual(block_to_block_type(test_str4), "ordered_list")
        self.assertEqual(block_to_block_type(test_str5), "paragraph")
    
    def test_is_heading(self):
        test_str = "### A heading\nalsd;fj\nas;ldf"
        test_str2 = "## # A heading\nalsd;fj\nas;ldf"
        test_str3 = " ## # A heading\nalsd;fj\nas;ldf"
        test_str4 = "####### A heading\nalsd;fj\nas;ldf"
        test_str5 = "###*### A heading\nalsd;fj\nas;ldf"
        test_str6 = "# A heading\nalsd;fj\nas;ldf"
        test_str7 = "# # A heading\nalsd;fj\nas;ldf"

        self.assertTrue(is_heading(test_str))
        self.assertTrue(is_heading(test_str2))
        self.assertFalse(is_heading(test_str3))
        self.assertFalse(is_heading(test_str4))
        self.assertFalse(is_heading(test_str5))
        self.assertTrue(is_heading(test_str6))
        self.assertTrue(is_heading(test_str7))

    def test_is_code(self):
        test_str = "```;lajfldl\n;aksjdf; alsdkfj\n ;ajf a;jf```"
        test_str2 = "` ``;lajfldl\n;aksjdf; alsdkfj\n ;ajf a;jf```"
        test_str3 = "```;lajfldl\n;aksjdf; alsdkfj\n ;ajf a;jf`#`"

        self.assertTrue(is_code(test_str))
        self.assertFalse(is_code(test_str2))
        self.assertFalse(is_code(test_str3))
    
    def test_is_unordered_list(self):
        test_str = """* wlfhh a;lkfj  a;fj\n- aflk;jaf;lkjaf ;lakf \n* aflkjafjl alfj"""
        test_str2 = """*wlfhh a;lkfj  a;fj\n- aflk;jaf;lkjaf ;lakf \n* aflkjafjl alfj"""
        test_str3 = """ * wlfhh a;lkfj  a;fj\n- aflk;jaf;lkjaf ;lakf \n* aflkjafjl alfj"""
        test_str4 = """* wlfhh a;lkfj  a;fj\n* aflk;jaf;lkjaf ;lakf \n* aflkjafjl alfj"""
        test_str5 = """- wlfhh a;lkfj  a;fj\n- aflk;jaf;lkjaf ;lakf \n- aflkjafjl alfj"""

        self.assertTrue(is_unordered_list(test_str))
        self.assertFalse(is_unordered_list(test_str2))
        self.assertFalse(is_unordered_list(test_str3))
        self.assertTrue(is_unordered_list(test_str4))
        self.assertTrue(is_unordered_list(test_str5))

    def test_is_ordered_list(self):
        test_str = """1. asdl;fkjasdf\n2.asl;dfkja;sdf as;dja\n3.lkj; alskjf lkajf;"""
        test_str2 = """1. asdl;fkjasdf\n2. asl;dfkja;sdf as;dja\n3. lkj; alskjf lkajf;"""
        test_str3 = """1. asdl;fkjasdf\n 2. asl;dfkja;sdf as;dja\n3. lkj; alskjf lkajf;"""
        test_str4 = """1. asdl;fkjasdf\n2 . asl;dfkja;sdf as;dja\n3. lkj; alskjf lkajf;"""

        self.assertFalse(is_ordered_list(test_str))
        self.assertTrue(is_ordered_list(test_str2))
        self.assertFalse(is_ordered_list(test_str3))
        self.assertFalse(is_ordered_list(test_str4))


if __name__ == "_main_":
    unittest.main()