import re
class Lexer:
    def __init__(self, input_string: str, token_definitions: dict):
        self.input_string = input_string
        self.token_definitions = token_definitions

    def lex(self) -> list:
        tokens = []
        line_number = 1
        line_start_pos = 0
        pos = 0

        while pos < len(self.input_string):
            match = None
            for token_name, pattern in self.token_definitions.items():
                regex = re.compile(pattern)
                match = regex.match(self.input_string, pos)
                if match:
                    text = match.group(0)
                    if token_name != 'WHITESPACE':
                        tokens.append((token_name, text, line_number, pos - line_start_pos))
                    pos = match.end()
                    break
            if not match:
                raise ValueError(f"Invalid character '{self.input_string[pos]}' at line {line_number}, column {pos - line_start_pos}")
            if '\n' in match.group(0):
                line_number += match.group(0).count('\n')
                line_start_pos = match.end() - len(match.group(0))
            pos = self._skip_whitespace(pos)

        return tokens

    def _skip_whitespace(self, pos):
        return re.match(r'\s*', self.input_string[pos:]).end() + pos

