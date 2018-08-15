import sys
import os
import time
from State import State

# takes a file name as an argument and loads the state in the file and returns a new state as a 2D list
def loadstate( str ):

    # open file
    f = open(str, 'r')

    # 2D array for storing state
    state = []

    # get the number of columns and rows
    tempstr = f.readline()
    temparray = tempstr.split(',')
    colnum = int(temparray[0])
    rownum = int(temparray[1])

    for i in range(rownum):
        tempstr = f.readline()
        temparray = tempstr.split(',')
        temprowval = []

        for j in range(colnum):
            temprowval.append(temparray[j])

        state.append(temprowval)

    # return the loaded state
    return state


# `` increment length every time

# perform breadth first search on a given state
def breadthfirstsearch(state):
    statesExplored = []
    numberOfNodesExplored = 0
    time.clock()


    # Initialize the queue
    # Only append and pop will be used
    queue = []
    queue.append(state)
    statesExplored.append(state.getstate())

    # boolean to control bfs while loop
    found = False

    # while loop to perform bfs
    while not found:
        numberOfNodesExplored += 1
        # nextParent = 0
        moves = queue[0].allmoves()
        # print queue[0].outputstate(), moves, '\n'

        if queue[0].completecheck():
            found = True

        else:
            # nextParent = moves.__len__()
            for i in range(moves.__len__()):
                # print moves[i]
                # numberOfNodesExplored += 1
                tempstate = State(queue[0].applymovecloning(moves[i]), queue[0], moves[i])
                if tempstate.getstate() not in statesExplored:
                    queue.append(tempstate)
                    statesExplored.append(tempstate.getstate())
            queue.pop(0)

    # get time elapsed before ends
    print ('\n--------------------------\nTime taken to find solution\n-------------------------')
    print ("%1.5f" % time.clock(), 'seconds')

    # print information about solution path
    print ('\n-----------------------------------\nSolution\n-----------------------------------')
    stack = []
    parent = queue[0].getparent()
    next = queue[0]
    counter = 0
    while True:
        if next.getmove():
            stack.insert(0, next.getmove())
            next = next.getparent()
        else:
            break

    # length of solution
    lengthofsolution = stack.__len__()

    for i in range(stack.__len__()):
        print (stack.pop(0))

    queue[0].outputstate()

    print ('\n----------------------------\nNumber of Nodes Explored\n----------------------------')
    print (numberOfNodesExplored)
    print ('\n--------------------------------\nLength of Solution\n------------------------------')
    print (lengthofsolution)

    return


def printqueue(queue):
    for i in range(queue.__len__()):
        print (queue[0])
    return


def depthfirstsearch(state):
    statesExplored = []
    numberOfNodesExplored = 1
    time.clock()

    # Initialize the queue
    # Only append and pop will be used
    stack = []
    stack.insert(0, state)
    # statesExplored.append(state.getstate())

    # boolean to control dfs while loop
    found = False

    # print stack[0].outputstate(), '\n'

    if not stack[0].completecheck():
        moves = stack[0].allmoves()
        # insert initial children in stack
        for i in range(moves.__len__()-1, -1, -1):
            stack.insert(0, State(state.applymovecloning(moves[i]), state, moves[i]))

        counter = 0
        # while loop to perform dfs
        while not found:
            numberOfNodesExplored += 1

            if stack[0].getstate() in statesExplored:
                    stack.pop(0)

            elif not stack[0].completecheck():
                statesExplored.append(stack[0].getstate())
                moves = stack[0].allmoves()
                # print stack[0].outputstate(), '\n', moves[i], '\n'

                parent = stack[0]
                for i in range(moves.__len__() - 1, -1, -1):
                   stack.insert(0, State(parent.applymovecloning(moves[i]), parent, moves[i]))

            elif stack[0].completecheck():
                found = True

    # get time elapsed before ends
    print ('\n--------------------------\nTime taken to find solution\n-------------------------')
    print ("%1.5f" % time.clock(), 'seconds')

    # print information about solution path
    print ('\n-----------------------------------\nSolution\n-----------------------------------')
    solutionstack = []

    next = stack[0]
    while True:
        if next.getmove():
            solutionstack.insert(0, next.getmove())
            next = next.getparent()
        else:
            break

    # length of solution
    lengthofsolution = solutionstack.__len__()

    for i in range(solutionstack.__len__()):
        print (solutionstack.pop(0))

    stack[0].outputstate()

    print ('\n----------------------------\nNumber of Nodes Explored\n----------------------------')
    print (numberOfNodesExplored)

    print ('\n--------------------------------\nLength of Solution\n------------------------------')
    print (lengthofsolution)

    return


def a_star(state):
    # start the clock
    time.clock()

    statesExplored = set()
    # statesExplored = []
    # statesExplored = {}
    numberOfNodesExplored = 0
    state.setg(0)

    # Location of the goal
    goal_location = find_location(state, '-1')
    # print 'goal_location ', goal_location

    # Initialize the queue
    # Only append and pop will be used
    queue = []
    queue.append(state)
    # statesExplored.append(state.getstate())
    # statesExplored.update({state.getstate(): 0})
    statesExplored.add(tuple(tuple(x) for x in state.getstate()))

    # boolean to control bfs while loop
    found = False


    # while loop to perform astar
    while not found:
        index = find_lowest_f(queue)
        queue.insert(0, queue.pop(index))
        numberOfNodesExplored += 1

        # nextParent = 0
        # print queue[0].outputstate(), moves, '\n'

        if queue[0].completecheck():
            found = True

        else:
            moves = queue[0].allmoves()
            # nextParent = moves.__len__()
            for i in range(moves.__len__()):
                # piece used for current move
                piece = moves[i][1]

                tempstate = State(queue[0].applymovecloning(moves[i]), queue[0], moves[i])

                # update g and f for tempstate
                tempstate.setg(queue[0].getg() + 1)
                piece_location = find_location(tempstate, piece)
                tempstate.setf(tempstate.getg() + find_manhattan_distance(piece_location, goal_location))
                temptuple = tuple(tuple(x) for x in tempstate.getstate())

                if temptuple not in statesExplored:
                # if tempstate.getstate() not in statesExplored:
                    # if tempstate.getf() < queue[1].getf():
                    #     queue.insert(1, tempstate)
                    # else:
                    tempstate.normalize()
                    queue.append(tempstate)
                    # statesExplored.append(tempstate.getstate())
                    # statesExplored.update({tempstate.getstate(): 0})
                    statesExplored.add(temptuple)

            queue.pop(0)

    # get time elapsed before ends
    print ('\n--------------------------\nTime taken to find solution\n-------------------------')
    print ("%1.5f" % time.clock(), 'seconds')

    # print information about solution path
    print ('\n-----------------------------------\nSolution\n-----------------------------------')
    stack = []
    parent = queue[0].getparent()
    next = queue[0]
    counter = 0
    while True:
        if next.getmove():
            stack.insert(0, next.getmove())
            next = next.getparent()
        else:
            break

    # length of solution
    lengthofsolution = stack.__len__()

    for i in range(stack.__len__()):
        print (stack.pop(0))

    queue[0].outputstate()

    print ('\n----------------------------\nNumber of Nodes Explored\n----------------------------')
    print (numberOfNodesExplored)

    print ('\n--------------------------------\nLength of Solution\n------------------------------')
    print (lengthofsolution)






    # # Piece Location
    # piece_location = find_location(state, '2')
    # print 'piece_location ', piece_location

    # manhattan_distance = find_manhattan_distance(state, piece_location, goal_location)
    # print 'manhattan_distance ', manhattan_distance




    return state

def find_manhattan_distance(piece_location, goal_location):
    manhattan_distance = 99999

    # Finds the manhattan distance for all locations of piece against all locations of goal
    # for each iteration it checks if it is the lowest distance found so far, if it is then it
    # updates the manhattan_distance variable with the new lowest value
    for i in range(piece_location.__len__()):
        for j in range(goal_location.__len__()):
            val = abs(goal_location[j][0] - piece_location[i][0]) + abs(goal_location[j][1] - piece_location[i][1])
            if val < manhattan_distance:
                manhattan_distance = val

    return manhattan_distance

def find_location(state_arg, piece):
    locations = []
    state_list = state_arg.getstate()

    for i in range(state_list.__len__()):
        for j in range(state_list[i].__len__()):
            if state_list[i][j] == piece:
                locations.append([i, j])

    return locations

def find_lowest_f(queue_arg):
    temp_f = 999999
    index = -1

    for i in range(queue_arg.__len__()):
        if queue_arg[i].getf() < temp_f:
            temp_f = queue_arg[i].getf()
            index = i

    return index



# Main starts here

# check if the correct number of command line arguments have been provided
if sys.argv.__len__() != 3:
    print (sys.argv.__len__())
    print ('Please call program with 2 arguments <filename in the same directory as this program> <Search Algorithm bfs, dfs or astar>')
    exit(1)


# store filename and check if it exists
filename = sys.argv[1]
if not os.path.exists(filename):
    print ('File Was Not Found')
    exit(1)


# store searchalgo
searchalgo = sys.argv[2]


state = State(loadstate(filename))

state.outputstate()


if searchalgo.lower() == 'bfs':
    breadthfirstsearch(state)
elif searchalgo.lower() == 'dfs':
    depthfirstsearch(state)
elif searchalgo.lower() == 'id':
    print ('Did not implement iterative deepening')
elif searchalgo.lower() == 'astar':
    a_star(state)
else:
    print ('Please call program with bfs, dfs or astar')