"""
Alison Major
September 11, 2021
Artificial Intelligence 1 – CPSC 57100
Fall Semester 2021
Machine Problem 1
"""

import queue
import numpy as np


class PuzzleState:
    """This program implements A* for solving a sliding tile puzzle"""
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self, conf, g, pred_state):
        self.puzzle = conf  # Configuration of the state
        self.gcost = g  # Path cost
        self._compute_heuristic_cost()  # Set heuristic cost
        self.fcost = self.gcost + self.hcost
        self.pred = pred_state  # Predecessor state
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None

    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__()

    def _compute_heuristic_cost(self):
        """ TODO: Actually calculate this! """
        # """ Updates the heuristic function value for use in A* """
        self.hcost = 5

    def is_goal(self):
        """ Checks to see if current state puzzle matches the goal state puzzle. """
        return np.array_equal(PuzzleState.SOLVED_PUZZLE, self.puzzle)

    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)

    def __lt__(self, other):
        return self.fcost < other.fcost

    def __str__(self):
        return np.str(self.puzzle)

    move = 0

    def show_path(self):
        """ Shows the path by printing each chosen state that leads to the goal. """
        if self.pred is not None:
            self.pred.show_path()

        if PuzzleState.move == 0:
            print('START')
        else:
            print('Move', PuzzleState.move, 'ACTION:', self.action_from_pred)
        PuzzleState.move = PuzzleState.move + 1
        print(self)

    def can_move(self, direction):
        """ Determines if the blank tile can move in a particular direction. """
        row = self.zeroloc[0]
        col = self.zeroloc[1]

        if direction == 'up' and row != 0:
            return True
        if direction == 'down' and row != 2:
            return True
        if direction == 'left' and col != 0:
            return True
        if direction == 'right' and col != 2:
            return True
        return False

    def gen_next_state(self, direction):
        """ TODO """
        print('puzzle: ', self.puzzle)
        print(direction)
        print('puzzle: ', self.puzzle)

        # conf = the new array
        # g = self.gcost
        # pred_state = self
        # next_state = PuzzleState(conf, g, pred_state)

        return self.puzzle


def main():
    """ Runs the main program. """
    print('Artificial Intelligence')
    print('MP1: A* for Sliding Puzzle')
    print('SEMESTER: FALL 2021, TERM 1')
    print('NAME: ALISON MAJOR')
    print()

    # load random start state onto frontier priority queue
    frontier = queue.PriorityQueue()
    active_state = np.loadtxt('./samples/mp1input1.txt', dtype=np.int32)
    start_state = PuzzleState(active_state, 0, None)

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
                # If it's already in the frontier, it's guaranteed to have lower cost,
                # so no need to update.

    print('\nNumber of states visited =', num_states)


if __name__ == "__main__":
    main()
