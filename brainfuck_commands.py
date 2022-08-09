from brainfuck_classes import BFException, Char

def _increment_pointer(env):
    env.increment_pointer()

def _decrement_pointer(env):
    env.decrement_pointer()

def _increment_value(env):
    env.increment_value()

def _decrement_value(env):
    env.decrement_value()

def _print_value(env):
    value = env.get_value()
    print(chr(value), end='')

def _input_value(env):
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
