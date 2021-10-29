interduction = '''1. The game is played on a grid that’s 3 movess by 3 movess.
2. Players take turns putting their marks (O or X) in empty movess by typing in the number according to the template below.
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 movess are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

*************
* 0 | 1 | 2 *
* --|---|-- *
* 3 | 4 | 5 *
* --|---|-- *
* 6 | 7 | 8 *
*************
'''
print(interduction)

moves = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    board = '''
    ***************
    *  {} | {} | {}  *
    * ---|---|--- *
    *  {} | {} | {}  *
    * ---|---|--- *
    *  {} | {} | {}  *
    ***************
    '''.format(*moves)
    print(board)


def player_input():
    player = 1
    status = -1

    while status == -1:
        display_board()

        if player % 2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player)
        choice = int(input('Enter a number:'))

        if player == 1:
            mark = 'X'
        else:
            mark = 'O'

        if choice == 1 and moves[1] == 1:
            moves[1] = mark
        elif choice == 2 and moves[2] == 2:
            moves[2] = mark
        elif choice == 3 and moves[3] == 3:
            moves[3] = mark
        elif choice == 4 and moves[4] == 4:
            moves[4] = mark
        elif choice == 5 and moves[5] == 5:
            moves[5] = mark
        elif choice == 6 and moves[6] == 6:
            moves[6] = mark
        elif choice == 7 and moves[7] == 7:
            moves[7] = mark
        elif choice == 8 and moves[8] == 8:
            moves[8] = mark
        elif choice == 9 and moves[9] == 9:
            moves[9] = mark
        else:
            print('Invalid move ')
            player -= 1

        status = check_win()
        player += 1

    print('RESULT')
    if status == 1:
        print('Player', player - 1, 'win')
    else:
        print('Game draw')


def check_win():
    if moves[1] == moves[2] and moves[2] == moves[3]:
        return 1
    elif moves[4] == moves[5] and moves[5] == moves[6]:
        return 1
    elif moves[7] == moves[8] and moves[8] == moves[9]:
        return 1
    elif moves[1] == moves[4] and moves[4] == moves[7]:
        return 1
    elif moves[2] == moves[5] and moves[5] == moves[8]:
        return 1
    elif moves[3] == moves[6] and moves[6] == moves[9]:
        return 1
    elif moves[1] == moves[5] and moves[5] == moves[9]:
        return 1
    elif moves[3] == moves[5] and moves[5] == moves[7]:
        return 1
    elif moves[1] != 1 and moves[2] != 2 and moves[3] != 3 and moves[4] != 4 and moves[5] != 5 and moves[
            6] != 6 and moves[7] != 7 and moves[8] != 8 and moves[9] != 9:
        return 0
    else:
        return -1


display_board()
player_input()
