import copy
import random

class State:
    def __init__(self, state=None, parent=None, move=None, g=None, f=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.f = f

    def getstate(self):
        return self.state

    def setstate(self, state):
        self.state = state

    def setparent(self, parent):
        self.parent = parent

    def getparent(self):
        return self.parent

    def getmove(self):
        return self.move

    def setmove(self, move):
        self.move = move

    def getf(self):
        return self.f

    def setf(self, f):
        self.f = f

    def getg(self):
        return self.g

    def setg(self, g):
        self.g = g

    # iterates through the given state and prints each column, row, element
    def outputstate(self):
        state = self.state
        # print (state
        for i in range(state.__len__()):
            print (state[i])
        return

    # simply creates a new copy of the given state and returns the new state
    # PERSONAL NOTE: look into changing deepcopy O{n^2)
    def clonestate(self):
        state = self.state
        tempstate = copy.deepcopy(state)
        return tempstate

    # iterates through the state and returns true if the state has been completed
    def completecheck(self):
        state = self.state
        tof = True
        for i in range(state.__len__()):
            row = state[i]
            for j in range(row.__len__()):
                if row[j] == "-1":
                    tof = False
        return tof

    # compares each value and position. Returns true if state1 and state2 are equal, else returns false
    def statecomparison(self, state2):
        state1 = self.state
        tof = False
        if state1 == state2:
            tof = True
        return tof

    # takes in a piece(number as string) and state as arguments
    # finds all valid moves for the given piece and returns a list
    # containing all valid moves (up, down, right, left as strings)
    def listofmoves(self, piece, state):

        list = []
        piecevalidationint = int(piece)
        row = []
        up = []
        down = []
        right = []
        left = []

        # error handling
        if piecevalidationint < 2:
            return list

        for i in range(state.__len__()):

            for j in range(state[i].__len__()):

                if piece == state[i][j]:

                    if piece == '2':
                        # check if left of piece is empty or part of piece
                        if state[i][j - 1] == piece or state[i][j - 1] == '0' or state[i][j - 1] == '-1':
                            left.append(True)
                        else:
                            left.append(False)

                        # check if right of piece is empty or part of piece
                        if state[i][j + 1] == piece or state[i][j + 1] == '0' or state[i][j + 1] == '-1':
                            right.append(True)
                        else:
                            right.append(False)

                        # check if up of piece is empty or part of piece
                        if state[i - 1][j] == piece or state[i - 1][j] == '0' or state[i - 1][j] == '-1':
                            up.append(True)
                        else:
                            up.append(False)

                        # check if down of piece is empty or part of piece
                        if state[i + 1][j] == piece or state[i + 1][j] == '0' or state[i + 1][j] == '-1':
                            down.append(True)
                        else:
                            down.append(False)

                    else:

                        # check if left of piece is empty or part of piece
                        if state[i][j-1] == piece or state[i][j-1] == '0':
                            left.append(True)
                        else:
                            left.append(False)

                        # check if right of piece is empty or part of piece
                        if state[i][j+1] == piece or state[i][j+1] == '0':
                            right.append(True)
                        else:
                            right.append(False)

                        # check if up of piece is empty or part of piece
                        if state[i-1][j] == piece or state[i-1][j] == '0':
                            up.append(True)
                        else:
                            up.append(False)

                        # check if down of piece is empty or part of piece
                        if state[i+1][j] == piece or state[i+1][j] == '0':
                            down.append(True)
                        else:
                            down.append(False)

                    # row.append([i, j])

        if all(up):
            list.append('up')
        if all(down):
            list.append('down')
        if all(left):
            list.append('left')
        if all(right):
            list.append('right')


        # return list
        return list


    # iterates through given state and calls listofmoves for each non 0 and -1 piece every piece's moves
    # are stored in a list and appended to a list of all moves which is returned to the caller
    def allmoves(self):
        state = self.state
        moves = []
        pieces = []
        for i in range( state.__len__() ):
            for j in range( state[i].__len__() ):
                temp = int(state[i][j])
                if temp >= 2:
                    if not pieces.__contains__(state[i][j]):
                        pieces.append(state[i][j])

                        allmovesforcurrentpiece = self.listofmoves(state[i][j], state)

                        # check if piece has more than one move
                        if allmovesforcurrentpiece.__len__() > 1:
                            for k in range(allmovesforcurrentpiece.__len__()):
                                moves.append([state[i][j], [allmovesforcurrentpiece[k]]])
                        elif allmovesforcurrentpiece.__len__() == 1:
                            moves.append([state[i][j], allmovesforcurrentpiece])
        return moves


    # given a state and move(a list of two strings, piece and direction)
    # applymove updates the state with the move
    def applymove(self, move, state):

        # list = self.listofmoves(move[0], state)
        # movesmade = []
        #
        # # checks if given move is valid
        # if not list:
        #     return

        # if move is to the right or down, the algorithm iterates from bottom-right up iterating to the left
        # instead of top-left down iterating to the right
        # this effectively reduces checks to avoid errors when moving blocks that are greater than one piece
        if move[1][0] == 'right' or move[1][0] == 'down':

            # New implementation for right and down moves

            for i in range(state.__len__()-1, -1, -1):
                for j in range(state[i].__len__()-1, -1, -1):
                    if move[0] == state[i][j]:
                        if move[1][0] == 'right': #and ((state[i][j+1] == move[0] or state[i][j+1] == '0') or ((move[0] == '2') and (state[i][j+1] <= move[0]))):
                            state[i][j+1] = state[i][j]
                            state[i][j] = '0'

                        elif move[1][0] == 'down':# and ((state[i+1][j] == move[0] or state[i+1][j] == '0') or ((move[0] == '2') and (state[i+1][j] <= move[0]))):
                            state[i+1][j] = state[i][j]
                            state[i][j] = '0'

            ## Commenting out old implementation. Performance hit for reverse()
            # state.reverse()
            #
            # for i in range(state.__len__()):
            #     for j in range(state[i].__len__()):
            #         if move[0] == state[i][j]:
            #
            #             if move[1][0] == 'right':
            #                 state[i][j - 1] = state[i][j]
            #                 state[i][j] = '0'
            #
            #             elif move[1][0] == 'down':
            #                 state[i-1][j] = state[i][j]
            #                 state[i][j] = '0'
            #
            # state.reverse()

        elif move[1][0] == 'left' or move[1][0] == 'up':

            for i in range(state.__len__()):
                for j in range(state[i].__len__()):
                    if move[0] == state[i][j]:

                        if move[1][0] == 'left':# and ((state[i][j-1] == move[0] or state[i][j-1] == '0') or ((move[0] == '2') and (state[i][j-1] <= move[0]))):
                            state[i][j-1] = state[i][j]
                            state[i][j] = '0'

                        elif move[1][0] == 'up':# and ((state[i-1][j] == move[0] or state[i-1][j] == '0') or ((move[0] == '2') and (state[i-1][j] <= move[0]))):
                            state[i-1][j] = state[i][j]
                            state[i][j] = '0'

        return

    # clones the given state and then applies the given move
    # the updated cloned state is then returned
    def applymovecloning(self, move):

        cloned = self.clonestate()
        self.applymove(move, cloned)

        return cloned

    # loops through every element and swaps and reduces the block number
    # while rearranging all non 2, 1 and -1 blocks in an ascending order
    # from top left to bottom right
    # this code is translated from the assignment page
    def normalize(self):
        state = self.state

        nextidx = '3'

        for h in range(state.__len__()):
            for w in range(state[h].__len__()):

                if int(state[h][w]) == int(nextidx):
                    nextidx = str(int(nextidx) + 1)

                elif int(state[h][w]) > int(nextidx):
                    self.swapidx(nextidx, state[h][w], state)
                    nextidx = str(int(nextidx) + 1)

        return

    # swaps given values in the given state
    # helper function for normalize
    # this code is translated from the assignment page
    @staticmethod
    def swapidx(val1, val2, state):

        for h in range(state.__len__()):
            for w in range(state[h].__len__()):

                if int(state[h][w]) == int(val1):
                    state[h][w] = val2

                elif int(state[h][w]) == int(val2):
                    state[h][w] = val1

        return

    # picks a random move from the set of all valid moves and applies it
    # normalizes the updated state and repeats the previous steps either N
    # number of times or if the puzzle has been completed, whichever is
    # achieved first
    def randomwalks(self, n):
        state = self.state

        for i in range(n):

            # outputs current state
            print ('Current State')
            self.outputstate()

            # checks if complete, prints either true or false
            # if true then returns to caller
            complete = self.completecheck()
            print (complete)

            if complete:
                return

            # gets and prints all moves
            moves = self.allmoves()
            print ('List of all moves')

            randnum = random.randint(0, (moves.__len__() - 1))

            print ('Applying Move ', moves[randnum])

            # applies move
            self.applymove(moves[randnum], state)

            print ('New State')

            # prints new state after the move has been applied
            self.outputstate()

            print ('Normalizing State')

            # normalizes state
            self.normalize()

            print ('------------------------------------')

        return
