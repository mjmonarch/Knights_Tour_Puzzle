# ---------------------------------STAGE 1---------------------------------
def display_board(_x, _y):
    print('-------------------')
    for i in range(8, 0, -1):
        if i != _y:
            print(i, '| _ _ _ _ _ _ _ _ |', sep='')
        else:
            output_line = f"{i}|"
            output_line += "".join([' X' if j == _x else ' _' for j in range(1, 9)])
            output_line += ' |'
            print(output_line)
    print('-------------------')
    print('   1 2 3 4 5 6 7 8 ')


print("Enter the knight's starting position:")
while True:
    try:
        x, y = [int(x) for x in input().split()]
        if 0 <= x <= 8 and 0 <= y <= 8:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid dimensions!")
display_board(x, y)
