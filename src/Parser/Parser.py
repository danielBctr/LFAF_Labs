class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        return self.parse_assignment_expression()

    def parse_assignment_expression(self):
        left = self.parse_comparison_expression()

        if self.current_token()[0] == 'ASSIGN':
            operator = self.current_token()
            self.advance()

            right = self.parse_comparison_expression()

            if self.current_token()[0] == 'COMMA':
                self.advance()
                right = self.parse_assignment_expression()

            left = {
                'type': 'assignment_expression',
                'operator': operator,
                'left': left,
                'right': right
            }

        return left

    def parse_comparison_expression(self):
        left = self.parse_logical_expression()

        while self.current_token()[0] in ['EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'LESS_THEN_EQUALS', 'GREATER_THAN', 'GREATER_THAN_EQUAL']:
            operator = self.current_token()
            self.advance()

            right = self.parse_logical_expression()

            left = {
                'type': 'comparison_expression',
                'operator': operator,
                'left': left,
                'right': right
            }

        return left

    def parse_logical_expression(self):
        left = self.parse_addition_expression()

        while self.current_token()[0] in ['AND', 'OR', 'NOT']:
            if self.current_token()[0] == 'NOT':
                operator = self.current_token()
                self.advance()

                expression = self.parse_addition_expression()

                left = {
                    'type': 'not_expression',
                    'operator': operator,
                    'expression': expression
                }
            else:
                operator = self.current_token()
                self.advance()

                right = self.parse_addition_expression()

                left = {
                    'type': 'logical_expression',
                    'operator': operator,
                    'left': left,
                    'right': right
                }

        return left

    def parse_addition_expression(self):
        left = self.parse_multiplication_expression()

        while self.current_token()[0] in ['PLUS', 'MINUS']:
            operator = self.current_token()
            self.advance()

            right = self.parse_multiplication_expression()

            left = {
                'type': 'basic_algebra',
                'operator': operator,
                'left': left,
                'right': right
            }

        return left

    def parse_multiplication_expression(self):
        left = self.parse_primary_expression()

        while self.current_token()[0] in ['TIMES', 'DIVIDE']:
            operator = self.current_token()
            self.advance()

            right = self.parse_primary_expression()

            left = {
                'type': 'advanced_algebra',
                'operator': operator,
                'left': left,
                'right': right
            }

        return left

    def parse_primary_expression(self):
        token = self.current_token()
        self.advance()

        if token[0] == 'NUMBER':
            return {
                'type': 'number',
                'value': token[1]
            }
        elif token[0] == 'IDENTIFIER':
            return {
                'type': 'variable',
                'name': token[1]
            }
        elif token[0] == 'LPAREN':
            expression = self.parse_expression()
            self.expect('RPAREN')
            return expression
        elif token[0] == 'IF':
            condition = self.parse_expression()
            self.expect('COLON')
            if_expression = self.parse_expression()

            if self.current_token()[0] == 'ELSE':
                self.advance()
                self.expect('COLON')
                else_expression = self.parse_expression()
                return {
                    'type': 'if_else_expression',
                    'condition': condition,
                    'if_expression': if_expression,
                    'else_expression': else_expression
                }

            return {
                'type': 'if_expression',
                'condition': condition,
                'if_expression': if_expression
            }
        elif token[0] == 'TRUE':
            return {
                'type': 'boolean',
                'value': True
            }
        elif token[0] == 'FALSE':
            return {
                'type': 'boolean',
                'value': False
            }
        elif token[0] == 'NOT':
            expression = self.parse_expression()
            return {
                'type': 'not_expression',
                'operator': token,
                'expression': expression
            }

        raise ValueError(f"Invalid token '{token[1]}' at line {token[2]}, column {token[3]}")

    def current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        else:
            return ('EOF', 'End of File', -1, -1)

    def advance(self):
        self.current_token_index += 1

    def expect(self, token_type):
        if self.current_token()[0] != token_type:
            raise ValueError(f"Expected token '{token_type}', but found '{self.current_token()[0]}' at line {self.current_token()[2]}, column {self.current_token()[3]}")
        self.advance()
