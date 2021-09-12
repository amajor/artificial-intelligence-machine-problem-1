""" The unit tests for the PuzzleState class. """
import unittest
import numpy.testing

from mp1 import PuzzleState


class TestPuzzleState(unittest.TestCase):
    """ Will run tests against modules and functions in the PuzzleState class. """
    def test_solved_puzzle_value(self):
        # pylint: disable=no-self-use
        """ Tests is the SOLVED_PUZZLE value matches the desired state. """
        desired = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]]
        actual = PuzzleState.SOLVED_PUZZLE
        numpy.testing.assert_allclose(desired, actual)

    def test_compute_heuristic_cost(self):
        """ TODO """

    def test_is_goal(self):
        """ TODO """

    def test_show_path(self):
        """ TODO """

    def test_can_move(self):
        """ TODO """

    def test_gen_next_state(self):
        """ TODO """

if __name__ == '__main__':
    unittest.main()
