import unittest
import sudoku_engine as se

class SudokuTestBoard(unittest.TestCase):
    def test_first_box_skipempty(self):
        sudoku = se.SudokuBoard("1ee000000/24e000000/eee000000/4e9000000/7e1000000/526000000/e12000000/eee000000/6ee000000")
        result = sudoku.box(1, showoption=se.ItemsShowOption.SkipEmpty)
        expected = [
            {'val': '1', 'row': 1, 'col': 1, 'box': 1},
            {'val': '2', 'row': 2, 'col': 1, 'box': 1},
            {'val': '4', 'row': 2, 'col': 2, 'box': 1}
        ]
        self.assertEqual(expected, result)


    def test_first_box_emptyonly(self):
        sudoku = se.SudokuBoard("1ee000000/24e000000/eee000000/4e9000000/7e1000000/526000000/e12000000/eee000000/6ee000000")
        result = sudoku.box(1, showoption=se.ItemsShowOption.EmptyOnly)
        expected = [
            {'val': 'e', 'row': 1, 'col': 2, 'box': 1},
            {'val': 'e', 'row': 1, 'col': 3, 'box': 1},
            {'val': 'e', 'row': 2, 'col': 3, 'box': 1},
            {'val': 'e', 'row': 3, 'col': 1, 'box': 1},
            {'val': 'e', 'row': 3, 'col': 2, 'box': 1},
            {'val': 'e', 'row': 3, 'col': 3, 'box': 1}
        ]
        self.assertEqual(expected, result)

    def test_seventh_row(self):
        sudoku = se.SudokuBoard("eeeeeeeee/eeeeeeeee/eeeeeeeee/eeeeeeeee/eeeeeeeee/eeeeeeeee/777777777/eeeeeeeee/eeeeeeeee")
        result = sudoku.row(7)
        expected = [
            {'val': '7', 'row': 7, 'col': 1, 'box': 7},
            {'val': '7', 'row': 7, 'col': 2, 'box': 7},
            {'val': '7', 'row': 7, 'col': 3, 'box': 7},
            {'val': '7', 'row': 7, 'col': 4, 'box': 8},
            {'val': '7', 'row': 7, 'col': 5, 'box': 8},
            {'val': '7', 'row': 7, 'col': 6, 'box': 8},
            {'val': '7', 'row': 7, 'col': 7, 'box': 9},
            {'val': '7', 'row': 7, 'col': 8, 'box': 9},
            {'val': '7', 'row': 7, 'col': 9, 'box': 9},
        ]
        self.assertEqual(expected, result)

    def test_last_column(self):
        sudoku = se.SudokuBoard("eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9/eeeeeeee9")
        result = sudoku.column(9)
        expected = [
            {'val': '9', 'row': 1, 'col': 9, 'box': 3},
            {'val': '9', 'row': 2, 'col': 9, 'box': 3},
            {'val': '9', 'row': 3, 'col': 9, 'box': 3},
            {'val': '9', 'row': 4, 'col': 9, 'box': 6},
            {'val': '9', 'row': 5, 'col': 9, 'box': 6},
            {'val': '9', 'row': 6, 'col': 9, 'box': 6},
            {'val': '9', 'row': 7, 'col': 9, 'box': 9},
            {'val': '9', 'row': 8, 'col': 9, 'box': 9},
            {'val': '9', 'row': 9, 'col': 9, 'box': 9}
        ]
        self.assertEqual(expected, result)

    def test_all_valid_digits(self):
        sudoku = se.SudokuBoard("eeee8eeee/eeeeeeeee/eeeeeeeee/eee1e2eee/6eeeeeee7/eee3e4eee/eeeeeeeee/eeeeeeeee/eeee9eeee")
        result = sudoku.allValidDigits(5, 5)
        expected = [
            {'val': '5', 'row': 5, 'col': 5, 'box': 5}
        ]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()


