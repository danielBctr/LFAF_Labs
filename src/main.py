from Grammar.Grammar import Grammar
from src.Automaton.FiniteAutomaton import FiniteAutomaton


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



