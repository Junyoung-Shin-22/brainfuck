from brainfuck_classes import *
from brainfuck_commands import *
from brainfuck_parse_compile import *
from brainfuck_run import *

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('brainfuck_file', help='brainfuck (.bf) file to execute')
    args = parser.parse_args()

    with open(args.brainfuck_file) as f:
        code = f.read()
    
    parsed = brainfuck_parse(code)
    compiled = brainfuck_compile(parsed)

    global_env = Memory()
    brainfuck_run(compiled, global_env)

def _debug():
    code = '++--[+]<<>,.[>[<]]'
    parsed = brainfuck_parse(code)
    compiled = brainfuck_compile(parsed)

    print(*compiled, sep=', ')

if __name__ == '__main__':
    # _debug()
    main()