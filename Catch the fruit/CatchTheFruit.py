# Catch the fruit

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from Fruit import *  # bring in the Fruit class code
from Basket import * # bring in the Basket class code
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
LIME = (0, 255,0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)


# 4 - Load assets: image(s), sounds, etc.
oDisplay = pygwidgets.DisplayText(window, (WINDOW_WIDTH -120, 10), '', fontSize=30)

# 5 - Initialize variables
oBasket = Basket(window, WINDOW_WIDTH, WINDOW_HEIGHT)

oFruitList = [
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'apple'),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'banana'),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'cherry'),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'grapes'),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'strawberry'),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'pear')]

oRestartButton = pygwidgets.TextButton(window, (5, 5), 'Restart')

score = 0


# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):  # ckicked on the Restart button
            print('User pressed the Restart button')
            score = 0
            oDisplay.setText('Score: ' + str(score))
            for oFruit in oFruitList:
                oFruit.reset()

    # Add "continuous mode" code here to check for left or right arrow keys
    # If you get one, tell the basket to move itself appropriately
        
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                oBasket.move("left") 
            elif event.key == pygame.K_RIGHT:
                oBasket.move("right") 


    # 8 - Do any "per frame" actions+
    for oFruit in oFruitList:
        oFruit.update()

        basketRect = oBasket.getRect()
        fruitRect = oFruit.getRect()
        if basketRect.colliderect(fruitRect):
            print('Fruit has collided with the basket')
            points = oFruit.getPoints()
            score += points
            oDisplay.setText('Score: ' + str(score))

    # 9 - Clear the screen before drawing it again
    window.fill(LIME)
    
    # 10 - Draw the screen elements
    for oFruit in oFruitList:
        oFruit.draw()   # tell each ball to draw itself

    oRestartButton.draw()
    oBasket.draw()
    oDisplay.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount

