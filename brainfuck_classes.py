class BFException(Exception):
    pass

class Char:
    NUM_BYTE = 4
    min = -2 ** (NUM_BYTE * 8)
    max = -min - 1

    def __init__(self, address):
        self.address = address
        self.value = 0
    
    def increment(self, amount=1):
        self.value += amount
        if self.value > Char.max:
            raise BFException(f'char overflow at address {self.address}')
    
    def decrement(self, amount):
        self.value -= amount
        if self.value < Char.min:
            raise BFException(f'char overflow at address {self.address}')
    
    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value
        

class Memory:
    SIZE = 32768

    def __init__(self):
        self.memory = [Char(i) for i in range(Memory.SIZE)]
        self.pointer = 0
    
    def increment_pointer(self, amount=1):
        self.pointer += amount
        if self.pointer >= Memory.SIZE:
            raise BFException('pointer out of range')
    
    def decrement_pointer(self, amount=1):
        self.pointer -= amount
        if self.pointer < 0:
            raise BFException('pointer out of range')
    
    def increment_value(self, amount=1):
        self.memory[self.pointer].increment(amount)
    
    def decrement_value(self, amount=1):
        self.memory[self.pointer].decrement(amount)
    
    def get_value(self):
        return self.memory[self.pointer].get()
    
    def set_value(self, value):
        self.memory[self.pointer].set(value)


class AtomicCommand:
    def __init__(self, base_command, amount=1):
        self.base_command = base_command
        self.amount = amount
    
    def __str__(self):
        return f'{self.base_command}{self.amount}'

class BracketCommand:
    def __init__(self, commands):
        self.commands = commands
    
    def __str__(self):
        return '[' + ', '.join(str(c) for c in self.commands) + ']'