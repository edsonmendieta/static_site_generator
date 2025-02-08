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


def block_to_block_type(block: str) -> str:
    if is_heading(block):
        return "heading"
    if is_code(block):
        return "code"
    if is_quote(block):
        return "quote"
    if is_unordered_list(block):
        return "unordered_list"
    if is_ordered_list(block):
        return "ordered_list"
    
    return "paragraph"

def is_heading(block: str) -> str:
    block_lines = block.split('\n')
    if block_lines[0][0] != "#":
        return False
    
    heading = block_lines[0].split(" ")
    if len(heading[0]) <= 6 and heading[1]:
        for char in heading[0]:
            if char != '#':
                return False
    else:
        return False

    return True

def is_code(block: str) -> bool:
    if block[:3] == "```" and block[-3:] == "```":
        return True
    return False

def is_quote(block: str) -> bool:
    block_lines = block.split('\n')
    for line in block_lines:
        if line[0] != '>':
            return False
    
    return True

def is_unordered_list(block:str) -> bool:
    block_lines = block.split('\n')

    for line in block_lines:
        if line[0] + line[1] != "* " and line[0] + line[1] != "- ":
            return False
    
    return True

def is_ordered_list(block: str) -> bool:
    block_lines = block.split('\n')
    
    line_numbers = []
    for line in block_lines:
        period_split = line.split('.')
        if period_split[0].isdigit() == False or period_split[1][0] != " ":
            return False
        else:
            line_numbers.append(period_split[0])
    
    if line_numbers[0] != "1":
        print(line_numbers[0])
        return False 
    else:
        prev_line_number = -1
        for number in line_numbers:
            if int(number) <= int(prev_line_number):
                return False
            else:
                prev_line_number = number

    return True