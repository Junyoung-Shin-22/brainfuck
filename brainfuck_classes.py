class BFException(Exception):
    pass

class Char:
    min = -128
    max =  127

    def __init__(self, address):
        self.address = address
        self.value = 0
    
    def increment(self):
        self.value += 1
        if self.value > Char.max:
            raise BFException(f'char overflow at address {self.address}')
    
    def decrement(self):
        self.value -= 1
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
    
    def increment_pointer(self):
        self.pointer += 1
        if self.pointer >= Memory.SIZE:
            raise BFException('pointer out of range')
    
    def decrement_pointer(self):
        self.pointer -= 1
        if self.pointer < 0:
            raise BFException('pointer out of range')
    
    def increment_value(self):
        self.memory[self.pointer].increment()
    
    def decrement_value(self):
        self.memory[self.pointer].decrement()
    
    def get_value(self):
        return self.memory[self.pointer].get()
    
    def set_value(self, value):
        self.memory[self.pointer].set(value)
