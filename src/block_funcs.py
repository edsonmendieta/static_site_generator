from typing import List
from .textnode import TextType, TextNode

from .helper_funcs import *


def markdown_to_blocks(markdown: str) -> List[str]:
    blocks = markdown.split('\n\n')
    blocks_non_empty = []
    for block in blocks:
        if block:
            blocks_non_empty.append(block)

    for i in range(len(blocks_non_empty)):
        blocks_non_empty[i] = blocks_non_empty[i].lstrip().rstrip()

    
    return blocks_non_empty

