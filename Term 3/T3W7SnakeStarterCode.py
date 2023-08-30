from machine import *
from ssd1306_plus import *
from random import *
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)

joyX = ADC(Pin(26))
joyY = ADC(Pin(27))
joyBtn = Pin(16,Pin.IN,Pin.PULL_UP)

apple = '''
     #  
    #   
  ##### 
 #######
####### 
####### 
 #######
  ##### 
'''

'''
--- Task 1 ---
Modify the readMove function to return the previous move if a new move isn't made
The current code is the code from the crossy road game.
Parameters:
    previousMove - A letter representing the direction the snake is facing.
                The possible values are: "U"-up, "D"-down,"L"-left or "R-right"
Return - A letter representing the direction the snake is facing. If a movement
         isn't currently being given, return the previous move
Tests - There are no specific tests as it is based on the position of the
        joysticks. You can write some tests within the "if inTestMode:" at the
        bottom of this file.
'''
def readMove(previousMove):
    readingX = joyX.read_u16()/32768-1
    readingY = joyY.read_u16()/32768-1
    move = "M"
    if abs(readingX) > abs(readingY):
        if readingX > 0.95:
            move = "R"
        elif readingX < -0.95:
            move = "L"
    else:
        if readingY > 0.95:
            move = "U"
        elif readingY < -0.95:
            move = "D"
    return move

'''
--- Task 2 ---
Implement the moveForward function
Parameters:
    snake - A list of coordinates of the snake with the first element being the
            head of the snake and the last element being the end of the snake.
            example: [(1,2),(2,2),(3,2),(3,1)]
    direction - A letter representing the direction to snake is facing.
                The possible values are: "U"-up, "D"-down,"L"-left or "R-right"
    idealLength - The ideal number of coordinates in the snake list. If the
                  length of snake is less than the ideal length, the last
                  coordinate of the snake should not be removed
Return - An updated snake with a new set of coordinates.
Tests:
moveForward([(1,2),(2,2),(3,2),(3,1)],"U",4) == [(1, 1), (1, 2), (2, 2), (3, 2)]
moveForward([(4,3),(3,3)],"D",5) == [(4, 4), (4, 3), (3, 3)]
moveForward([(0,1),(1,1),(2,1),(3,1),(3,2),(4,2)],"L",6) == [(-1,1),(0,1),(1,1),(2,1),(3,1),(3,2)]
moveForward([(5,4),(4,4),(3,4),(3,5)],"R",5) == [(6, 4), (5, 4), (4, 4), (3, 4), (3, 5)]
'''
def moveForward(snake,direction,idealLength):
    return snake

'''
--- Task 3 ---
Implement the drawSnake function
The grid for the game should be 8 pixels heigh by 8 pixels tall. Each square of
    the snake should be a 6x6 pixel solid box in the middle of the 8x8 grid
    so there is a gap of 2 pixels between each box of the snake.
Parameters:
    snake - A list of coordinates of the snake with the first element being the
            head of the snake and the last element being the end of the snake.
            example: [(1,2),(2,2),(3,2),(3,1)]
Note - The funciton should not call oled.fill(0) or oled.show(). These are done
       outside of the function.
Return - Nothing
Tests - The snake should move to the right of the screen when not in test mode.
'''
def drawSnake(snake):
    pass

'''
--- Task 4 ---
Implement the drawFruits function
The grid for the game should be 8 pixels heigh by 8 pixels tall. The apple
    should be drawn within this box.
Parameters:
    fruit - A coordinate of the fruit
            example: (4,6)
Note - The funciton should not call oled.fill(0) or oled.show(). These are done
       outside of the function.
Hint - You can use the apple defined at the start of this file. Don't forget
       about oled.draw_sprite(sprite,x,y,fillCharacter,clearCharacter).
Return - Nothing
Tests - An apple should appear on the screen when not is test mode.
'''
def drawFruits(fruit):
    pass

'''
--- Task 5 ---
Implement the isSnakeOnFruit function
Parameters:
    snake - A list of coordinates of the snake with the first element being the
            head of the snake and the last element being the end of the snake.
            example: [(1,2),(2,2),(3,2),(3,1)]
    fruit - A coordinate of the fruit
            example: (4,6)
Return - True if the snake is on the fruit or
         False if the snake is not on the fruit
Tests:
isSnakeOnFruit([(1,2),(2,2),(3,2),(3,1)],(3,2)) == True
isSnakeOnFruit([(1,2),(2,2),(3,2),(3,1)],(2,3)) == False
isSnakeOnFruit([(0,1),(1,1),(2,1),(3,1),(3,2),(4,2)],(0,1)) == True
isSnakeOnFruit([(0,1),(1,1),(2,1),(3,1),(3,2),(4,2)],(3,4)) == False
'''
def isSnakeOnFruit(snake,fruit):
    return False

'''
--- Task 6 ---
Implement the findNewFruitPosition function
Parameters:
    snake - A list of coordinates of the snake with the first element being the
            head of the snake and the last element being the end of the snake.
            example: [(1,2),(2,2),(3,2),(3,1)]
Return - A random fruit position within the board which is not on the snake
Note - The bounds of the board are from 0-15 for x and 0-7 for y
Hint - You can use randint(lowerBound, upperBound) to generate random numbers
Tests - There are no specific tests for this task as the result is random
'''
def findNewFruitPosition(snake):
    return (0,0)

'''
--- Task 7 ---
Implement the isSnakeColliding function
Parameters:
    snake - A list of coordinates of the snake with the first element being the
            head of the snake and the last element being the end of the snake.
            example: [(1,2),(2,2),(3,2),(3,1)]
Return - True if two of the coordinates of the snake are the same
         False if all the coordinates of the snake are different
Hint - You only need to check that the head of the snake isn't colliding.
Tests:
isSnakeColliding([(1,2),(2,2),(2,1),(1,1),(1,2)]) == True
isSnakeColliding([(4,3),(3,3)]) == False
isSnakeColliding([(2,1),(3,1),(3,0),(2,0),(2,1),(2,2),(2,2)]) == True
isSnakeColliding([(5,4),(4,4),(3,4),(3,5),(3,6),(2,6)]) == False

'''
def isSnakeColliding(snake):
    return False

'''
--- Task 8 ---
Implement the isSnakeOffScreen function
Parameters:
    snake - A list of coordinates of the snake with the first element being the
            head of the snake and the last element being the end of the snake.
            example: [(1,2),(2,2),(3,2),(3,1)]
Return - True if the snake is out of the coordinates of the screen
         False if the snake is within the coordinates of the screen
Hint - You only need to check that the head of the snake isn't colliding.
Note - The bounds of the board are from 0-15 for x and 0-7 for y
Tests:
isSnakeOffScreen([(0,1),(3,0),(15,3),(6,7),(4,10)]) == False
isSnakeOffScreen([(-1,2),(2,2),(2,1),(1,1),(1,2)]) == True
isSnakeOffScreen([(3,8),(4,4),(3,4),(3,5),(3,6),]) == True
isSnakeOffScreen([(16,4),(4,4),(3,4),(3,5)]) == True
isSnakeOffScreen([(5,-1),(4,4),(2,4),(4,5),(3,4),(2,6)]) == True
'''
def isSnakeOffScreen(snake):
    return False

'''
--- Extension Tasks ---
Once you have completed the game and showed your tutor, pick some
    extension activities or make your own modificaionts to enhance your game.

Easy:
    - Make the type of fruit change by gving it a different sprite.
    - Keep track of the score and display it at then end of the game.
    - Give the snake two eyes on it's head and a triangle for a tail.
    - Make it so the snake can wrap across opposite sides of the screen.
Medium:
    - Add multiple fruits or a random number of fruits.
    - Make the snake continous by connectecting the adjacent squares.
    - Make random walls appear when fruits are eaten. The game ends if
        the snake hits the wall.
    - Add a second type of fruit which decreases the length of the tail.
Hard:
    - Make the fruit fly about as the game moves not fixed to the grid.
    - Add a second opposite snake which mirrors your moves.
    - Requie the snake to get a key to unlock the fruit.
'''

inTestMode = False

if inTestMode:
    print("Testing Mode:")
    ### You can write code here to test your functions.
else:
    snake = [(0,3)]
    fruit = (3,5)
    direction = "R"
    idealLength = 4
    
    while not(isSnakeColliding(snake)) and not(isSnakeOffScreen(snake)):
        endTime = time.ticks_ms() + 500
        while (time.ticks_ms() < endTime):
            direction = readMove(direction)
        snake = moveForward(snake,direction,idealLength)
        
        if isSnakeOnFruit(snake,fruit):
            fruit = findNewFruitPosition(snake)
            idealLength += 1

        oled.fill(0)
        drawSnake(snake)
        drawFruits(fruit)
        oled.show()

