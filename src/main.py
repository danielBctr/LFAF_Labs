from src.Lexer.lexer import Lexer
from src.Lexer.token import Token
from src.Parser.Parser import Parser

# Lab 3

print("-------------------------------Lab4-----------------------------------")
# String 1:
'''
input_string = 'x = 3.14 * (y - 2);'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

print("\n\tString 1 : \n" + input_string + "\n" + "\nTokens:")
for token in tokens:
    print(token)
# String 2:
input_string = 'y = "hello, world" != "goodbye" && true || null;'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

print("\n\tString 2 : \n" + input_string + "\n" + "\nTokens:")
for token in tokens:
    print(token)
# String 3:
input_string = 'z = 10 * (3 + 4) % 5 || false;'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

print("\n\tString 3 : \n" + input_string + "\n" + "\nTokens:")
for token in tokens:
    print(token)
# String 4:
input_string = 'c,b =(a != 0 || a == !b):;'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

print("\n\tString 4 : \n" + input_string + "\n" + "\nTokens:")
for token in tokens:
    print(token)
# String 5:
input_string = 'for(a && b): {return false}; if: !a else:b; while(!true)'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

print("\n\tString 5 : \n" + input_string + "\n" + "\nTokens:")
for token in tokens:
    print(token)
'''

# Expression #1
print("Expression 1")
input_string = '(x - 2) / 1 + 2 / 3'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

parser = Parser(tokens)
ast = parser.parse()
print(ast)

print("Expression 2")
input_string = 'if 2 == 0: 2 else: 2 * 1'
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

parser = Parser(tokens)
ast = parser.parse()
print(ast)
print("Expression 3")
input_string = "if x > 5: result = 1"
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

parser = Parser(tokens)
ast = parser.parse()
print(ast)
print("Expression 4")
input_string = "x = 10 + 5 * (2 - 1); y = x > 10"
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

parser = Parser(tokens)
ast = parser.parse()
print(ast)

print("Expression 5")
input_string = "if x = true: x = 1 else: y = false"
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

parser = Parser(tokens)
ast = parser.parse()
print(ast)

print("Expression 6")
input_string = "if !x && y || x && !y = true: x = 1"
lexer = Lexer(input_string, Token.token_exprs)
tokens = lexer.lex()

parser = Parser(tokens)
ast = parser.parse()
print(ast)
