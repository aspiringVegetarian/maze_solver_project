import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 15
        num_rows = 7
        m1 = Maze(0, 0, num_rows, num_cols, 0, 0)
        self.assertEqual(
            len(m1._cells),
            num_rows
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )

    def test_maze_opening_closing(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 0, 0)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )
if __name__ == "__main__":
    unittest.main()

