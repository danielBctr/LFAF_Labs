from Grammar.Grammar import Grammar
from src.Automaton.FiniteAutomaton import FiniteAutomaton
from src.Lexer.lexer import Lexer
from src.Lexer.token import Token

# Implementation of my grammar
grammar = Grammar(
    start_symbol='S',
    terminals=['a', 'b','c','d'],
    non_terminals=['S', 'F', 'L'],
    productions={
        'S': ["bS", "aF", "d"],
        'F': ["cF", "dF", "aL", "b"],
        'L': ["aL", "c"]
    }
)
print("----------------------Lab1----------------------------")
# Generate string
print("The 5 generated strings: ")
for _ in range(5):
    print(grammar.word_generator())
"""
print("")
# convert to finite automaton
fa = grammar.to_finite_automaton()
print(fa.get_states())
print(fa.get_alphabet())
print(fa.get_transitions())
print(fa.get_first_state())
print(fa.get_accept_states())

print("")
# Valid or Not
words = ["bcd", "dbcc", "aab", "bbaac", "abcd", "bacdb", "bbbbadcddb"]
for word in words:
    if fa.check_word(word):
        print(f"{word} is valid")
    else:
        print(f"No, {word} is not valid")
"""
print("\n---------------------Lab2-----------------------------------")
# Tasks 2
grammarType = grammar.classify_grammar()
print("\tTask 2-> Grammar Type: \n", grammarType)

# Task 3 a
fa2 = FiniteAutomaton(states={'q0', 'q1', 'q2', 'q3'},
                          alphabet=['a', 'b'],
                          transitions=[
                              ('q0', 'a', 'q1'),
                              ('q0', 'b', 'q0'),
                              ('q1', 'a', 'q2'),
                              ('q1', 'a', 'q3'),
                              ('q2', 'a', 'q3'),
                              ('q2', 'b', 'q0')
                          ],
                          first_state='q0',
                          final_state={'q3'})

gr = fa2.convert_to_grammar(Grammar)
print("\n\tTask 3.a-> FA to RG")
print(f"FA:\nAlphabet: {fa2.get_alphabet()}\nStates: {fa2.get_states()}\nInitial state: {fa2.get_first_state()}\nFinal states: {fa2.get_accept_states()}\nTransitions: {fa2.get_transitions()}")
print(f"\nRG:\nnon-terminal: {gr.non_terminals}\nTerminal: {gr.terminals}\nStart character: {gr.start_symbol}\nProductions: {gr.productions}")

#Task 3 b
print("\n\tTask 3.b-> is Deterministic? : \n", fa2.is_deterministic())

#Task 3 c

dfa = fa2.convert_to_dfa()

print("\n\tTask 3.c-> The DFA: ")
print("Alphabet: ", dfa.get_alphabet())
print("States: ", dfa.get_states())
print("Initial state: ", dfa.get_first_state())
print("Final states: ", dfa.get_accept_states())
print("Transitions: ", dfa.get_transitions())

print("Is the converted DFA Deterministic? : \n", dfa.is_deterministic())

# Task 3 d
print("\n\t Task 3.d-> Drawing the Graph...")
fa2.draw()

# Lab 3

print("-------------------------------Lab3-----------------------------------")
# String 1:
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

# Lab 4

print("-------------------------------Lab4-----------------------------------")

starting_symbol = 'S'
non_terminals = ['S', 'A', 'B', 'C', 'D']
terminals = ['a', 'b', 'd']
productions = {'S': ['dB', 'A'],
                'A': ['d', 'dS', 'aBdB'],
                'B': ['a', 'aS', 'AC'],
                'D': ['AB'],
                'C': ['bC', 'ε']
                }

grammar = Grammar(starting_symbol , terminals, non_terminals, productions)

print(f"\tInitial Grammar:\nVt(Terminal): {grammar.terminals}\nVn(Non-terminal): {grammar.non_terminals}\nP(Productions): {grammar.productions}")
grammar.to_cnf()
print(f"\n\tCNF(Chomsky Normal Form):\nVt(Terminal): {grammar.terminals}\nVn(Non-terminal): {grammar.non_terminals}\nP(Productions): {grammar.productions}")



