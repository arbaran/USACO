with open('tttt.in', 'r') as fin:
    game_board = []
    for _ in range(3):
        game_board.append(fin.readline().rstrip('\n'))

possible = []
slash = set()
bslash = set()
for row in range(3):
    hori = set()
    verti = set()
    for col in range(3):
        hori.add(game_board[row][col])
        verti.add(game_board[col][row])
    bslash.add(game_board[row][row])
    slash.add(game_board[row][2-row])
    possible.append(hori)
    possible.append(verti)
possible.append(bslash)
possible.append(slash)

#print(possible)

team_win = 0
solo_win = 0
for i in possible:
    if len(i) == 2:
        team_win += 1
#print(team_win)
for i in possible:
    if len(i) == 1:
        solo_win += 1
print(str(team_win) + ", " + str(solo_win))


# print(game_board)