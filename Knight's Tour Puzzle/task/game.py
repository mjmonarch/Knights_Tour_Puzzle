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
def format_num_y(num, digits):
    if len(str(num)) < digits:
        return str(' ' * (digits - len(str(num))) + str(num))
    else:
        return str(num)


def format_num_x(num, digits):
    if len(str(num)) < digits:
        return str(' ' * (digits - len(str(num))) + str(num))
    else:
        return str(num)


def display_board(_X, _Y, _x, _y):
    y_digits = len(str(_Y))
    cell_size = len(str(_X * _Y))
    empty_cell = '_' * cell_size + ' '
    full_cell = ' ' * (cell_size - 1) + 'X' + ' '
    border = ' ' * len(str(_Y)) + '-' * (_X * (cell_size + 1) + 3)
    num_string = ' ' * len(str(_Y)) + '  '
    for i in range (_X):
        num_string += format_num_x(str(i + 1), cell_size) + ' '

    print(border)
    for i in range(_Y, 0, -1):
        if i != _y:
            print(format_num_y(i, y_digits), '| ' + _X * empty_cell + '|', sep='')
        else:
            output_line = f"{format_num_y(i, y_digits)}| "
            output_line += "".join([full_cell if j == _x else empty_cell for j in range(1, _X + 1)])
            output_line += '|'
            print(output_line)
    print(border)
    print(num_string)


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
display_board(X, Y, x, y)
