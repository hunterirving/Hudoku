#breadth-first treasure hunt
#hunter irving
#2/10/2016

from random import randint
import Queue
import time


def traverse(gameBoard, visitedBoard, difficulty):
    q = Queue.Queue() #holds onto indexes we can reach, when we visit one, it gets popped off and we push its neighbors
    
    currentX = 0
    currentY = 0
    currentAnswer = ""
    q.put("0,0,solution:") #start us off by pushing the starting location
    visitedBoard = mark(0, 0, visitedBoard) #so we don't try to go to the starting position
    
    while (True):
        print("now popping...")             
        try:
            popped =  q.get_nowait().split(',') #pop top element
        except Queue.Empty:
            print("queue is empty...")
            printBoard(gameBoard)
            print "THIS BOARD HAS NO SOLUTIONS"
            print "calling main"
            main(difficulty) #we need to generate a new board, hopefully with a solution
            return
        
        print ("popped " + str(popped) + " off of the queue")
        
        currentX = int(popped[0]) #grab X from popped thing
        currentY = int(popped[1]) #grab Y from popped thing  
        currentAnswer = popped[2] #grab answer string from popped thing
        
        indexValue = gameBoard[currentX][currentY] #get value at index (currentX,currentY)
    
        if(currentX - indexValue) < 0: #will moving up put us OB?
            print "moving up " + str(indexValue) + " takes us OB"
        elif(unvisited(currentX - indexValue, currentY, visitedBoard)): #have we already visited this element?
            print "moving up " + str(indexValue) + " is valid"
            print "pushing " + str(currentX - indexValue) + "," + str(currentY) + " onto the queue"
            visitedBoard = mark(currentX - indexValue, currentY, visitedBoard) #mark unmarked neighbor above us
            q.put(str(currentX - indexValue) + "," + str(currentY) + "," + currentAnswer + " up") #push that neighbor onto the queue
            
        if(currentY + indexValue) > 20: #will moving right put us OB?
            print "moving right " + str(indexValue) + " takes us OB"
        elif(unvisited(currentX, currentY + indexValue, visitedBoard)): #have we already visited this element?
            print "moving right " + str(indexValue) + " is valid"
            print "pushing " + str(currentX) + "," + str(currentY + indexValue) + " onto the queue"
            visitedBoard = mark(currentX, currentY + indexValue, visitedBoard) #mark unmarked neighbor to our right
            q.put(str(currentX) + "," + str(currentY + indexValue) + "," + currentAnswer + " right") #push that neighbor onto the queue
            if(doneCheck(currentX, currentY + indexValue)):
                printBoard(gameBoard)
                finalAnswer = currentAnswer + " right"
                finalAnswerLength = len(finalAnswer.split()) - 1
                print "Length of shortest solution: " + str(finalAnswerLength)
                print "Shortest " + str(finalAnswer)
                if(weNeedToGoDeeper(finalAnswerLength, difficulty)):
                    main(difficulty)
                return
                
        if(currentX + indexValue) > 20: #will moving down put us OB?
            print "moving down " + str(indexValue) + " takes us OB"
        elif(unvisited(currentX + indexValue, currentY, visitedBoard)): #have we already visited this element?
            print "moving down " + str(indexValue) + " is valid"
            print "pushing " + str(currentX + indexValue) + "," + str(currentY) + " onto the queue"
            visitedBoard = mark(currentX + indexValue, currentY, visitedBoard) #mark unmarked neighbor below us
            q.put(str(currentX + indexValue) + "," + str(currentY) + "," + currentAnswer + " down") #push that neighbor onto the queue
            if(doneCheck(currentX + indexValue, currentY)):
                printBoard(gameBoard)
                finalAnswer = currentAnswer + " down"
                finalAnswerLength = len(finalAnswer.split()) - 1
                print "Length of shortest solution: " + str(finalAnswerLength)
                print "Shortest " + str(finalAnswer)
                if(weNeedToGoDeeper(finalAnswerLength, difficulty)):
                    main(difficulty)
                return
                
        if(currentY - indexValue) < 0: #will moving left put us OB?
            print "moving left " + str(indexValue) + " takes us OB"
        elif(unvisited(currentX, currentY - indexValue, visitedBoard)): #have we already visited this element?
            print "moving left " + str(indexValue) + " is valid"
            print "pushing " + str(currentX) + "," + str(currentY - indexValue) + " onto the queue"
            visitedBoard = mark(currentX, currentY - indexValue, visitedBoard) #mark unmarked neighbor to our left
            q.put(str(currentX) + "," + str(currentY - indexValue) + "," + currentAnswer + " left") #push that neighbor onto the queue
            
def doneCheck(X, Y):
    if (X == 20 and Y == 20):
        print "SOLUTION FOUND"
        return True
    return False

def mark(X, Y, visitedBoard):
    visitedBoard[X][Y] = True
    return visitedBoard
                             
def unvisited(X, Y, visitedBoard):
    return not(visitedBoard[X][Y])
        
def generateVisitedBoard():
    visitedBoard = [[False for x in range(21)] for x in range(21)]    
    return visitedBoard
    
#un-comment the debug board to try different set-ups
def generateGameBoard():
    board = [[randint(1,4) for x in range(21)] for x in range(21)]
    """board = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 4],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]"""
    return board
                 
def printBoard(board):
    for row in board:
        print '\n',
        for val in row:
            print val,
    print '\n'
    
def getDifficulty(): #returns a difficulty string
    difficulty = ''
    while not(difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard' or difficulty == 'any'):
        difficulty = raw_input("\nInput difficulty: easy / medium / hard / any : ")
    return difficulty

    
def weNeedToGoDeeper(length, diff): #returns true or false
    if(diff == 'any'):
        return False
    elif(diff == 'easy'):
        if(length < 14):
            return False
        return True
    elif(diff == 'medium'):
        if(length == 14):
            return False
        return True
    elif(diff == 'hard'):
        if(length > 14):
            return False
        return True
    
def main(difficulty):
    gameBoard = generateGameBoard()
    printBoard(gameBoard)
    visitedBoard = generateVisitedBoard()
    traverse(gameBoard, visitedBoard, difficulty)

def newMain():
    main(getDifficulty())

newMain()    
    

#interesting observations + ideas

""" best solutions are almost always made up of only rights and downs, as lefts and ups take you further from the solution
shortest solution is of length 10
longest is of length 40(?) ... all ones zig-zagging from start to finish? that's actually wrong... zig-zag horizontally down..
next step will be to write a modified version of this program that generates 5000 (or some large number) boards,
finds the shortest solution for each, finds the length of each shortest solution, puts the lengths of all these solutions into a list,
and averages the elements in the list to find the "average shortest length" for these types of problems
this will become our baseline for "medium difficulty" problems
easy problems will take a few less steps
harder a few more
we can prompt a user for "easy/medium/hard" difficulty, then continually generate boards until we generate one whose
shortest solution is within the appropriate range
if a generated board has zero solutions, we'll throw it out and generate another one...
to PROVE that this breadth-first approach is better than depth-first, we'll generate 5000 boards then feed them to both our
breadth-first and depth-first methods (that is, both algorithms will be working with identical boards)
we'll determine which of them takes longer when run on the same (non-student machine) computer
then maybe divide that by 5000 to get some stats on the average time it takes each algorithm to solve a board
then we'll write a paper about it
then we'll make a powerpoint i guess
i think broken code/failed attempts/ideas will be useful so keep all that stuff

over and out

    - h """
