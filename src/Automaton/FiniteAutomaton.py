class FiniteAutomaton:
    def __init__(self, transitions):
        self.states = set()
        self.alphabet = set()
        self.transitions = transitions
        self.first_state = None
        self.true_state = set()

    def get_transitions(self):
        return '\n'.join(str(t) for t in self.transitions) + ':\n'

    def check_word(self, word):
        state = self.first_state[0]
        for i in word:
            state = next((t.get_next_state() for t in self.transitions if
                          t.get_current_state() == state and t.get_transition_label() == i), None)
            if state is None:
                return False
        return str(state) in self.true_state

    def get_states(self):
        return self.states

    def put_states(self, states):
        self.states = states

    def get_alphabet(self):
        return self.alphabet

    def put_alphabet(self, alphabet):
        self.alphabet = alphabet

    def get_first_state(self):
        return self.first_state

    def put_first_state(self, startState):
        self.first_state = startState

    def get_accept_states(self):
        return self.true_state

    def put_accept_states(self, acceptStates):
        self.true_state = acceptStates



