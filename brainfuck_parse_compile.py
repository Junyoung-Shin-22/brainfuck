from brainfuck_classes import *
from brainfuck_commands import *

def _deep_append(lst, value, depth):
    for _ in range(depth):
        lst = lst[-1]
    lst.append(value)

def brainfuck_parse(code):
    parsed = []
    depth = 0

    for token in code:
        if token in BRAINFUCK_COMMANDS:
            _deep_append(parsed, token, depth)
        
        elif token == '[':
            _deep_append(parsed, [], depth)
            depth += 1
        
        elif token == ']':
            depth -= 1
            if depth < 0:
                    raise BFException('bracket mismatch')
    
    if depth != 0:
        raise BFException('bracket mismatch')
    return parsed

def brainfuck_compile(tokens):
    i = 0
    compiled_commands = []

    while i < len(tokens):
        token = tokens[i]

        if isinstance(token, list):
            bracket_commands = brainfuck_compile(token)
            compiled_command = BracketCommand(bracket_commands)
            i += 1
        
        elif token in BRAINFUCK_OPERATION:
            amount = 0
            sign = BRAINFUCK_OPERATION_SIGN[token]
            while i < len(tokens) and (token == tokens[i] or BRAINFUCK_OPERATION_PAIRS[token] == tokens[i]):
                amount += sign * BRAINFUCK_OPERATION_SIGN[tokens[i]]
                i += 1
            compiled_command = AtomicCommand(token, amount)
        
        elif token in BRAINFUCK_IO:
            compiled_command = AtomicCommand(token)
            i += 1
        
        compiled_commands.append(compiled_command)
    
    return compiled_commands