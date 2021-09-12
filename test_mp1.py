import unittest
import numpy.testing

from mp1 import PuzzleState


class TestPuzzleState(unittest.TestCase):
    def test_SOLVED_PUZZLE_value(self):
        desired = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]]
        actual = PuzzleState.SOLVED_PUZZLE
        numpy.testing.assert_allclose(desired, actual)


if __name__ == '__main__':
    unittest.main()
