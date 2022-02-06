# # ---------------------------------STAGE 1---------------------------------
# def display_board(_x, _y):
#     print('-------------------')
#     for i in range(8, 0, -1):
#         if i != _y:
#             print(i, '| _ _ _ _ _ _ _ _ |', sep='')
#         else:
#             output_line = f"{i}|"
#             output_line += "".join([' X' if j == _x else ' _' for j in range(1, 9)])
#             output_line += ' |'
#             print(output_line)
#     print('-------------------')
#     print('   1 2 3 4 5 6 7 8 ')
#
#
# print("Enter the knight's starting position:")
# while True:
#     try:
#         x, y = [int(x) for x in input().split()]
#         if 0 <= x <= 8 and 0 <= y <= 8:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# display_board(x, y)

# ---------------------------------STAGE 2---------------------------------
# def format_num_y(num, digits):
#     if len(str(num)) < digits:
#         return str(' ' * (digits - len(str(num))) + str(num))
#     else:
#         return str(num)
#
#
# def format_num_x(num, digits):
#     if len(str(num)) < digits:
#         return str(' ' * (digits - len(str(num))) + str(num))
#     else:
#         return str(num)
#
#
# def display_board(_X, _Y, _x, _y):
#     y_digits = len(str(_Y))
#     cell_size = len(str(_X * _Y))
#     empty_cell = '_' * cell_size + ' '
#     full_cell = ' ' * (cell_size - 1) + 'X' + ' '
#     border = ' ' * len(str(_Y)) + '-' * (_X * (cell_size + 1) + 3)
#     num_string = ' ' * len(str(_Y)) + '  '
#     for i in range (_X):
#         num_string += format_num_x(str(i + 1), cell_size) + ' '
#
#     print(border)
#     for i in range(_Y, 0, -1):
#         if i != _y:
#             print(format_num_y(i, y_digits), '| ' + _X * empty_cell + '|', sep='')
#         else:
#             output_line = f"{format_num_y(i, y_digits)}| "
#             output_line += "".join([full_cell if j == _x else empty_cell for j in range(1, _X + 1)])
#             output_line += '|'
#             print(output_line)
#     print(border)
#     print(num_string)

#
# while True:
#     print("Enter your board dimensions:")
#     try:
#         X, Y = [int(x) for x in input().split()]
#         if X > 0 and Y > 0:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# while True:
#     print("Enter the knight's starting position:")
#     try:
#         x, y = [int(x) for x in input().split()]
#         if 0 < x <= X and 0 < y <= Y:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# display_board(X, Y, x, y)

# # ---------------------------------STAGE 3---------------------------------
# def format_num(num, digits):
#     if len(str(num)) < digits:
#         return str(' ' * (digits - len(str(num))) + str(num))
#     else:
#         return str(num)
#
#
# def str_cell(size, value):
#     if value == 0:
#         return '_' * size + ' '
#     elif value == 1:
#         return ' ' * (size - 1) + 'X' + ' '
#     elif value == 2:
#         return ' ' * (size - 1) + 'O' + ' '
#
#
# def display_board(_X, _Y, _board):
#     y_digits = len(str(_Y))
#     cell_size = len(str(_X * _Y))
#     border = ' ' * len(str(_Y)) + '-' * (_X * (cell_size + 1) + 3)
#     num_string = ' ' * len(str(_Y)) + '  '
#     for i in range (_X):
#         num_string += format_num(str(i + 1), cell_size) + ' '
#
#     print(border)
#     for i in range(_Y):
#         output_line = f"{format_num(_Y - i, y_digits)}| "
#         for j in range(_X):
#             output_line += str_cell(cell_size, _board[_Y - i - 1][j])
#         output_line += '|'
#         print(output_line)
#     print(border)
#     print(num_string)
#
#
# while True:
#     print("Enter your board dimensions:")
#     try:
#         X, Y = [int(x) for x in input().split()]
#         if X > 0 and Y > 0:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# while True:
#     print("Enter the knight's starting position:")
#     try:
#         y, x = [int(x) for x in input().split()]
#         if 0 < x <= Y and 0 < y <= X:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# board = [[0] * X for i in range(Y)]
# board[x - 1][y - 1] = 1
# # print(board)
#  # check up
# if x + 2 <= Y:
#     if y != 1:
#         board[x + 1][y - 2] = 2
#     if y + 1 <= X:
#         board[x + 1][y] = 2
# # check bottom
# if x - 2 >= 1:
#     if y != 1:
#         board[x - 3][y - 2] = 2
#     if y + 1 <= X:
#         board[x - 3][y] = 2
# # check left
# if y - 2 >= 1:
#     if x != 1:
#         board[x - 2][y - 3] = 2
#     if x + 1 <= Y:
#         board[x][y - 3] = 2
# # check right
# if y + 2 <= X:
#     if x != 1:
#         board[x - 2][y + 1] = 2
#     if x + 1 <= Y:
#         board[x][y + 1] = 2
#
# display_board(X, Y, board)

# ---------------------------------STAGE 4---------------------------------
# def format_num(num, digits):
#     if len(str(num)) < digits:
#         return str(' ' * (digits - len(str(num))) + str(num))
#     else:
#         return str(num)
#
#
# def str_cell(size, value):
#     if value == 0:
#         return '_' * size + ' '
#     elif value == -1:
#         return ' ' * (size - 1) + 'X' + ' '
#     else:
#         return ' ' * (size - 1) + str(value) + ' '
#
#
# def display_board(_board):
#     y_digits = len(str(Y))
#     cell_size = len(str(X * Y))
#     border = ' ' * len(str(Y)) + '-' * (X * (cell_size + 1) + 3)
#     num_string = ' ' * len(str(Y)) + '  '
#     for i in range (X):
#         num_string += format_num(str(i + 1), cell_size) + ' '
#
#     print(border)
#     for i in range(Y):
#         output_line = f"{format_num(Y - i, y_digits)}| "
#         for j in range(X):
#             output_line += str_cell(cell_size, _board[Y - i][j + 1])
#         output_line += '|'
#         print(output_line)
#     print(border)
#     print(num_string)
#
#
# def num_moves(_x, _y, _board):
#     quantity = 0
#     # check up
#     if _x + 2 <= Y:
#         if _y != 1 and not board[_x + 2][_y - 1]:
#             quantity += 1
#         if _y != X and not board[_x + 2][_y + 1]:
#             quantity += 1
#     # check bottom
#     if _x - 2 >= 1:
#         if _y != 1 and not board[_x - 2][_y - 1]:
#             quantity += 1
#         if _y != X and not board[_x - 2][_y + 1]:
#             quantity += 1
#     # check left
#     if _y - 2 >= 1:
#         if _x != Y and not board[_x + 1][_y - 2]:
#             quantity += 1
#         if _x != 1 and not board[_x - 1][_y - 2]:
#             quantity += 1
#     # check right
#     if _y + 2 <= X:
#         if _x != 1 and not board[_x - 1][_y + 2]:
#             quantity += 1
#         if _x != Y and not board[_x + 1][_y + 2]:
#             quantity += 1
#     return quantity
#
#
# while True:
#     print("Enter your board dimensions:")
#     try:
#         X, Y = [int(x) for x in input().split()]
#         if X > 0 and Y > 0:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# while True:
#     print("Enter the knight's starting position:")
#     try:
#         y, x = [int(x) for x in input().split()]
#         if 0 < x <= Y and 0 < y <= X:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# board = [[0] * (X + 1) for i in range(Y + 1)]
# board[x][y] = -1
# print(board)
# # check up
# if x + 2 <= Y:
#     if y != 1:
#         board[x + 2][y - 1] = num_moves(x + 2, y - 1, board)
#     if y != X:
#         board[x + 2][y + 1] = num_moves(x + 2, y + 1, board)
# # check bottom
# if x - 2 >= 1:
#     if y != 1:
#         board[x - 2][y - 1] = num_moves(x - 2, y - 1, board)
#     if y != X:
#         board[x - 2][y + 1] = num_moves(x - 2, y + 1, board)
# # check left
# if y - 2 >= 1:
#     if x != Y:
#         board[x + 1][y - 2] = num_moves(x + 1, y - 2, board)
#     if x != 1:
#         board[x - 1][y - 2] = num_moves(x - 1, y - 2, board)
# # check right
# if y + 2 <= X:
#     if x != 1:
#         board[x - 1][y + 2] = num_moves(x - 1, y + 2, board)
#     if x != Y:
#         board[x + 1][y + 2] = num_moves(x + 1 , y + 2, board)
#
# print("Here are the possible moves:")
# display_board(board)

# # ---------------------------------STAGE 5---------------------------------
# import copy
#
#
# def format_num(num, digits):
#     if len(str(num)) < digits:
#         return str(' ' * (digits - len(str(num))) + str(num))
#     else:
#         return str(num)
#
#
# def str_cell(size, value):
#     if value == -1:
#         return '_' * size + ' '
#     elif value == -2:
#         return ' ' * (size - 1) + 'X' + ' '
#     elif value == -3:
#         return ' ' * (size - 1) + '*' + ' '
#     else:
#         return ' ' * (size - 1) + str(value) + ' '
#
#
# def display_board(_board):
#     y_digits = len(str(Y))
#     cell_size = len(str(X * Y))
#     border = ' ' * len(str(Y)) + '-' * (X * (cell_size + 1) + 3)
#     num_string = ' ' * len(str(Y)) + '  '
#     for i in range (X):
#         num_string += format_num(str(i + 1), cell_size) + ' '
#
#     print(border)
#     for i in range(Y):
#         output_line = f"{format_num(Y - i, y_digits)}| "
#         for j in range(X):
#             output_line += str_cell(cell_size, _board[Y - i][j + 1])
#         output_line += '|'
#         print(output_line)
#     print(border)
#     print(num_string)
#
#
# def num_moves(_x, _y, _board):
#     quantity = 0
#     # check up
#     if _y + 2 <= Y:
#         if _x != 1 and board[_y + 2][_x - 1] not in [-3, -2]:
#             quantity += 1
#         if _x != X and board[_y + 2][_x + 1] not in [-3, -2]:
#             quantity += 1
#     # check bottom
#     if _y - 2 >= 1:
#         if _x != 1 and board[_y - 2][_x - 1] not in [-3, -2]:
#             quantity += 1
#         if _x != X and board[_y - 2][_x + 1] not in [-3, -2]:
#             quantity += 1
#     # check left
#     if _x - 2 >= 1:
#         if _y != Y and board[_y + 1][_x - 2] not in [-3, -2]:
#             quantity += 1
#         if _y != 1 and board[_y - 1][_x - 2] not in [-3, -2]:
#             quantity += 1
#     # check right
#     if _x + 2 <= X:
#         if _y != 1 and board[_y - 1][_x + 2] not in [-3, -2]:
#             quantity += 1
#         if _y != Y and board[_y + 1][_x + 2] not in [-3, -2]:
#             quantity += 1
#     return quantity
#
#
# def get_possible_moves():
#     _possible_moves = []
#     # check up
#     if y + 2 <= Y:
#         if x != 1 and board[y + 2][x - 1] not in [-3, -2]:
#             _possible_moves.append([x - 1, y + 2])
#         if x != X and board[y + 2][x + 1] not in [-3, -2]:
#             _possible_moves.append([x + 1, y + 2])
#     # check bottom
#     if y - 2 >= 1:
#         if x != 1 and board[y - 2][x - 1] not in [-3, -2]:
#             _possible_moves.append([x - 1, y - 2])
#         if x != X and board[y - 2][x + 1] not in [-3, -2]:
#             _possible_moves.append([x + 1, y - 2])
#     # check left
#     if x - 2 >= 1:
#         if y != Y and board[y + 1][x - 2] not in [-3, -2]:
#             _possible_moves.append([x - 2, y + 1])
#         if y != 1 and board[y - 1][x - 2] not in [-3, -2]:
#             _possible_moves.append([x - 2, y - 1])
#     # check right
#     if x + 2 <= X:
#         if y != 1 and board[y - 1][x + 2] not in [-3, -2]:
#             _possible_moves.append([x + 2, y - 1])
#         if y != Y and board[y + 1][x + 2] not in [-3, -2]:
#             _possible_moves.append([x + 2, y + 1])
#     return _possible_moves
#
#
# def board_with_moves(_board, _possible_moves):
#     for move in _possible_moves:
#         _board[move[1]][move[0]] = num_moves(move[0], move[1], board)
#     return _board
#
#
# while True:
#     print("Enter your board dimensions:")
#     try:
#         X, Y = [int(x) for x in input().split()]
#         if X > 0 and Y > 0:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# while True:
#     print("Enter the knight's starting position:")
#     try:
#         x, y = [int(x) for x in input().split()]
#         if 0 < x <= X and 0 < y <= Y:
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Invalid dimensions!")
# board = [[-1] * (X + 1) for i in range(Y + 1)]
# board[y][x] = -2
#
# count = 1
# total_moves = X * Y
#
# while True:
#     possible_moves = get_possible_moves()
#     if not possible_moves:
#         if count < total_moves:
#             print("No more possible moves!")
#             print(f"Your knight visited {count} squares!")
#             break
#         else:
#             print("What a great tour! Congratulations!")
#             break
#     board1 = board_with_moves(copy.deepcopy(board), possible_moves)
#     display_board(board1)
#     board[y][x] = -3
#     while True:
#         print("Enter your next move:")
#         # print(possible_moves)
#         try:
#             x, y = [int(x) for x in input().split()]
#             if [x, y] in possible_moves:
#                 break
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Invalid dimensions!")
#     board[y][x] = -2
#     count += 1

# ---------------------------------STAGE 6---------------------------------
import copy
import operator


def format_num(num, digits):
    if len(str(num)) < digits:
        return str(' ' * (digits - len(str(num))) + str(num))
    else:
        return str(num)


def str_cell(size, value):
    if value == -1:
        return '_' * size + ' '
    elif value == -2:
        return ' ' * (size - 1) + 'X' + ' '
    elif value == -3:
        return ' ' * (size - 1) + '*' + ' '
    else:
        return format_num(value, size) + ' '


def display_board(_board):
    y_digits = len(str(Y))
    cell_size = len(str(X * Y))
    border = ' ' * len(str(Y)) + '-' * (X * (cell_size + 1) + 3)
    num_string = ' ' * len(str(Y)) + '  '
    for i in range (X):
        num_string += format_num(str(i + 1), cell_size) + ' '

    print(border)
    for i in range(Y):
        output_line = f"{format_num(Y - i, y_digits)}| "
        for j in range(X):
            output_line += str_cell(cell_size, _board[Y - i][j + 1])
        output_line += '|'
        print(output_line)
    print(border)
    print(num_string)


def display_board_2(_board):
    y_digits = len(str(Y))
    cell_size = len(str(X * Y))
    border = ' ' * len(str(Y)) + '-' * (X * (cell_size + 1) + 3)
    num_string = ' ' * len(str(Y)) + '  '
    for i in range(X):
        num_string += format_num(str(i + 1), cell_size) + ' '

    print(border)
    for i in range(Y):
        output_line = f"{format_num(Y - i, y_digits)}| "
        for j in range(X):
            output_line += str_cell(cell_size, _board[Y - i][j + 1])
        output_line += '|'
        print(output_line)
    print(border)
    print(num_string)


def num_moves(_x, _y, _board):
    quantity = 0
    # check up
    if _y + 2 <= Y:
        if _x != 1 and _board[_y + 2][_x - 1] == -1:
            quantity += 1
        if _x != X and _board[_y + 2][_x + 1] == -1:
            quantity += 1
    # check bottom
    if _y - 2 >= 1:
        if _x != 1 and _board[_y - 2][_x - 1] == -1:
            quantity += 1
        if _x != X and _board[_y - 2][_x + 1] == -1:
            quantity += 1
    # check left
    if _x - 2 >= 1:
        if _y != Y and _board[_y + 1][_x - 2] == -1:
            quantity += 1
        if _y != 1 and _board[_y - 1][_x - 2] == -1:
            quantity += 1
    # check right
    if _x + 2 <= X:
        if _y != 1 and _board[_y - 1][_x + 2] == -1:
            quantity += 1
        if _y != Y and _board[_y + 1][_x + 2] == -1:
            quantity += 1
    return quantity


def get_possible_moves(_board, _x, _y):
    _possible_moves = []
    # check up
    if _y + 2 <= Y:
        if _x != 1 and _board[_y + 2][_x - 1] == -1:
            _possible_moves.append((_x - 1, _y + 2))
        if _x != X and _board[_y + 2][_x + 1] == -1:
            _possible_moves.append((_x + 1, _y + 2))
    # check bottom
    if _y - 2 >= 1:
        if _x != 1 and _board[_y - 2][_x - 1] == -1:
            _possible_moves.append((_x - 1, _y - 2))
        if _x != X and _board[_y - 2][_x + 1] == -1:
            _possible_moves.append((_x + 1, _y - 2))
    # check left
    if _x - 2 >= 1:
        if _y != Y and _board[_y + 1][_x - 2] == -1:
            _possible_moves.append((_x - 2, _y + 1))
        if _y != 1 and _board[_y - 1][_x - 2] == -1:
            _possible_moves.append((_x - 2, _y - 1))
    # check right
    if _x + 2 <= X:
        if _y != 1 and _board[_y - 1][_x + 2] == -1:
            _possible_moves.append((_x + 2, _y - 1))
        if _y != Y and _board[_y + 1][_x + 2] == -1:
            _possible_moves.append((_x + 2, _y + 1))
    return _possible_moves


def board_with_moves(_board, _possible_moves):
    for move in _possible_moves:
        _board[move[1]][move[0]] = num_moves(move[0], move[1], _board)
    return _board


def solution(_board, _x, _y, _step):
    possible_moves = get_possible_moves(_board, _x, _y)
    if not possible_moves:
        if _step < X * Y + 1:
            return False
        else:
            return True
    else:
        possible_moves_dict = {}
        for move in possible_moves:
            possible_moves_dict[move] = num_moves(move[0], move[1], _board)
        possible_moves_dict_sorted = dict(sorted(possible_moves_dict.items(), key=operator.itemgetter(1), reverse=True))
        for key in possible_moves_dict_sorted:
            _board[key[1]][key[0]] = _step
            # display_board(_board)
            if solution(_board, key[0], key[1], _step + 1):
                return True
            _board[key[1]][key[0]] = -1
        return False


def play_board(_board, _x, _y):
    count = 1
    total_moves = X * Y

    while True:
        possible_moves = get_possible_moves(_board, _x, _y)
        if not possible_moves:
            if count < total_moves:
                print("No more possible moves!")
                print(f"Your knight visited {count} squares!")
                break
            else:
                print("What a great tour! Congratulations!")
                break
        board1 = board_with_moves(copy.deepcopy(_board), possible_moves)
        display_board(board1)
        _board[_y][_x] = -3
        while True:
            print("Enter your next move: ", end='')
            # print(possible_moves)
            try:
                _x, _y = [int(x) for x in input().split()]
                if (_x, _y) in possible_moves:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid move! ", end='')
        _board[_y][_x] = -2
        count += 1


while True:
    print("Enter your board dimensions:")
    try:
        X, Y = [int(x) for x in input().split()]
        if X > 0 and Y > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid dimensions!")
while True:
    print("Enter the knight's starting position:")
    try:
        x, y = [int(x) for x in input().split()]
        if 0 < x <= X and 0 < y <= Y:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid dimensions!")

board = [[-1] * (X + 1) for i in range(Y + 1)]
board[y][x] = 1

while True:
    print("Do you want to try the puzzle? (y/n):")
    answer = input()
    board_p = copy.deepcopy(board)

    result = solution(board, x, y, 2)
    if answer == 'y':
        if result:
            board_p[y][x] = -2
            play_board(board_p, x, y)
        else:
            print("No solution exists!")
        break
    if answer == 'n':
        if result:
            print("Here's the solution!")
            display_board_2(board)
        else:
            print("No solution exists!")
        break
    print("Invalid input!")
