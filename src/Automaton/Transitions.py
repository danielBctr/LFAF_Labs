class Transitions:
    def __init__(self, current_state, next_state, transition_label):
        self.current_state, self.next_state, self.transition_label = current_state, next_state, transition_label

    def __str__(self):
        return str(self.next_state)

    def get_current_state(self): return self.current_state
    def get_next_state(self): return self.next_state
    def get_transition_label(self): return self.transition_label

