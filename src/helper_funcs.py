from typing import List
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.NORMAL or node.text.count(delimiter) == 0:
            new_nodes.append(node)
            continue
        else:
            if node.text.count(delimiter) % 2 != 0: # missing a matching closing delimiter
                raise Exception("Node text contains invalid Markdown syntax.")

            split_strings = split_node_strings(node, delimiter)
            for string in split_strings:
                if delimiter in string:
                    new_nodes.append(TextNode(string.lstrip(delimiter).rstrip(delimiter), text_type))
                else:
                    new_nodes.append(TextNode(string, TextType.NORMAL))
        
    return new_nodes


def split_node_strings(node: TextNode, delimiter: str) -> List[int]:
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

    split_strings = [] # Remove empty strings from return value
    for sub in sub_strings:
        if delimiter in sub and len(sub) > len(delimiter) * 2:
            split_strings.append(sub)
        if sub and delimiter not in sub:
            split_strings.append(sub)

    return split_strings