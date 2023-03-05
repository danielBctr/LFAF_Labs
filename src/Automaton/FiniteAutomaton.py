import networkx as nx
import matplotlib.pyplot as plt
class FiniteAutomaton:
    def __init__(self, states:set, alphabet: list, transitions:list, first_state, final_state: set):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.first_state = first_state
        self.final_state = final_state

    def get_transitions(self):
        return '\n'.join(str(t) for t in self.transitions) + ':\n'

    def check_word(self, word):
        state = self.first_state[0]
        for i in word:
            state = next((t.get_next_state() for t in self.transitions if
                          t.get_current_state() == state and t.get_transition_label() == i), None)
            if state is None:
                return False
        return str(state) in self.final_state

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
        return self.final_state

    def put_accept_states(self, acceptStates):
        self.final_state = acceptStates

    def convert_to_grammar(self, Grammar):

        productions = {state: [] for state in self.states}
        start_symbol = self.first_state + "'"
        productions[start_symbol] = [self.first_state]
        for accept_state in self.final_state:
            productions[accept_state].append("ε")
        for q, a, p in self.transitions:
            productions[q].append(a + p)
        non_terminals = list(self.states) + [start_symbol]
        terminals = self.alphabet

        return Grammar(start_symbol, terminals, non_terminals, productions)

    def is_deterministic(self):

        transitions = {}
        for transition in self.transitions:
            if transition[0] in transitions:
                if transition[1] in transitions[transition[0]]:
                    return "Nope is not"
                else:
                    transitions[transition[0]].append(transition[1])
            else:
                transitions[transition[0]] = [transition[1]]
        return "Yes, it is"

    def convert_to_dfa(self):
        dfa_states, dfa_alphabet, dfa_transitions, dfa_acceptStates = set(), self.alphabet, [], set()
        dfa_startState = frozenset(self.epsilon_closure({self.first_state}, self.transitions))
        queue, processed_states = [dfa_startState], set()

        while queue:
            state_set = queue.pop(0)
            if state_set in processed_states:
                continue
            processed_states.add(state_set)

            dfa_states.add(state_set)

            for accept_state in self.final_state:
                if accept_state in state_set:
                    dfa_acceptStates.add(state_set)
                    break

            for symbol in dfa_alphabet:
                next_states = self.epsilon_closure(self.move(state_set, symbol, self.transitions), self.transitions)
                if next_states:
                    dfa_transitions.append((state_set, symbol, frozenset(next_states)))
                    if frozenset(next_states) not in processed_states:
                        queue.append(frozenset(next_states))

        return FiniteAutomaton(states=dfa_states, alphabet=dfa_alphabet, transitions=dfa_transitions,
                               first_state=dfa_startState, final_state=dfa_acceptStates)

    def epsilon_closure(self, states, transitions):
        e_closure = set(states)
        queue = list(states)
        while queue:
            state = queue.pop(0)
            next_states = [transition[2] for transition in transitions if
                           transition[0] == state and transition[1] == 'ε']
            new_states = set(next_states) - e_closure
            e_closure |= new_states
            queue.extend(new_states)
        return e_closure

    def move(self, states, symbol, transitions):
        return {transition[2] for state in states for transition in transitions if
                transition[0] == state and transition[1] == symbol}

    def draw(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.states)
        G.add_edges_from([(t[0], t[2], {'label': t[1]}) for t in self.transitions])
        pos = nx.circular_layout(G)
        node_color = '#66c2a5'
        node_size = 2000
        font_size = 20
        font_family = 'sans-serif'
        edge_color = '#8da0cb'
        edge_width = 2
        arrow_size = 30
        fig, ax = plt.subplots(figsize=(10, 10))
        nx.draw_networkx_nodes(G, pos, node_size=node_size, alpha=0.8, node_color=node_color)
        nx.draw_networkx_labels(G, pos, font_size=font_size, font_family=font_family, font_weight='bold')
        edge_labels = {(e[0], e[1]): e[2]['label'] for e in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=font_size, font_family=font_family)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrows=True, arrowsize=arrow_size, width=edge_width,
                               edge_color=edge_color)
        ax.set_axis_off()
        plt.show()














