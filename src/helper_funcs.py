from typing import List
from textnode import TextType, TextNode

# def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
#     new_nodes = []

#     for node in old_nodes:
#         if node.text_type is not TextType.NORMAL:
#             new_nodes.append(node)
#             continue
#         else:
#             if node.text.count(delimiter) % 2 is not 0: # missing a matching closing delimiter
#                 raise Exception("Node text contains invalid Markdown syntax.")


def split_markup_strings(node: TextNode, delimiter: str) -> List[int]:
    sub_strings = []
    curr_str = ""
    for i in range(0, len(node.text)): 
        if curr_str.count(delimiter) < 2:
            curr_str += node.text[i]
        else:
            first_delim = curr_str.find(delimiter)
            sub_strings.append(curr_str[:first_delim]) # normal text extracted
            sub_strings.append(curr_str[first_delim:]) # delim text extracted

            curr_str = node.text[i]

    if curr_str.count(delimiter) == 2:
        first_delim = curr_str.find(delimiter)
        sub_strings.append(curr_str[:first_delim]) # normal text extracted
        sub_strings.append(curr_str[first_delim:]) # delim text extracted
    else:
        sub_strings.append(curr_str)

    final_strings = [] # Remove empty strings from return value
    for sub in sub_strings:
        if sub:    
            final_strings.append(sub)

    return final_strings


node1 = TextNode("Hello **my** name is **baseball**, ice.", TextType.NORMAL)
node2 = TextNode("some words. more words **more words**", TextType.NORMAL)
node3 = TextNode("**bold words** more words more words", TextType.NORMAL)
node4 = TextNode("**bold words****bold too** more words more words", TextType.NORMAL)
print(split_markup_strings(node1, "**"))
print(split_markup_strings(node2, "**"))
print(split_markup_strings(node3, "**"))
print(split_markup_strings(node4, "**"))
