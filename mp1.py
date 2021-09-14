"""
Alison Major
September 11, 2021
Artificial Intelligence 1 – CPSC 57100
Fall Semester 2021
Machine Problem 1

Full code and test suite available on GitHub:
https://github.com/amajor/artificial-intelligence-machine-problem-1
"""

import queue
from copy import deepcopy
import numpy as np


class PuzzleState:
    """This program implements A* for solving a sliding tile puzzle"""
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self, conf, g, predecessor_state):
        self.puzzle = conf  # Configuration of the state
        self.g_cost = g  # Path cost
        self._compute_heuristic_cost()  # Set heuristic cost
        self.f_cost = self.g_cost + self.heuristic_cost  # Frontier node cost
        self.predecessor = predecessor_state  # Predecessor state
        self.zero_location = np.argwhere(self.puzzle == 0)[0]
        self.action_from_predecessor = None

    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__()

    def _compute_heuristic_cost(self):
        """ Updates the heuristic function value for use in A*
            using the Manhattan Distance Heuristic. """
        heuristic_value = 0
        tile_value = 0
        while tile_value < 9:
            # Determine current position of this number tile.
            current_position = np.argwhere(self.puzzle == tile_value)[0]

            # Determine desired position of this number tile.
            desired_position = np.argwhere(self.SOLVED_PUZZLE == tile_value)[0]

            # Calculate how many rows and columns the tile is from its desired position.
            row_distance = abs(current_position[0] - desired_position[0])
            col_distance = abs(current_position[1] - desired_position[1])

            # Calculate heuristic value for this tile and add to total.
            heuristic_value = heuristic_value + row_distance + col_distance

            # Move to next numeric tile.
            tile_value += 1

        # Set the current heuristic value.
        self.heuristic_cost = heuristic_value

    def is_goal(self):
        """ Checks to see if current state puzzle matches the goal state puzzle. """
        return np.array_equal(PuzzleState.SOLVED_PUZZLE, self.puzzle)

    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def __str__(self):
        return str(self.puzzle)

    move = 0

    def show_path(self):
        """ Shows the path by printing each chosen state that leads to the goal. """
        if self.predecessor is not None:
            self.predecessor.show_path()

        if PuzzleState.move == 0:
            print('START')
        else:
            print('Move', PuzzleState.move, 'ACTION:', self.action_from_predecessor)
        PuzzleState.move = PuzzleState.move + 1
        print(self)

    def can_move(self, direction):
        """ Determines if the blank tile can move in a particular direction. """
        row = self.zero_location[0]
        col = self.zero_location[1]

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
        """ Generates the next state for the puzzle after moving blank in specified direction. """
        # Find the current zero-location (blank space).
        zero_row = self.zero_location[0]
        zero_col = self.zero_location[1]

        # Store the zero location values for our swap tile calculations.
        swap_row = zero_row
        swap_col = zero_col

        # Find the value in the appropriate direction.
        if direction == 'up':
            swap_row -= 1
        if direction == 'down':
            swap_row += 1
        if direction == 'left':
            swap_col -= 1
        if direction == 'right':
            swap_col += 1

        # Move the zero-location in the direction specified,
        # swapping with the number in the location it moves to.
        new_puzzle = deepcopy(self.puzzle)
        new_puzzle[zero_row, zero_col], new_puzzle[swap_row, swap_col] = (
            new_puzzle[swap_row, swap_col], new_puzzle[zero_row, zero_col]
        )

        # Create the new state.
        path_cost = self.g_cost + 1
        predecessor_state = self
        next_state = PuzzleState(new_puzzle, path_cost, predecessor_state)

        # Set the predecessor's direction being moved.
        next_state.action_from_predecessor = direction

        return next_state


def main():
    """ Runs the main program. """
    print('Artificial Intelligence')
    print('MP1: A* for Sliding Puzzle')
    print('SEMESTER: FALL 2021, TERM 1')
    print('NAME: ALISON MAJOR')
    print()

    # load random start state onto frontier priority queue
    frontier = queue.PriorityQueue()
    puzzle_array = np.loadtxt('./samples/mp1input1.txt', dtype=np.int32)
    start_state = PuzzleState(puzzle_array, 0, None)

    frontier.put(start_state)

    closed_set = set()

    num_states = 0
    while not frontier.empty():
        #  Choose state at front of priority queue.
        next_state = frontier.get()
        num_states = num_states + 1

        #  If puzzle matches goal, then quit and return path.
        if next_state.is_goal():
            next_state.show_path()
            break

        # Add state chosen for expansion to closed_set.
        closed_set.add(next_state)

        # Expand state (up to 4 moves possible).
        possible_moves = ['up', 'down', 'left', 'right']
        for move in possible_moves:
            if next_state.can_move(move):
                neighbor = next_state.gen_next_state(move)
                if neighbor in closed_set:
                    # If it's already in the frontier,
                    # it's guaranteed to have lower cost,
                    # so no need to update.
                    continue
                if neighbor not in frontier.queue:
                    frontier.put(neighbor)

    # Number of states visited is inaccurate;
    # more states were visited to calculate the moves.
    # However, the example printout shows count for
    # number of MOVES (not number of states).
    print('\nNumber of states visited =', num_states)


if __name__ == "__main__":
    main()
