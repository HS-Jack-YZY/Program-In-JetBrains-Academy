def show_chess(chessboard):
    """ 将棋盘显示出来 """
    print("---------")
    for i in range(3):
        # 显示棋盘的每行
        print("|", end=' ')
        for index in range(3):
            # 打印每行每一元素
            print(chessboard[index + i * 3], end=' ')
        print('|')
    print("---------")

def enter_cells():
    chessboard = list(input("Enter cells: "))
    return chessboard

def check_game(chessboard):
    """检查游戏状态"""
    # if not check_winner(chessboard):
    #     if not check_exception(chessboard):
    #         print("Impossible")
    #     elif check_not_finish((chessboard)):
    #         print("Game not finished")

    if not check_exception(chessboard):
        print("Impossible")
    else:
        if not check_winner(chessboard):
            if check_not_finish(chessboard):
                return "Game not finish"
        else:
            return "Finish"



def check_not_finish(chessboard):
    flag = False
    if '_' in chessboard:
        if not (is_x_win(chessboard) and is_y_win(chessboard)):
            # 都未获胜
            flag = True
    return flag


def check_winner(chessboard):
    """ 检查胜利者 """
    flag = False
    if is_x_win(chessboard):
        print("X wins")
        flag = True
    elif is_y_win(chessboard):
        print("O wins")
        flag = True
    elif not check_not_finish(chessboard):
        print("Draw")
        flag = True

    return flag

def is_x_win(chessboard):
    """ 是否x胜利 """
    x_win = False

    # 检查是否一行获胜
    for row_num in range(3):
        for col_num in range(3):
            if chessboard[col_num + row_num * 3] == 'X':
                if col_num == 2:
                    x_win = True
                continue
            else:
                break

    # 检查是否一列获胜
    for col_num in range(3):
        for row_num in range(3):
            if chessboard[col_num + row_num * 3] == 'X':
                if row_num == 2:
                    x_win = True
                continue
            else:
                break

    # 检查是否对角获胜
    if chessboard[0] == 'X':
        if chessboard[4] == 'X':
            if chessboard[8] == 'X':
                x_win = True
    if chessboard[2] == 'X':
        if chessboard[4] == 'X':
            if chessboard[6] == 'X':
                x_win = True
    return x_win

def is_y_win(chessboard):
    """ 是否o胜利 """
    o_win = False

    # 检查是否一行获胜
    for row_num in range(3):
        for col_num in range(3):
            if chessboard[col_num + row_num * 3] == 'O':
                if col_num == 2:
                    o_win = True
                continue
            else:
                break

    # 检查是否一列获胜
    for col_num in range(3):
        for row_num in range(3):
            if chessboard[col_num + row_num * 3] == 'O':
                if row_num == 2:
                    o_win = True
                continue
            else:
                break

    # 检查是否对角获胜
    if chessboard[0] == 'O':
        if chessboard[4] == 'O':
            if chessboard[8] == 'O':
                o_win = True
    if chessboard[2] == 'O':
        if chessboard[4] == 'O':
            if chessboard[6] == 'O':
                o_win = True
    return o_win

def check_exception(chessboard):
    """ 检查是否出现impossible状态 """
    flag = True # 状态变量
    if is_x_win(chessboard) and is_y_win(chessboard):
        # 同时获胜
        flag = False
    X_Y_difference = abs(chessboard.count('X') - chessboard.count('O'))
    if X_Y_difference >= 2:
        # 棋子数目差值大于等于2
        flag = False

    return flag # False 代表有问题

def enter_coordinate_X(chessboard):
    while True:
        try:
            the_row, the_col = input("Enter the coordinates: ").split()
            the_row = int(the_row)
            the_col = int(the_col)
        except ValueError:
            print("You should enter numbers!")
        else:
            address = (the_row - 1) * 3 + the_col - 1
            if 1 <= the_row <= 3 and 1 <= the_col <= 3:
                if chessboard[address] == '_':
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")

    chessboard[address] = 'X'
    return chessboard

def enter_coordinate_O(chessboard):
    while True:
        try:
            the_row, the_col = input("Enter the coordinates: ").split()
            the_row = int(the_row)
            the_col = int(the_col)
        except ValueError:
            print("You should enter numbers!")
        else:
            address = (the_row - 1) * 3 + the_col - 1
            if 1 <= the_row <= 3 and 1 <= the_col <= 3:
                if chessboard[address] == '_':
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")

    chessboard[address] = 'O'
    return chessboard


def main():
    chessboard = ['_'] * 9
    show_chess(chessboard)
    while True:
        enter_coordinate_X(chessboard)
        show_chess(chessboard)
        state_result = check_game(chessboard)
        if state_result == 'Finish':
            break

        enter_coordinate_O(chessboard)
        show_chess(chessboard)
        state_result = check_game(chessboard)
        if state_result == 'Finish':
            break



main()