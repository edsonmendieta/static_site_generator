import re

from typing import List
from .textnode import TextType, TextNode


'''
--------------------------------
                                |
Extract all markdown from text  |
                                |
--------------------------------
'''
def text_to_textnodes(text: str) -> List[TextNode]:
    node = TextNode(text, TextType.NORMAL)

    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes) 
    nodes = split_nodes_link(nodes)

    return nodes

'''
--------------------------------
                                |
Split Nodes by link & img regex |
                                |
--------------------------------
'''
def extract_markdown_links(text:str) -> List[tuple]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_images(text: str) -> List[tuple]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []

    for node in old_nodes: # Check for nodes that don't require splitting
        if node.text_type is not TextType.NORMAL or len(extract_markdown_links(node.text)) < 1:
            new_nodes.append(node)
            continue
        else:
            # 1: extract links
            links_tuple_list = extract_markdown_links(node.text)
            # 2: put them back together in '[]()' format
            links_str_list = []
            for link in links_tuple_list:
                links_str_list.append(f"[{link[0]}]({link[1]})")

            # 3: find(reconstructed_link_text) for all links and store the starting indices in a list
            links_indices = []
            for link in links_str_list:
                links_indices.append(node.text.find(link))

            # 4: loop through original node.text string 
            rev_links_tuple_list = list(reversed(links_tuple_list))
            rev_links_str_list = list(reversed(links_str_list))
            temp_str = ""

            counter = 0
            while counter < len(node.text):
                if rev_links_str_list and counter == node.text.find(rev_links_str_list[-1]):
                    new_nodes.append(TextNode(temp_str, TextType.NORMAL))
                    temp_str = ""
                    new_nodes.append(TextNode(rev_links_tuple_list[-1][0], TextType.LINK, rev_links_tuple_list[-1][1]))

                    counter += len(rev_links_str_list[-1]) # Move counter to index after end of link string

                    rev_links_str_list.pop()
                    rev_links_tuple_list.pop()
                else:
                    temp_str += node.text[counter]
                    counter += 1
            if len(temp_str) > 0:
                new_nodes.append(TextNode(temp_str, TextType.NORMAL))
        
        final_nodes = []
        for node in new_nodes:
            if node.text_type != TextType.NORMAL or node.text != "":
                final_nodes.append(node)
        
        return final_nodes

# Really unecessary as it's a carbon copy of split_nodes_links(). Just here to satisfy a test requirement
def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []

    for node in old_nodes: # Check for nodes that don't require splitting
        if node.text_type is not TextType.NORMAL or len(extract_markdown_images(node.text)) < 1:
            new_nodes.append(node)
            continue
        else:
            # 1: extract links
            images_tuple_list = extract_markdown_images(node.text)
            # 2: put them back together in '[]()' format
            images_str_list = []
            for image in images_tuple_list:
                images_str_list.append(f"![{image[0]}]({image[1]})")

            # 3: find(reconstructed_link_text) for all links and store the starting indices in a list
            images_indices = []
            for image in images_str_list:
                images_indices.append(node.text.find(image))

            # 4: loop through original node.text string 
            rev_images_tuple_list = list(reversed(images_tuple_list))
            rev_images_str_list = list(reversed(images_str_list))
            temp_str = ""

            counter = 0
            while counter < len(node.text):
                if rev_images_str_list and counter == node.text.find(rev_images_str_list[-1]):
                    new_nodes.append(TextNode(temp_str, TextType.NORMAL))
                    temp_str = ""
                    new_nodes.append(TextNode(rev_images_tuple_list[-1][0], TextType.IMAGE, rev_images_tuple_list[-1][1]))

                    counter += len(rev_images_str_list[-1]) # Move counter to index after end of link string

                    rev_images_str_list.pop()
                    rev_images_tuple_list.pop()
                else:
                    temp_str += node.text[counter]
                    counter += 1
            if len(temp_str) > 0:
                new_nodes.append(TextNode(temp_str, TextType.NORMAL))
        
        final_nodes = []
        for node in new_nodes:
            if node.text_type != TextType.NORMAL or node.text != "":
                final_nodes.append(node)
        
        return final_nodes


'''
-------------------------------
                               |
  Split Nodes by a delimiter   |
                               |
-------------------------------
'''
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




def main():

    print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))

if __name__ == "__main__":
    main()