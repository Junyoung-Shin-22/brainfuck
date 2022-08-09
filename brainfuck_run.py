from brainfuck_commands import BRAINFUCK_COMMANDS

def brainfuck_run(tokens, env):
    for token in tokens:
        if isinstance(token, list):
            while env.get_value() != 0:
                brainfuck_run(token, env)

        elif token in BRAINFUCK_COMMANDS:
            BRAINFUCK_COMMANDS[token](env)
      