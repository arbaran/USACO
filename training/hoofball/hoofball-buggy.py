'''
Terms:
    Dead pool: 2 player(1 pair) pass to each other, ball cannot pass out of the pool.
    Pass direction: 'L' - pass to left. 'R' - pass to right.

    Each player(cow) has 2 attributes: position and pass direction. Pass direction will be decided by
        the distance to it's neighbors.

Solution:
    No matter from where the balls started, eventually they all ended in dead pool. So instead of counting
    how many balls to start with, we can just count how many balls fall into deal pool at the end.
    1. Sort player by poistion value. Smaller position number on left, larger position number on right.
    2. Identify all dead pools
    3. For each dead pool, count how many balled being trapped eventrually.
        1) if there's no input ball (means left neighbor pass to left, right neighbor pass to right),
            there will be 1 ball ended in this pool.
        2) if there's one input ball (means left eighbor pass to right OR right neighbor pass to left),
            there will be 1 ball ended in this pool.
        3) if there's two input ball (means left eighbor pass to right AND right neighbor pass to left),
            there will be 2 balls ended in this pool.
    4. Calculate the sum of balls ended in every dead pool and the sum will be the result.
'''


# Player class
class Player:
    def __init__(self, position):
        self._p = position
        self._d = 'N'

    # get position
    def getPosition(self):
        return self._p

    # get    distance to another player
    def distance(self, player):
        return abs(self._p - player._p)
    
    # set pass direction
    def setPassDirection(self, d):
        self._d = d
    
    # get pass direction
    def getPassDirection(self):
        return self._d

  

   
# Main program
# read input
lines = []
with open("hoofball.in") as fInput:
    lines = fInput.readlines()

# turn input to a list of Players
players = list(Player(int(x.strip())) for x in lines[1].split())

# sort player list based on position value
players.sort(key = lambda p : p.getPosition())

# set pass directions for each player
N = len(players)
for i in range(N):
    if i == 0: # first one can only pass to right
        players[i].setPassDirection('R')
    elif i == N - 1: # last one can only pass to left
        players[i].setPassDirection('L')
    else: # middle players pass direction depends on distance to left and right
        leftDistance = players[i].distance(players[i - 1])
        rightDistance = players[i].distance(players[i + 1])
        if leftDistance > rightDistance: # If close to right
            players[i].setPassDirection('R')
        else: 
            players[i].setPassDirection('L') 

# find dead pool started from very left
deadPoolList = []
preDirection = 'R' # previous player's pass direction
for i in range(N): 
    curDirection = players[i].getPassDirection() # current player's pass direction
    # If previous player pass to right and current player pass to left, it's a dead pool
    if preDirection == 'R' and curDirection == 'L': 
        deadPool = (i - 1, i)
        deadPoolList.append(deadPool)
    preDirection = curDirection

# caculate trapped balls
trappedBalls = 0
if len(deadPoolList) == 0: # no dead pool, only 1 inital ball needed
    trappedBalls = 1 
else:
    for deadPool in deadPoolList:
        if deadPool[0] == 0: # If dead pool is on very left
            trappedBalls += 1
        elif deadPool[1] == N - 1: # if dead pool is on very right
            trappedBalls += 1
        else: # If dead pool is in the middle
            # if left neighbor pass to right AND right neighbor pass to left    
            if players[deadPool[0] - 1].getPassDirection() == 'R' and players[deadPool[1] + 1].getPassDirection() == 'L': 
                trappedBalls += 2
            # if left neighbor pass to right OR right neighbor pass to left
            elif players[deadPool[0] - 1].getPassDirection() == 'R' or players[deadPool[1] + 1].getPassDirection() == 'L': 
                trappedBalls += 1
            #if there's no input from both left and right neighbors
            elif players[deadPool[0] - 1].getPassDirection() == 'L' and players[deadPool[1] + 1].getPassDirection() == 'R':
                trappedBalls += 1    

result = trappedBalls

# Write output
with open("hoofball.out", 'w') as fOutput:
    fOutput.write(str(result))