# Kathleen Delany delan270
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work. None of it was
# obtained from any source other than material presented as part of the
# course.

import turtle
import random

def make_Board():
#creates game board grid
  m = []
  for i in range(64):
      m.append([0]*64)
  turtle.setup(500,500)
  turtle.speed('fastest')
  turtle.setworldcoordinates(0,0,50,50)
  turtle.shapesize(2,2)
  turtle.penup()
  turtle.hideturtle()
  turtle.color("seagreen")
  turtle.shape("square")
  curxpos = 5
  curypos = 40
  for i in range(8):
    for j in range(8):
      turtle.setpos(curxpos, curypos)
      m[i][j] = "empty"
      turtle.stamp()
      curypos -= 5
    curxpos += 5
    curypos = 40
  numbpos = 5
# writes in grid numbers
  for i in range(8):
    turtle.setpos(numbpos,43)
    numbpos += 5
    turtle.pendown()
    turtle.color("black")
    turtle.write(i)
    turtle.penup()
  numbpos = 40
  for i in range(8):
    turtle.setpos(1,numbpos)
    numbpos -= 5
    turtle.pendown()
    turtle.write(i)
    turtle.penup()
#Placing starting pieces
  turtle.setpos(20,20)
  turtle.shape("circle")
  turtle.color("black")
  turtle.shapesize(2,2)
  turtle.stamp()
  m[3][4] = "black"
  turtle.setpos(25,25)
  turtle.stamp()
  m[4][3] = "black"
  turtle.color("white")
  turtle.setpos(20,25)
  turtle.stamp()
  m[3][3] = "white"
  turtle.setpos(25,20)
  turtle.stamp()
  m[4][4] = "white"
  return m

# Converts Grid coordinates to Turtle coordinates
def convertGrid(userinput):
    coorDict = {(0,0):(5,40), (1,0):(10,40), (2,0):(15,40),(3,0):(20,40),(4,0):(25,40),(5,0):(30,40),(6,0):(35,40),(7,0):(40,40),
                (0,1):(5,35), (1,1):(10,35), (2,1):(15,35),(3,1):(20,35),(4,1):(25,35),(5,1):(30,35),(6,1):(35,35),(7,1):(40,35),
                (0,2):(5,30), (1,2):(10,30), (2,2):(15,30),(3,2):(20,30),(4,2):(25,30),(5,2):(30,30),(6,2):(35,30),(7,2):(40,30),
                (0,3):(5,25), (1,3):(10,25), (2,3):(15,25),(3,3):(20,25),(4,3):(25,25),(5,3):(30,25),(6,3):(35,25),(7,3):(40,25),
                (0,4):(5,20), (1,4):(10,20), (2,4):(15,20),(3,4):(20,20),(4,4):(25,20),(5,4):(30,20),(6,4):(35,20),(7,4):(40,20),
                (0,5):(5,15), (1,5):(10,15), (2,5):(15,15),(3,5):(20,15),(4,5):(25,15),(5,5):(30,15),(6,5):(35,15),(7,5):(40,15),
                (0,6):(5,10), (1,6):(10,10), (2,6):(15,10),(3,6):(20,10),(4,6):(25,10),(5,6):(30,10),(6,6):(35,10),(7,6):(40,10),
                (0,7):(5,5),  (1,7):(10,5),  (2,7):(15,5), (3,7):(20,5), (4,7):(25,5), (5,7):(30,5), (6,7):(35,5), (7,7):(40,5)}
    result = coorDict[userinput]
    return result

# Tells if coordinates is in grid
def inGrid(row,col):
  if row >= 0 and row < 8 and col >= 0 and col < 8:
    return True
  else:
    return False

def neighb_Lst(row,col):
  lst_neigh = []
  if inGrid(row-1,col-1):
      lst_neigh.append((row-1,col-1))
  if inGrid(row+1,col+1):
      lst_neigh.append((row+1,col+1))
  if inGrid(row-1,col):
      lst_neigh.append((row-1,col))
  if inGrid(row+1,col):
      lst_neigh.append((row+1,col))
  if inGrid(row,col+1):
      lst_neigh.append((row,col+1))
  if inGrid(row,col-1):
      lst_neigh.append((row,col-1))
  if inGrid(row+1,col-1):
      lst_neigh.append((row+1,col-1))
  if inGrid(row-1,col+1):
      lst_neigh.append((row-1,col+1))
  return lst_neigh

def isValidMove(board, row, col, color):
  potneighb = neighb_Lst(row,col)
  if board[row][col] == "empty":
    for i in range(len(potneighb)):
      if board[potneighb[i][0]][potneighb[i][1]] != "empty"and board[potneighb[i][0]][potneighb[i][1]] != color:
         xcoord = (row,col)[0]
         ycoord = (row,col)[1]
         xcoord2 = (potneighb[i][0],potneighb[i][1])[0]
         ycoord2 = (potneighb[i][0],potneighb[i][1])[1]

         xdelt = xcoord2 - xcoord
         ydelt = ycoord2 - ycoord
         xval = row + xdelt
         yval = col + ydelt
         #print("xval:", xval)
         #print("yval:", yval)
         if board[xval][yval] != color and board[xval][yval] != "empty":
            while board[xval][yval] != "empty" and inGrid(xval,yval):
                finalspace = board[xval][yval]
                xval+=xdelt
                yval+=ydelt
            #print("Final Space: ", finalspace)
            #flips tiles
            if finalspace == color:
                return True
  return False

def getValidMoves(board, color):
  validMoves = []
  for i in range(8):
    for j in range(8):
      if isValidMove(board, i, j, color):
        validMoves.append((i,j))
  return validMoves


def fliptiles(board,row,col,color,validtile):
  neighbors = neighb_Lst(validtile[0], validtile[1])
  for i in range(len(neighbors)):
     if board[neighbors[i][0]][neighbors[i][1]] != "empty"and board[neighbors[i][0]][neighbors[i][1]] != color:
         xcoord = (row,col)[0]
         ycoord = (row,col)[1]
         xcoord2 = (neighbors[i][0],neighbors[i][1])[0]
         ycoord2 = (neighbors[i][0],neighbors[i][1])[1]

         xdelt = xcoord2 - xcoord
         ydelt = ycoord2 - ycoord
         xval = row + xdelt
         yval = col + ydelt

         if board[xval][yval] != color and board[xval][yval] != "empty":
             while board[xval][yval] != "empty" and inGrid(xval,yval):
               finalspace = board[xval][yval]
               xval+=xdelt
               yval+=ydelt
             xval = row + xdelt
             yval = col + ydelt
             if finalspace == color:
               while board[xval][yval] != "empty" and inGrid(xval,yval):
                 board[xval][yval] = color
                 tuplecoors = convertGrid((xval,yval))
                 turtle.setposition(tuplecoors)
                 turtle.color(color)
                 turtle.stamp()
                 xval+=xdelt
                 yval+=ydelt


#Human turn
def humanTurn(board):
  validmoves = getValidMoves(board,"black")
  humanT = turtle.textinput("Othello", "Enter coordinates (row, column): ")
  if humanT == "":
    endGame(board)
  inputTurn = tuple(int(x) for x in humanT.split(","))
  validMove = False
  askagain = True
  while validMove == False:
    if inputTurn in validmoves:
      validMove = True
      askagain = False
      board[inputTurn[0]][inputTurn[1]] = "black"
      inputcoors = convertGrid(inputTurn)
      turtle.setposition(inputcoors)
      turtle.color("black")
      turtle.stamp()
      fliptiles(board,inputTurn[0],inputTurn[1],"black",inputTurn)
    if askagain == True :
      humanT = turtle.textinput("Othello", "Invalid entry: Enter coordinates (row, column): ")
      if humanT == "":
        endGame(board)
      inputTurn = tuple(int(x) for x in humanT.split(","))

#computer turn
def selectNextPlay(board):
  validmoves = getValidMoves(board,"white")
  xcoor = random.randint(0,7)
  ycoor = random.randint(0,7)
  validMove = False
  while validMove == False:
    if (xcoor,ycoor) in validmoves:
      validMove = True
      board[xcoor][ycoor] = "white"
      tuplecoors = convertGrid((xcoor,ycoor))
      turtle.setposition(tuplecoors)
      turtle.color("white")
      turtle.stamp()
      fliptiles(board,xcoor,ycoor,"white",(xcoor,ycoor))
    xcoor = random.randint(0,7)
    ycoor = random.randint(0,7)

def fullBoardCheck(board):
  for i in range(8):
    for j in range(8):
      if board[i][j] =="empty":
        return True
  return False

def endGame(board):
  humanScore = 0
  computerScore = 0
  for i in range(8):
    for j in range(8):
      if board[i][j] == "black":
        humanScore +=1
      if board[i][j] == "white":
        computerScore +=1
  turtle.color("black")
  if humanScore > computerScore:
    turtle.setposition(15,48)
    turtle.write(('Human wins!', humanScore, 'to', computerScore), font=("Arial", 20, "bold"))
  if computerScore > humanScore:
    turtle.setposition(15,48)
    turtle.write(("Computer wins!", computerScore, "to", humanScore), font=("Arial", 20, "bold"))
  if computerScore == humanScore:
    turtle.setposition(15,48)
    turtle.write(('Tie!', humanScore, 'to', computerScore), font=("Arial", 20, "bold"))
  turtle.done()




def main():
  board = make_Board()
  while fullBoardCheck(board):
    compwent = False
    humanwent = False
    # Check if no available move for each player
    if getValidMoves(board,"black") == [] and getValidMoves(board,"white") != []:
      selectNextPlay(board)
      compwent = True
    elif getValidMoves(board,"black") != [] and getValidMoves(board,"white") == []:
      humanTurn(board)
      humanwent = True

    # "Human" turn
    if humanwent == False:
      humanTurn(board)
    # Computer's turn
    if compwent == False:
      selectNextPlay(board)
    if getValidMoves(board,"white") == [] and getValidMoves(board,"black") == []:
        endGame(board)
  endGame(board)

if __name__ == '__main__':
    main()
