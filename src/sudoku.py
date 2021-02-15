SUDOKU_DIMENTION = 9
SUDOKU_BOX_DIMENTION = 3


class InvalidSudokuException(Exception):
    pass


def print_sudoku(sudoku):
    print('**********************************')
    for i in sudoku:
        for j in i:
            print(j, end=" ")
        print("")
    print('**********************************')


def find_position_to_solve(position_to_fill, sudoku):
    for i in range(SUDOKU_DIMENTION):
        for j in range(SUDOKU_DIMENTION):
            if sudoku[i][j] == 0:
                position_to_fill[0] = i
                position_to_fill[1] = j
                return True
    return False


def used_in_row(num, row, column, sudoku):
    for i in range(SUDOKU_DIMENTION):
        if sudoku[row][i] == num:
            return True
    return False


def used_in_column(num, row, column, sudoku):
    for i in range(SUDOKU_DIMENTION):
        if sudoku[i][column] == num:
            return True
    return False


def used_in_box(num, row, column, sudoku):
    for i in range(SUDOKU_BOX_DIMENTION):
        for j in range(SUDOKU_BOX_DIMENTION):
            if sudoku[i + row][j + column] == num:
                return True
    return False


def is_location_valid(num, row, col, sudoku):
    return not used_in_row(num, row, col, sudoku) and not used_in_column(num, row, col, sudoku) and not used_in_box(num, row - row % SUDOKU_BOX_DIMENTION, col - col % SUDOKU_BOX_DIMENTION, sudoku)


def solve_sudoku(sudoku):
    position_to_fill = [0, 0]

    if not find_position_to_solve(position_to_fill, sudoku):
        print('All cells filled, exiting...')
        return True

    row = position_to_fill[0]
    col = position_to_fill[1]

    for i in range(1, SUDOKU_DIMENTION + 1):
        if is_location_valid(i, row, col, sudoku):
            sudoku[row][col] = i

            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0

    return False


def run(sudoku):
    print('Sudoku sudoku - initial state')
    print_sudoku(sudoku)
    if not solve_sudoku(sudoku):
        raise InvalidSudokuException('Sudoku is invalid')
    print('Sudoku sudoku - Final state')
    print_sudoku(sudoku)
    return sudoku


if __name__ == "__main__":
    sudoku = [[0 for j in range(SUDOKU_DIMENTION)]
              for i in range(SUDOKU_DIMENTION)]
    run(sudoku)
