import enum
from queue import Queue

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
        for i in input():
            input_buffer.add(i)
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
        self.instruction_pointer += 1

    def run(self):
        while self.instruction_pointer < len(self.program.code):
            self.exec()

class BrainFuckProgram:
    def __init__(self, rawCode):
        self.code, self.brackets = self.compile(rawCode)

    def compile(self, codeFromFile : str) -> tuple:
        code = list(filter(lambda x : x in {'+', '-', '>', '<', '.', ',', '[', ']'}, codeFromFile))
        matches = []
        matching_brackets = {}
        for i in range(len(code)):
            if code[i] == '[':
                matches.append(i)
            elif code[i] == ']':
                beginning_bracket_locaiton = matches.pop()
                matching_brackets[beginning_bracket_locaiton] = i
                matching_brackets[i] = beginning_bracket_locaiton
        return (code, matching_brackets)

    def get_match(self, x : int) -> int:
        return self.brackets[x]

g = "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[-]"

f = """ 1 +++++ +++               Set Cell #0 to 8
 2 [
 3     >++++               Add 4 to Cell #1; this will always set Cell #1 to 4
 4     [                   as the cell will be cleared by the loop
 5         >++             Add 4*2 to Cell #2
 6         >+++            Add 4*3 to Cell #3
 7         >+++            Add 4*3 to Cell #4
 8         >+              Add 4 to Cell #5
 9         <<<<-           Decrement the loop counter in Cell #1
10     ]                   Loop till Cell #1 is zero
11     >+                  Add 1 to Cell #2
12     >+                  Add 1 to Cell #3
13     >-                  Subtract 1 from Cell #4
14     >>+                 Add 1 to Cell #6
15     [<]                 Move back to the first zero cell you find; this will
16                         be Cell #1 which was cleared by the previous loop
17     <-                  Decrement the loop Counter in Cell #0
18 ]                       Loop till Cell #0 is zero
19
20 The result of this is:
21 Cell No :   0   1   2   3   4   5   6
22 Contents:   0   0  72 104  88  32   8
23 Pointer :   ^
24
25 >>.                     Cell #2 has value 72 which is 'H'
26 >---.                   Subtract 3 from Cell #3 to get 101 which is 'e'
27 +++++ ++..+++.          Likewise for 'llo' from Cell #3
28 >>.                     Cell #5 is 32 for the space
29 <-.                     Subtract 1 from Cell #4 for 87 to give a 'W'
30 <.                      Cell #3 was set to 'o' from the end of 'Hello'
31 +++.----- -.----- ---.  Cell #3 for 'rl' and 'd'
32 >>+.                    Add 1 to Cell #5 gives us an exclamation point
33 >++.                    And finally a newline from Cell #6"""

b = BrainFuckInterpreter(BrainFuckProgram(f))
b.run()
