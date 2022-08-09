from brainfuck_classes import BFException
from brainfuck_commands import BRAINFUCK_COMMANDS

def deep_append(lst, value, depth):
    for _ in range(depth):
        lst = lst[-1]
    lst.append(value)

def brainfuck_parse(code):
    parsed = []
    depth = 0

    for token in code:
        if token in BRAINFUCK_COMMANDS:
            deep_append(parsed, token, depth)
        
        elif token == '[':
            deep_append(parsed, [], depth)
            depth += 1
        
        elif token == ']':
            depth -= 1
            if depth < 0:
                    raise BFException('bracket mismatch')
    
    if depth != 0:
        raise BFException('bracket mismatch')
    return parsed