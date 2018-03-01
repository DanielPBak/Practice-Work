def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

import random

num_rows = int(input('how many rows? '))
num_columns = int(input('how many columns? '))
num_bombs = int(input('how many bombs? '))

if num_bombs > num_rows * num_columns:
    exit('too many bombs')

num_zeros = (num_rows * num_columns) - num_bombs

starting_board = [0] * num_zeros + [-1]  * num_bombs
random.shuffle(starting_board)
elements_per_row = int((num_rows * num_columns) / num_rows)
board = to_matrix(starting_board, elements_per_row)
for idx_y, row in enumerate(board):
    for idx_x, element in enumerate(row):
        if element == -1:
            valid_neighbors = []
            for i in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x = idx_x + i[0]
                y = idx_y + i[1]
                if x < 0 or x >= num_columns or y < 0 or y >= num_rows or board[y][x] == -1:
                    continue
                else:
                    print((idx_x, idx_y), (x, y))
                    board[y][x] += 1
for row in board:
    print(row)
                
player_board = to_matrix(['_'] * num_rows * num_columns, elements_per_row)
num_guesses = 0
guesses_to_win = num_zeros
while(num_guesses < guesses_to_win):
    for row in player_board:
        print(row)
    guess = int(input('Flag (0) or guess (1)? '))
    guess_row = int(input('y index? '))
    guess_column = int(input('x index? '))
    if guess and (player_board[guess_row][guess_column] != '_' and player_board[guess_row][guess_column] != 'F'):
        print('already guessed this one.', player_board[guess_row][guess_column])
        continue
    if guess:
        if board[guess_row][guess_column] == -1:
            player_board[guess_row][guess_column] = 'X'
            exit('GAME OVER')
        else:
            num_guesses += 1
            print(board[guess_row][guess_column])
            player_board[guess_row][guess_column] = board[guess_row][guess_column]

    else:
        player_board[guess_row][guess_column] = 'F'

for row in player_board:
    print(row)
exit('You win!')
