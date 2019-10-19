import enum
from queue import Queue
from BrainfuckProgram import BrainFuckProgram

class BrainFuckInterpreter:
    def __init__(self, program):
        self.memory = [0]
        self.memory_pointer = 0
        self.instruction_pointer = 0
        self.input_buffer = Queue()
        self.program = program

    def expand_memory(self):
        self.memory.append(0)

    def move_memory_pointer(self, amount : int) -> None:
        self.memory_pointer = self.memory_pointer + amount
        if self.memory_pointer > len(self.memory) - 1:
            self.expand_memory()

    def print_cell_value(self):
        print(chr(self.memory[self.memory_pointer]), end="")

    def set_cell_value(self, amount : int):
        self.memory[self.memory_pointer] = amount % 256

    def get_user_input(self):
        if self.input_buffer.empty():
            for i in input():
                self.input_buffer.put(ord(i))
        self.set_cell_value(self.input_buffer.get())

    def do_a_loop(self):
        if self.memory[self.memory_pointer] == 0:
            self.instruction_pointer = self.program.get_match(self.instruction_pointer)

    def end_a_loop(self):
        self.instruction_pointer = self.program.get_match(self.instruction_pointer) - 1


    def exec(self):
        if self.program.code[self.instruction_pointer] == '>':
            self.move_memory_pointer(1)
        elif self.program.code[self.instruction_pointer] == '<':
            self.move_memory_pointer(-1)
        elif self.program.code[self.instruction_pointer] == '+':
            self.set_cell_value(self.memory[self.memory_pointer] + 1)
        elif self.program.code[self.instruction_pointer] == '-':
            self.set_cell_value(self.memory[self.memory_pointer] - 1)
        elif self.program.code[self.instruction_pointer] == '.':
            self.print_cell_value()
        elif self.program.code[self.instruction_pointer] == ',':
            self.get_user_input()
        elif self.program.code[self.instruction_pointer] == '[':
            self.do_a_loop()
        elif self.program.code[self.instruction_pointer] == ']':
            self.end_a_loop()
        else:
            print("What the fuck why the hell isn't this code valid you god damn fuck")
            exit(127)
        print(f'{self.memory} {self.memory_pointer} {self.program.code[self.instruction_pointer]}')
        #input()
        self.instruction_pointer += 1
