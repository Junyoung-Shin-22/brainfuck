from brainfuck_classes import *
from brainfuck_commands import *
from brainfuck_parse import *
from brainfuck_run import *

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('brainfuck_file', help='brainfuck (.bf) file to execute')
    args = parser.parse_args()

    with open(args.brainfuck_file) as f:
        code = f.read()
    
    tokens = brainfuck_parse(code)
    global_env = Memory()


    brainfuck_run(tokens, global_env)

if __name__ == '__main__':
    main()