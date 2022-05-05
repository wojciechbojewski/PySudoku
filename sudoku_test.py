import unittest
from  ddt import ddt, data

@ddt
class SudokuTestBoard(unittest.TestCase):

    @data([
            {'val': '1', 'row': 1, 'col': 1, 'box': 1},
            {'val': '2', 'row': 2, 'col': 1, 'box': 1},
            {'val': '4', 'row': 2, 'col': 2, 'box': 1}
        ])
    def test_first_box_skipempty(self, expected):
        from Engine.SudokuBoard import SudokuBoard
        from Engine.ItemsShowOption import ItemsShowOption
        sudoku = SudokuBoard("1ee000000/24e000000/eee000000/4e9000000/7e1000000/526000000/e12000000/eee000000/6ee000000")
        result = sudoku.box(1, showoption=ItemsShowOption.SkipEmpty)
        self.assertEqual(expected, result)


    @data([
            {'val': 'e', 'row': 1, 'col': 2, 'box': 1},
            {'val': 'e', 'row': 1, 'col': 3, 'box': 1},
            {'val': 'e', 'row': 2, 'col': 3, 'box': 1},
            {'val': 'e', 'row': 3, 'col': 1, 'box': 1},
            {'val': 'e', 'row': 3, 'col': 2, 'box': 1},
            {'val': 'e', 'row': 3, 'col': 3, 'box': 1}
        ])
    def test_first_box_emptyonly(self, expected):
        from Engine.SudokuBoard import SudokuBoard
        from Engine.ItemsShowOption import ItemsShowOption
        sudoku = SudokuBoard("1ee000000/24e000000/eee000000/4e9000000/7e1000000/526000000/e12000000/eee000000/6ee000000")
        result = sudoku.box(1, showoption=ItemsShowOption.EmptyOnly)
        self.assertEqual(expected, result)

    @data([
            {'val': '7', 'row': 7, 'col': 1, 'box': 7},
            {'val': '7', 'row': 7, 'col': 2, 'box': 7},
            {'val': '7', 'row': 7, 'col': 3, 'box': 7},
            {'val': '7', 'row': 7, 'col': 4, 'box': 8},
            {'val': '7', 'row': 7, 'col': 5, 'box': 8},
            {'val': '7', 'row': 7, 'col': 6, 'box': 8},
            {'val': '7', 'row': 7, 'col': 7, 'box': 9},
            {'val': '7', 'row': 7, 'col': 8, 'box': 9},
            {'val': '7', 'row': 7, 'col': 9, 'box': 9},
        ])
    def test_seventh_row(self, expected):
        from Engine.SudokuBoard import SudokuBoard
        sudoku = SudokuBoard("eeeeeeeee/eeeeeeeee/eeeeeeeee/eeeeeeeee/eeeeeeeee/eeeeeeeee/777777777/eeeeeeeee/eeeeeeeee")
        result = sudoku.row(7)
        self.assertEqual(expected, result)

    @data([
            {'val': '9', 'row': 1, 'col': 9, 'box': 3},
            {'val': '9', 'row': 2, 'col': 9, 'box': 3},
            {'val': '9', 'row': 3, 'col': 9, 'box': 3},
            {'val': '9', 'row': 4, 'col': 9, 'box': 6},
            {'val': '9', 'row': 5, 'col': 9, 'box': 6},
            {'val': '9', 'row': 6, 'col': 9, 'box': 6},
            {'val': '9', 'row': 7, 'col': 9, 'box': 9},
            {'val': '9', 'row': 8, 'col': 9, 'box': 9},
            {'val': '9', 'row': 9, 'col': 9, 'box': 9}
        ])
    def test_last_column(self, expected):
        from Engine.SudokuBoard import SudokuBoard
        sudoku = SudokuBoard("eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9")
        result = sudoku.column(9)
        self.assertEqual(expected, result)

    @data([
            {'val': '5', 'row': 5, 'col': 5, 'box': 5}
        ])
    def test_all_valid_digits(self, expected):
        from Engine.SudokuBoard import SudokuBoard
        sudoku = SudokuBoard("eeee8eeee/eeeeeeeee/eeeeeeeee/eee1e2eee/6eeeeeee7/eee3e4eee/eeeeeeeee/eeeeeeeee/eeee9eeee")
        result = sudoku.allValidDigits(5, 5)
        self.assertEqual(expected, result)

    @data({'val': '5', 'row': 5, 'col': 5, 'box': 5})
    def test_setDigit_OK_1(self, expected):
        from Engine.SudokuBoard import SudokuBoard
        sudoku = SudokuBoard("eeee8eeee/eeeeeeeee/eeeeeeeee/eee1e2eee/6eeeeeee7/eee3e4eee/eeeeeeeee/eeeeeeeee/eeee9eeee")
        result = sudoku.setDigit(5, 5, 5)
        self.assertEqual(expected, result)

    def test_setDigit_OK_2(self):
        from Engine.SudokuBoard import SudokuBoard
        from Engine.ItemsShowOption import ItemsShowOption
        sudoku = SudokuBoard("eeee8eeee/eeeeeeeee/eeeeeeeee/eee1e2eee/6eeeeeee7/eee3e4eee/eeeeeeeee/eeeeeeeee/eeee9eeee")
        new_digit = sudoku.setDigit(5, 5, 5)
        new_fen = f"eeee8eeee/eeeeeeeee/eeeeeeeee/eee1e2eee/6eee{new_digit['val']}eee7/eee3e4eee/eeeeeeeee/eeeeeeeee/eeee9eeee"
        self.assertEqual(new_fen, sudoku.board_fen)

    def test_setDigit_fail(self):
        from Engine.SudokuBoard import SudokuBoard
        sudoku = SudokuBoard("eeee8eeee/eeeeeeeee/eeeeeeeee/eee1e2eee/6eeeeeee7/eee3e4eee/eeeeeeeee/eeeeeeeee/eeee9eeee")
        with self.assertRaises(ValueError):
            for x in [1,2,3,4,6,7,8,9]:
                sudoku.setDigit(5, 5, x)

if __name__ == '__main__':
    unittest.main()


