def print_sudoku(array):
    print('**********************************')
    for i in array:
        for j in i:
            print(j, end=" ")
        print("")
    print('**********************************')


def find_position_to_solve(l, array):
    for i in range(9):
        for j in range(9):
            if array[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def check(num, row, col, array):

    num_in_row = False
    num_in_column = False
    num_in_box = False

    for i in range(9):
        if array[row][i] == num:
            num_in_row = True

    for i in range(9):
        if array[i][col] == num:
            num_in_column = True

    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if array[i + box_row][j + box_col] == num:
                num_in_box = True

    if (not num_in_row and not num_in_column and not num_in_box):
        array[row][col] = num
        return True
    return False


def main_cycle(array):
    l = [0, 0]

    if not find_position_to_solve(l, array):
        print('All cells filled, exiting...')
        return True

    row = l[0]
    col = l[1]

    for i in range(1, 10):
        if check(i, row, col, array):
            if main_cycle(array):
                return True
            array[row][col] = 0

    return False

def run(array):
    print('Sudoku Board - initial state')
    print_sudoku(array)
    main_cycle(array)
    print('Sudoku Board - Final state')
    print_sudoku(array)
    return array


if __name__ == "__main__":
    array = [[0 for j in range(9)] for i in range(9)]
    run(array)