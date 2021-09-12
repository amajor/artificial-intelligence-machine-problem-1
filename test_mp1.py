""" The unit tests for the PuzzleState class. """
import unittest
from parameterized import parameterized
import numpy.testing
import numpy as np

from mp1 import PuzzleState


class TestPuzzleState(unittest.TestCase):
    """ Will run tests against modules and functions in the PuzzleState class. """

    def setUp(self):
        active_state = np.loadtxt('./samples/mp1input1.txt', dtype=np.int32)
        self._puzzle_state = PuzzleState(active_state, 0, None)

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
        self.skipTest('Test not yet created')

    @parameterized.expand([
        ("should be exact match", [[0, 1, 2], [3, 4, 5], [6, 7, 8]], True),
        ("should not match", [[8, 6, 7], [2, 0, 1], [3, 4, 5]], False)
    ])
    def test_is_goal(self, name, puzzle, expected):
        # pylint: disable=unused-argument
        """ Tests that we return True for goal match and False for not matched. """
        self._puzzle_state.puzzle = puzzle
        actual = self._puzzle_state.is_goal()
        self.assertEqual(expected, actual)

    def test_show_path(self):
        """ TODO """
        self.skipTest('Test not yet created')

    def test_can_move(self):
        """ TODO """
        self.skipTest('Test not yet created')

    def test_gen_next_state(self):
        """ TODO """
        self.skipTest('Test not yet created')


if __name__ == '__main__':
    unittest.main()
