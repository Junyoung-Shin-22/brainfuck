from brainfuck_classes import *
from brainfuck_commands import *

def brainfuck_run(commands, env):
    for command in commands:
        if isinstance(command, AtomicCommand):
            BRAINFUCK_COMMANDS[command.base_command](env, command.amount)

        elif isinstance(command, BracketCommand):
            while env.get_value() != 0:
                brainfuck_run(command.commands, env)

      