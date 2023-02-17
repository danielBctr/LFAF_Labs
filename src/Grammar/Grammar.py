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

