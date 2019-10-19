class BrainFuckProgram:
    def __init__(self, rawCode):
        self.code, self.brackets = self.compile(rawCode)

    def __len__(self):
        return len(self.code)

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

