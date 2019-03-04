#! python3
# Program implements a stack and checks if a given string of brackets is balanced or
# unbalanced.

from stack import stack
import re

check_input = re.compile(r'[^\(\{\[\)\}\]]')

def check_brackets(string):
    if check_input.search(string):
        raise Exception('Input must only contain brackets: (), {}, [].')
    bracket_dict = {')': '(', '}': '{', ']': '['}
    bracket_stack = stack()
    for i in string:
        if i in bracket_dict.values():
            bracket_stack.push(i)
        else:
            if bracket_stack.is_empty() or bracket_dict[i] != bracket_stack.pop():
                return 'unbalanced'
    if bracket_stack.is_empty():
        return 'balanced'
    else:
        return 'unbalanced'