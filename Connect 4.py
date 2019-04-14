""" 
Henry Rodas
4/12/19 
Final Project
This program will allow 2 users to play connect 4 against each other.
"""
from graphics import*
"""
main():
Description: Will call the methods that create the window and the board and the
method that will run the game
Parameters: None
Returns: None
Plan: Calls the methods that create the window and board and call connect4
"""
def main():
    win = GraphWin("Connect 4",700,700)
    win.yUp()
    makeBoard(win)
    connect4(win)

"""
Description: 
Parameters: 
	win  - window to draw the board in
	
Returns: 
Plan: 
"""
def connect4(win):
    board = ["BBBBBBB","BBBBBBB","BBBBBBB","BBBBBBB","BBBBBBB",\
             "BBBBBBB"]
    width = win.getWidth()
    height = win.getHeight()
    boardHeight = height/7*6
    colHeight1 = boardHeight/7
    colHeight2 = boardHeight/7
    colHeight3 = boardHeight/7
    colHeight4 = boardHeight/7
    colHeight5 = boardHeight/7
    colHeight6 = boardHeight/7
    colHeight7 = boardHeight/7
    colHeightList = [colHeight1,colHeight2, colHeight3, colHeight4, colHeight5,\
                     colHeight6, colHeight7]
    widthLength = width/8
    circleRadiusHalf = width/14.0 - 10 /2
    turn = 0
    while checkScore(board) == None:
        click = win.getMouse()
        for i in range(7):
            if widthLength - circleRadiusHalf < click.getX() < widthLength + \
               circleRadiusHalf:
                turn += 1
                playerMove(i, colHeightList[i] / (boardHeight/7)-1, turn,board)
                clickCircle(turn, i+1, colHeightList[i], win)
                colHeightList[i] += boardHeight/7
            widthLength += width/8
            
        widthLength = width/8
        
        
    if checkScore(board) == "X":
        winner = Text(Point(width/2, height-20),"Player 1 Wins!")
        winner.draw(win)
    else:
        winner = Text(Point(width/2, height-20), "Player 2 Wins!")
        winner.draw(win)

def playerMove(col, row, turn, board):
    # O is yellow and X is red
    turnList = ["O", "X"]
    board[row] = board[row][:col] + turnList[turn%2] + board[row][col+1:]
"""
Description: Draws the connect 4 board 
Parameters: 
	win  - window to draw the board in 
Returns: None
Plan: I will evenly space out the empty circles in the board so that it could
use any size window. I will first draw the outline of the board and make a for
loop that will draw the empty circles based on the spacing of the window. 
"""
def makeBoard(win):
    width = win.getWidth()
    height = win.getHeight() 
    boardHeight = height/7*6
    board = Rectangle(Point(0,boardHeight),Point(width,0))
    board.setFill("blue")
    board.draw(win)
    circleRadius = width/14.0 - 10
    xCenter = width/8
    yCenter = boardHeight/7
    for i in range(6):
        for i in range(7):
            circle = Circle(Point(xCenter,yCenter),circleRadius)
            circle.setFill("white")
            circle.draw(win)
            xCenter += width/8
        xCenter = width/8
        yCenter += boardHeight/7
    player1Score = Text(Point(width/10, height*0.9),"Player 1 Score: ")
    player2Score = Text(Point(width*0.8, height*0.9), "Player 2 Score: ")
    player1Score.draw(win)
    player2Score.draw(win)
    
def checkScore(board):
    for i in range(len(board)):
        for j in range(7):
            letter = board[i][j]
            if letter != "B":
                if i < 4:
                    if letter == board[i+1][j] == board[i+2][j] ==board[i+3][j]:
                        return letter
                if j < 4:
                    if letter == board[i][j+1] == board[i][j+2]== board[i][j+3]:
                        return letter
                if j < 4 and i < 4:
                    if letter == board[i+1][j+1] == board[i+2][j+2] == \
                       board[i+3][j+3]:
                        return letter
                if j > 2 and i < 3:
                    if letter == board[i+1][j-1] == board[i+2][j-2] == \
                       board[i+3][j-3]:
                        return letter
                    
    return None

def clickCircle(turn, col, circleHeight, win):
    colorList = ["yellow","red"]
    color = colorList[turn%2]
    width = win.getWidth()
    circleRadius = width/14.0 - 10
    circle = Circle(Point(width/8 * col, circleHeight), circleRadius)
    circle.setFill(color)
    circle.draw(win)
        
    
                
        

    

if __name__ == "__main__":
    main()
