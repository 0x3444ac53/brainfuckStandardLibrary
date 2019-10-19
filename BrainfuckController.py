from BrainfuckInterpreter import BrainFuckInterpreter
from BrainfuckProgram import BrainFuckProgram
from sys import argv

class BrainfuckController:
    def __init__(self, filePath : str):
        with open(filePath, 'r') as f:
            rawCode = f.read()
        self.program = BrainFuckProgram(rawCode)
        self.interpreter = BrainFuckInterpreter(self.program)

    def run(self):
        while self.interpreter.instruction_pointer < len(self.program):
            self.interpreter.exec()

def main():
    print(f'{argv[1]}')
    p = BrainfuckController(argv[1])
    p.run()

main()
