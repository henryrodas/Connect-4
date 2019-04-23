""" 
Henry Rodas
4/23/19 
Final Project
This program will allow 2 users to play connect 4 against each other.
"""
from graphics import*
import time
"""
Description: Will call the methods that create the window and the board and the
method that will run the game
Parameters: None
Returns: None
Plan: Call the methods that asks the user for the number of rounds that they
want to play and create the window and board and call connect4
"""
def main():
    numRounds = askRound()
    win = GraphWin("Connect 4",700,700)
    win.yUp()
    connect4(numRounds,win)

"""
Description: Makes a window that allows the users to click on the number of
rounds they want to play
Parameters: None
Returns: The number of rounds --> 1, 3, or 5
Plan: I will use graphics to create boxes that will have 3 options for the
number of rounds and I will check where the user clicked so that I can return
the number of rounds they wanted.
"""
def askRound():
    """
    put for loop
    """
    roundwindow = GraphWin("Rounds",500,500)
    roundwindow.yUp()
    height = roundwindow.getHeight()
    width = roundwindow.getHeight()
    question = Text(Point(width/2, height*6.5/7),"HOW MANY ROUNDS DO YOU WANT TO PLAY?")
    button1 = Circle(Point(width/3, height*5/7),50)
    button1.setFill("red")
    button1.draw(roundwindow)
    buttonnum1 = Text(Point(width/3,height*5/7-60),"1")
    buttonnum1.draw(roundwindow)
    button2 = Circle(Point(width*2/3, height*5/7),50)
    button2.setFill("red")
    buttonnum2 = Text(Point(width*2/3,height*5/7 -60),"2")
    buttonnum2.draw(roundwindow)
    button2.draw(roundwindow)
    button3 = Circle(Point(width/3, height*3/7),50)
    button3.setFill("red")
    button3.draw(roundwindow)
    buttonnum3 = Text(Point(width/3,height*3/7-60),"3")
    buttonnum3.draw(roundwindow)
    button4 = Circle(Point(width*2/3, height*3/7),50)
    button4.setFill("red")
    buttonnum4 = Text(Point(width*2/3,height*3/7 -60),"4")
    buttonnum4.draw(roundwindow)
    button4.draw(roundwindow)
    button5 = Circle(Point(width/2,height/7),50)
    button5.setFill("red")
    button5.draw(roundwindow)
    buttonnum5 = Text(Point(width/2,height/7 -60),"5")
    buttonnum5.draw(roundwindow)
    
    question.draw(roundwindow)
    click = roundwindow.getMouse()
    clickX = click.getX()
    clickY = click.getY()
    #checks where click is
    if width/3-50<=clickX<= width/3+50 and height*5/7-60<clickY<height*5/7+60:
        button1.undraw()
        button1.setFill("green")
        button1.draw(roundwindow)
        time.sleep(1)
        roundwindow.close()
        return 1
    elif width*2/3-50<=clickX<= width*2/3+50 and height*5/7-60<clickY<height*5/7+60:
        button2.undraw()
        button2.setFill("green")
        button2.draw(roundwindow)
        time.sleep(1)
        roundwindow.close()
        return 2
    elif width/3-50<=clickX<= width/3+50 and height*3/7-60<clickY<height*3/7+60:
        button3.undraw()
        button3.setFill("green")
        button3.draw(roundwindow)
        time.sleep(1)
        roundwindow.close()
        return 3
    
    elif width*2/3-50<=clickX<= width*2/3+50 and height*3/7-60<clickY<height*3/7+60:
        button4.undraw()
        button4.setFill("green")
        button4.draw(roundwindow)
        time.sleep(1)
        roundwindow.close()
        return 4
    elif width/2-50<=clickX<=width/2+50 and height/7-50<=clickY<= height/7+50:
        button5.undraw()
        button5.setFill("green")
        button5.draw(roundwindow)
        time.sleep(1)
        roundwindow.close()
        return 5
    click = roundwindow.getMouse()
"""
Description: Will run the game using the other major methods
Parameters:
        rounds - number of rounds the users want to play
	win - window that has the board to draw circles in
Returns: None
Plan: I will use a while loop that will keep on looping until checkScore returns
True → one of the players won. In the loop, I will use .getMouse() to get the
turn on the player and then I will use the playerMove method to track the move
of the player in the game. I will also use checkScore to show the number of
moves in the game and I will use clickCircle to draw the circles on the board
based on the moves of the players. 
"""
def connect4(rounds, win):
    width = win.getWidth()
    height = win.getHeight()
    player1Score = Text(Point(width/10 + 60, height*0.9),"0")
    player2Score = Text(Point(width*0.8 + 60, height*0.9), "0")
    player1Score.draw(win)
    player2Score.draw(win)
    score1 = 0
    score2 = 0
    for i in range(rounds):
        makeBoard(win)
        board = ["BBBBBBB","BBBBBBB","BBBBBBB","BBBBBBB","BBBBBBB",\
                 "BBBBBBB"]
        boardHeight = height/7*6
        colHeightList = [boardHeight/7,boardHeight/7, boardHeight/7, boardHeight/7, \
                         boardHeight/7, boardHeight/7, boardHeight/7]
        widthLength = width/8
        circleRadiusHalf = width/14.0 - 10 /2
        turn = 0
    
        #checks if any of the players have won yet
        while checkScore(board) == None:
            click = win.getMouse()
            for j in range(7):
                if widthLength - circleRadiusHalf < click.getX() < widthLength + \
                   circleRadiusHalf:
                    #had to fix it the hard way --> fix it so that it works on any
                    if colHeightList[j] < boardHeight-50:
                        turn += 1
                        playerMove(j, colHeightList[j] / (boardHeight/7)-1, turn,board)
                        clickCircle(turn, j+1, colHeightList[j], win)
                        colHeightList[j] += boardHeight/7
                widthLength += width/8
            widthLength = width/8
        #adds to the score for the first player
        if checkScore(board) == "X":
            score1 += 1
            winner = Text(Point(width/2 + 30, height-20),"Player 1 Wins The Round!")
            winner.setSize(20)
            player1Score.undraw()
            player1Score = Text(Point(width/10 + 60, height*0.9),"{}".format(score1))
            player1Score.draw(win)
            winner.draw(win)
            time.sleep(3)
            winner.undraw()

        #adds to the score for the second player
        else:
            score2 += 1
            winner = Text(Point(width/2 + 30, height-20), "Player 2 Wins The Round!")
            winner.setSize(20)
            player2Score.undraw()
            player2Score = Text(Point(width*0.8 + 60, height*0.9), "{}".format(score2))
            winner.draw(win)
            player2Score.draw(win)
            time.sleep(3)
            winner.undraw()
            
        #checks if they played all the rounds
        if i + 1 == rounds:
            if score1 > score2:
                winner = Text(Point(width/2 + 30, height-20), "Player 1 Wins The Game!")
                winner.setSize(20)
                winner.draw(win)
                time.sleep(5)
                win.close()
            else:
                winner = Text(Point(width/2 + 30, height-20), "Player 2 Wins The Game!")
                winner.setSize(20)
                winner.draw(win)
                time.sleep(5)
                win.close()

"""
Description: Tracks the move of the players
Parameters:
	col - column of the move
	row - row of the move
	turn - one of the players' turn
	board - board of the game with each players’ moves but as a 2D list
Returns: None
Plan: I will check for the coordinates of the click and depending on where it
is on the window, the board 2D list will change to its corresponding spot.
Then it will return board so that checkScore could use it.
"""
def playerMove(col, row, turn, board):
    # O is yellow and X is red
    turnList = ["O", "X"]
    if row < 6 and col < 7:
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

"""
Description: Checks if one of the players have won
Parameters: 
	board - board of the game with each players’ moves but as a 2D list
Returns:
	letter - letter that corresponds to one of the players that won
	None - none of the players have won yet
Plan: I will loop through each index to check if there is 4 of the same symbol
in a line up, diagonally, and to the sides. If there is, then it will return
True. If the loop finishes, then it will return False.
"""
def checkScore(board):
    for i in range(len(board)):
        for j in range(7):
            letter = board[i][j]
            if letter != "B":
                #checks vertically for 4
                if i < 4:
                    if letter == board[i+1][j] == board[i+2][j] ==board[i+3][j]:
                        return letter
                #checks horizontally to the right for 4
                if j < 4:
                    if letter == board[i][j+1] == board[i][j+2]== board[i][j+3]:
                        return letter
                #checks diagonally (up right) for 4
                if j < 4 and i < 4:
                    if letter == board[i+1][j+1] == board[i+2][j+2] == \
                       board[i+3][j+3]:
                        return letter
                #checks diagonally (up left) for 4
                if j > 2 and i < 3:
                    if letter == board[i+1][j-1] == board[i+2][j-2] == \
                       board[i+3][j-3]:
                        return letter         
    return None
"""
Description: Draws the circle on the board based on the player’s move
Parameters: 
	turn - turn of one of the players
	col - column of the move of one of the players
	circleHeight - height of the center of the circle
	win - window that has the board to draw circles in
Returns: None
Plan: I will check for the coordinates of the click and based on where it is,
I will draw a circle in one of the spots of the board. 
"""
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
