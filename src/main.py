from Grammar.Grammar import Grammar

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

# Generate string
print("The 5 generated strings: ")
for _ in range(5):
    print(grammar.word_generator())

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


