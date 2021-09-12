"""
Alison Major
September 11, 2021
Artificial Intelligence 1 – CPSC 57100
Fall Semester 2021

Machine Problem 1
This program implements A* for solving a sliding tile puzzle
"""

import numpy as np
import queue


class PuzzleState:
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self, conf, g, predState):
        self.hcost = None
        self.puzzle = conf  # Configuration of the state
        self.gcost = g  # Path cost
        self._compute_heuristic_cost()  # Set heuristic cost
        self.fcost = self.gcost + self.hcost
        self.pred = predState  # Predecessor state
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None

    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__()

    def _compute_heuristic_cost(self):
        """ Updates the heuristic function value for use in A* """

    def is_goal(self):
        return np.array_equal(PuzzleState.SOLVED_PUZZLE, self.puzzle)

    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)

    def __lt__(self, other):
        return self.fcost < other.fcost

    def __str__(self):
        return np.str(self.puzzle)

    move = 0

    def show_path(self):
        if self.pred is not None:
            self.pred.show_path()

        if PuzzleState.move == 0:
            print('START')
        else:
            print('Move', PuzzleState.move, 'ACTION:', self.action_from_pred)
        PuzzleState.move = PuzzleState.move + 1
        print(self)

    def can_move(self, direction):
        """ TODO """
        if direction == 'up':
            print('Can I move up?')

        if direction == 'down':
            print('Can I move down?')

        if direction == 'left':
            print('Can I move left?')

        if direction == 'right':
            print('Can I move right?')

        """ We cannot move in any direction. """
        return False

    def gen_next_state(self, direction):
        """ TODO """


def main():
    print('Artificial Intelligence')
    print('MP1: A* for Sliding Puzzle')
    print('SEMESTER: FALL 2021, TERM 1')
    print('NAME: ALISON MAJOR')
    print()

    # load random start state onto frontier priority queue
    frontier = queue.PriorityQueue()
    a = np.loadtxt('mp1input1.txt', dtype=np.int32)
    start_state = PuzzleState(a, 0, None)

    frontier.put(start_state)

    closed_set = set()

    num_states = 0
    while not frontier.empty():
        #  choose state at front of priority queue
        next_state = frontier.get()
        num_states = num_states + 1

        #  if goal then quit and return path
        if next_state.is_goal():
            next_state.show_path()
            break

        # Add state chosen for expansion to closed_set
        closed_set.add(next_state)

        # Expand state (up to 4 moves possible)
        possible_moves = ['up', 'down', 'left', 'right']
        for move in possible_moves:
            if next_state.can_move(move):
                neighbor = next_state.gen_next_state(move)
                if neighbor in closed_set:
                    continue
                if neighbor not in frontier.queue:
                    frontier.put(neighbor)
                # If it's already in the frontier, it's guaranteed to have lower cost, so no need to update

    print('\nNumber of states visited =', num_states)


if __name__ == "__main__":
    main()
