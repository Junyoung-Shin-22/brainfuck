from brainfuck_classes import *

def _increment_pointer(env, amount):
    env.increment_pointer(amount)

def _decrement_pointer(env, amount):
    env.decrement_pointer(amount)

def _increment_value(env, amount):
    env.increment_value(amount)

def _decrement_value(env, amount):
    env.decrement_value(amount)

def _print_value(env, _):
    value = env.get_value()
    print(chr(value), end='')

def _input_value(env, _):
    value = input()
    try:
        value = ord(value)
    except:
        raise BFException(f'input {value} has wrong type')
    if not Char.min <= value <= Char.max:
        raise BFException(f'input {value} has wrong range')
    
    env.set_value(value)


BRAINFUCK_COMMANDS =\
    {
        '>':
            _increment_pointer,
        '<':
            _decrement_pointer,
        '+':
            _increment_value,
        '-':
            _decrement_value,
        '.':
            _print_value,
        ',':
            _input_value,
    }

_BRAINFUCK_POSITIVE = ('>', '+')
_BRAINFUCK_NEGATIVE = ('<', '-')

_BRAINFUCK_POSITIVE_SIGN = {operation:  1 for operation in _BRAINFUCK_POSITIVE}
_BRAINFUCK_NEGATIVE_SIGN = {operation: -1 for operation in _BRAINFUCK_NEGATIVE}

BRAINFUCK_OPERATION_SIGN =\
{
    operation: sign for operation, sign in
    list(_BRAINFUCK_POSITIVE_SIGN.items()) +
    list(_BRAINFUCK_NEGATIVE_SIGN.items())
}

BRAINFUCK_OPERATION_PAIRS =\
{
    a: b for a, b in 
    list(zip(_BRAINFUCK_POSITIVE, _BRAINFUCK_NEGATIVE)) +
    list(zip(_BRAINFUCK_NEGATIVE, _BRAINFUCK_POSITIVE))
}

BRAINFUCK_OPERATION = _BRAINFUCK_POSITIVE + _BRAINFUCK_NEGATIVE
BRAINFUCK_IO = ('.', ',')