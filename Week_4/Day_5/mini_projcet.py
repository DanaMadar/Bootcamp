interduction ='''1. The game is played on a grid that’s 3 squares by 3 squares.
2. Players take turns putting their marks (O or X) in empty squares by typing in the number according to the template below.
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

*************
* 0 | 1 | 2 *
* --|---|-- *
* 3 | 4 | 5 *
* --|---|-- *
* 6 | 7 | 8 *
*************
'''
print(interduction)

moves = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
board = '''
****************
* {} | {} | {} *
* ---|----|--- *
* {} | {} | {} *
* ---|----|--- *
* {} | {} | {} *
****************
'''.format(*moves)
print(board)

player_input = []
player_input.append(int(input("where do you wanna set your x/o: ")))
print(player_input)

for i, numb in enumerate(moves):
    if i == player_input[-1]:
        moves[i] = player_input[-1]
    
print(moves)
    


# play = "x"
# take_turn = 0
# let win():
#     if "x" or "o" == 1

# over = (take_turn <= 8)
# loop_until_game is over:
#     take_turn(player)
#     player = "o" if player == "x" else "x"
