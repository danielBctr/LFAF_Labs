from src.Automaton.FiniteAutomaton import FiniteAutomaton
from src.Automaton.Transitions import Transitions
import random
from typing import List, Dict

class Grammar:

    def __init__(self, start_symbol: str, terminals: List[str], non_terminals: List[str],
                 productions: Dict[str, List[str]]):
        self.start_symbol = start_symbol
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.productions = productions

    def word_generator(self, character: str = None) -> str:
        if character is None:
            character = self.start_symbol
        if character in self.terminals:
            return character
        right_sides = self.productions[character]
        random_right_side = random.choice(right_sides)
        word = ''
        for right_char in random_right_side:
            word += self.word_generator(right_char)
        return word

    def classify_grammar(self):
        for nonTerminal in self.non_terminals:
            for production in self.productions[nonTerminal]:
                if len(production) > 2 or not (
                        production[0] in self.terminals or production[0] in self.non_terminals) or (
                        len(production) == 2 and production[1] not in self.non_terminals):
                    return 'Type 2'
        for nonTerminal in self.non_terminals:
            if nonTerminal != self.start_symbol:
                if len(self.productions[nonTerminal]) > 1 or not (
                        len(self.productions[nonTerminal][0]) == 1 and (
                        self.productions[nonTerminal][0][0] in self.terminals or self.productions[nonTerminal][0][
                    0] in self.non_terminals)):
                    return 'Type 3'
        for nonTerminal in self.non_terminals:
            for production in self.productions[nonTerminal]:
                for symbol in production:
                    if symbol not in self.terminals and symbol not in self.start_symbol:
                        return 'Type 0'
        return 'Type 1'

    def to_cnf(self):
        transformations = [
            ("epsilon", self.remove_epsilon),
            ("unit", self.remove_unit),
            ("inaccessible", self.remove_inaccessible_symbols),
            ("non-productive", self.remove_non_productive_symbols),
        ]
        for name, transformation in transformations:
            transformation()
            print(f"\n\tRemoving {name} productions:\n"
                  f"Vn(Non-terminal): {self.non_terminals}\n"
                  f"P(Productions): {self.productions}")
        return self.productions, self.terminals, self.non_terminals

    def remove_epsilon(self):
        epsilon = set(variable for variable, productions in self.productions.items() if "ε" in productions)
        for left, right in self.productions.items():
            for i in right:
                for j in epsilon:
                    if j in i and left != j:
                        self.productions[left] = [x.replace(j, "") for x in self.productions[left]]
                        self.productions[left].append(i)
                    elif i == "ε":
                        self.productions[left].remove(i)
        return self.productions

    def remove_unit(self):
        self.productions = {
            left: [r for rhs in right for r in (self.productions[rhs] if rhs in self.productions else [rhs])]
            for left, right in self.productions.items()
        }
        if any(len(right) == 1 and right[0] in self.non_terminals for right in self.productions.values()):
            self.remove_unit()
        return self.productions

    def remove_inaccessible_symbols(self):
        accessible = set(w for right in self.productions.values() for r in right for w in r)

        self.productions = {
            left: right for left, right in self.productions.items() if left in accessible
        }

        self.non_terminals = [a for a in self.non_terminals if a in accessible]
        return self.productions

    def remove_non_productive_symbols(self):
        productive = set(left for left, right in self.productions.items() if any(r in self.terminals for r in right))
        self.productions = {
            left: [
                "".join(w for w in r if w in self.terminals or w in productive)
                for r in right if len(r) == 1 or any(w in productive for w in r)
            ]
            for left, right in self.productions.items() if left in productive
        }
        self.non_terminals = [a for a in self.non_terminals if a in productive]
        return self.productions

    """
        def to_finite_automaton(self):
            states = set(self.non_terminals) | {''}
            final_states = {''}
            transitions = [Transitions(non_terminal, right_side[1] if len(right_side) > 1 else '', right_side[0]) for
                           non_terminal in self.non_terminals for right_side in self.productions[non_terminal]]
            automaton = FiniteAutomaton(transitions)
            automaton.put_states(states)
            automaton.put_first_state(str(self.start_symbol))
            automaton.put_accept_states(final_states)
            automaton.put_alphabet(self.terminals)
            return automaton
    """
