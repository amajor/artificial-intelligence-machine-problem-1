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
        """ Tests is the SOLVED_PUZZLE value matches the desired state. """
        desired = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]]
        actual = self._puzzle_state.SOLVED_PUZZLE
        numpy.testing.assert_allclose(desired, actual)

    def test_compute_heuristic_cost(self):
        """ TODO """
        self.skipTest('Test not yet created')

    @parameterized.expand([
        ("should be exact match", [[0, 1, 2], [3, 4, 5], [6, 7, 8]], True),
        ("should not match", [[8, 6, 7], [2, 0, 1], [3, 4, 5]], False)
    ])
    def test_is_goal(self, _test_name, puzzle, expected):
        """ Tests that we return True for goal match and False for not matched. """
        self._puzzle_state.puzzle = puzzle
        actual = self._puzzle_state.is_goal()
        self.assertEqual(expected, actual)

    def test_show_path(self):
        """ TODO: is it worth testing the printed output? """
        self.skipTest('Test not yet created')

    @parameterized.expand([
        ("position [0 0] cannot move up", [[0, 1, 2], [3, 4, 5], [6, 7, 8]],  False),
        ("position [0 1] cannot move up", [[1, 0, 2], [3, 4, 5], [6, 7, 8]], False),
        ("position [0 2] cannot move up", [[1, 2, 0], [3, 4, 5], [6, 7, 8]], False),
        ("position [1 0] can move up", [[1, 2, 3], [0, 4, 5], [6, 7, 8]], True),
        ("position [1 1] can move up", [[1, 2, 3], [4, 0, 5], [6, 7, 8]], True),
        ("position [1 2] can move up", [[1, 2, 3], [4, 5, 0], [6, 7, 8]], True),
        ("position [2 0] can move up", [[1, 2, 3], [4, 5, 6], [0, 7, 8]], True),
        ("position [2 1] can move up", [[1, 2, 3], [4, 5, 6], [7, 0, 8]], True),
        ("position [2 2] can move up", [[1, 2, 3], [4, 5, 6], [7, 8, 0]], True)
    ])
    def test_can_move_up(self, _test_name, puzzle, expected):
        """ Tests whether the blank space can move UP """
        test_state = np.asarray(puzzle, dtype=np.int32)
        self._puzzle_state = PuzzleState(test_state, 0, None)
        actual = self._puzzle_state.can_move('up')
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ("position 1 can move down", [[0, 1, 2], [3, 4, 5], [6, 7, 8]], True),
        ("position 2 can move down", [[1, 0, 2], [3, 4, 5], [6, 7, 8]], True),
        ("position 3 can move down", [[1, 2, 0], [3, 4, 5], [6, 7, 8]], True),
        ("position 4 can move down", [[1, 2, 3], [0, 4, 5], [6, 7, 8]], True),
        ("position 5 can move down", [[1, 2, 3], [4, 0, 5], [6, 7, 8]], True),
        ("position 6 can move down", [[1, 2, 3], [4, 5, 0], [6, 7, 8]], True),
        ("position 7 cannot move down", [[1, 2, 3], [4, 5, 6], [0, 7, 8]], False),
        ("position 8 cannot move down", [[1, 2, 3], [4, 5, 6], [7, 0, 8]], False),
        ("position 9 cannot move down", [[1, 2, 3], [4, 5, 6], [7, 8, 0]], False)
    ])
    def test_can_move_down(self, _test_name, puzzle, expected):
        """ Tests whether the blank space can move DOWN """
        test_state = np.asarray(puzzle, dtype=np.int32)
        self._puzzle_state = PuzzleState(test_state, 0, None)
        actual = self._puzzle_state.can_move('down')
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ("position 1 cannot move left", [[0, 1, 2], [3, 4, 5], [6, 7, 8]], False),
        ("position 2 can move left", [[1, 0, 2], [3, 4, 5], [6, 7, 8]],  True),
        ("position 3 can move left", [[1, 2, 0], [3, 4, 5], [6, 7, 8]],  True),
        ("position 4 cannot move left", [[1, 2, 3], [0, 4, 5], [6, 7, 8]], False),
        ("position 5 can move left", [[1, 2, 3], [4, 0, 5], [6, 7, 8]], True),
        ("position 6 can move left", [[1, 2, 3], [4, 5, 0], [6, 7, 8]], True),
        ("position 7 cannot move left", [[1, 2, 3], [4, 5, 6], [0, 7, 8]], False),
        ("position 8 can move left", [[1, 2, 3], [4, 5, 6], [7, 0, 8]], True),
        ("position 9 can move left", [[1, 2, 3], [4, 5, 6], [7, 8, 0]], True)
    ])
    def test_can_move_left(self, _test_name, puzzle, expected):
        """ Tests whether the blank space can move in LEFT """
        test_state = np.asarray(puzzle, dtype=np.int32)
        self._puzzle_state = PuzzleState(test_state, 0, None)
        actual = self._puzzle_state.can_move('left')
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ("position 1 can move right", [[0, 1, 2], [3, 4, 5], [6, 7, 8]], True),
        ("position 2 can move right", [[1, 0, 2], [3, 4, 5], [6, 7, 8]], True),
        ("position 3 cannot move right", [[1, 2, 0], [3, 4, 5], [6, 7, 8]], False),
        ("position 4 can move right", [[1, 2, 3], [0, 4, 5], [6, 7, 8]], True),
        ("position 5 can move right", [[1, 2, 3], [4, 0, 5], [6, 7, 8]], True),
        ("position 6 cannot move right", [[1, 2, 3], [4, 5, 0], [6, 7, 8]], False),
        ("position 7 can move right", [[1, 2, 3], [4, 5, 6], [0, 7, 8]], True),
        ("position 8 can move right", [[1, 2, 3], [4, 5, 6], [7, 0, 8]], True),
        ("position 9 cannot move right", [[1, 2, 3], [4, 5, 6], [7, 8, 0]], False)
    ])
    def test_can_move_right(self, _test_name, puzzle, expected):
        """ Tests whether the blank space can move RIGHT """
        test_state = np.asarray(puzzle, dtype=np.int32)
        self._puzzle_state = PuzzleState(test_state, 0, None)
        actual = self._puzzle_state.can_move('right')
        self.assertEqual(expected, actual)

    @parameterized.expand([
        (
            "blank moves up and swaps with 2",
            'right',
            [[1, 2, 3], [4, 0, 5], [6, 7, 8]],
            [[1, 0, 3], [4, 2, 5], [6, 7, 8]]
        ), (
            "blank moves down and swaps with 7",
            'right',
            [[1, 2, 3], [4, 0, 5], [6, 7, 8]],
            [[1, 2, 3], [4, 7, 5], [6, 0, 8]]
        ), (
            "blank moves left and swaps with 4",
            'right',
            [[1, 2, 3], [4, 0, 5], [6, 7, 8]],
            [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        ), (
            "blank moves right and swaps with 5",
            'right',
            [[1, 2, 3], [4, 0, 5], [6, 7, 8]],
            [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        )
    ])
    def test_gen_next_state(self, _test_name, direction, current_puzzle, desired_puzzle):
        """ Test that the next state is generated when given a direction """
        self.skipTest('Test not yet created')
        self._puzzle_state.puzzle = current_puzzle
        self._puzzle_state.gen_next_state(direction)
        actual = self._puzzle_state.puzzle
        print('++++++++++++++++++++++++++++++++++++++')
        print('current_state: ', current_puzzle)
        print('--------------------------------------')
        print('actual:        ', actual)
        print('--------------------------------------')
        print('desired:       ', desired_puzzle)
        print('++++++++++++++++++++++++++++++++++++++')
        numpy.testing.assert_allclose(desired_puzzle, actual)


if __name__ == '__main__':
    unittest.main()
