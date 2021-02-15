def print_sudoku(sudoku):
    print('**********************************')
    for i in sudoku:
        for j in i:
            print(j, end=" ")
        print("")
    print('**********************************')


def find_position_to_solve(position_to_fill, sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                position_to_fill[0] = i
                position_to_fill[1] = j
                return True
    return False


def is_location_valid(num, row, col, sudoku):

    num_in_row = False
    num_in_column = False
    num_in_box = False

    for i in range(9):
        if sudoku[row][i] == num:
            num_in_row = True

    for i in range(9):
        if sudoku[i][col] == num:
            num_in_column = True

    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + box_row][j + box_col] == num:
                num_in_box = True

    if (not num_in_row and not num_in_column and not num_in_box):
        sudoku[row][col] = num
        return True
    return False


def solve_sudoku(sudoku):
    position_to_fill = [0, 0]

    if not find_position_to_solve(position_to_fill, sudoku):
        print('All cells filled, exiting...')
        return True

    row = position_to_fill[0]
    col = position_to_fill[1]

    for i in range(1, 10):
        if is_location_valid(i, row, col, sudoku):
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0

    return False

def run(sudoku):
    print('Sudoku Board - initial state')
    print_sudoku(sudoku)
    solve_sudoku(sudoku)
    print('Sudoku Board - Final state')
    print_sudoku(sudoku)
    return sudoku


if __name__ == "__main__":
    sudoku = [[0 for j in range(9)] for i in range(9)]
    run(sudoku)