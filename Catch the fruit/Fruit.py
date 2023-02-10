import pygame
from pygame.locals import *
import random
import pygwidgets


# Fruit class
class Fruit():

    def __init__(self, window, windowWidth, windowHeight, fruitType, points=15):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.fruitType = fruitType

        if fruitType == "apple":
            self.image = pygwidgets.Image(window, (0, 0), 'images/apple.png')
        elif fruitType == "banana":
            self.image = pygwidgets.Image(window, (0, 0), 'images/banana.png')
        elif fruitType == "cherry":
            self.image = pygwidgets.Image(window, (0, 0),"images/cherry.png")
        elif fruitType == "grapes":
            self.image = pygwidgets.Image(window, (0, 0),"images/grapes.png")
        elif fruitType == "strawberry":
            self.image = pygwidgets.Image(window, (0, 0),"images/strawberry.png")
        elif fruitType == "pear":
            self.image = pygwidgets.Image(window, (0, 0),"images/pear.png")



        # A rect is made up of [x, y, width, height]
        startingRect = self.image.getRect()
        self.width = startingRect[2]  # width
        self.height = startingRect[3]  # height

        # Choose a random speed in the y direction
        self.ySpeed = random.randrange(5, 9)
        self.maxX = self.windowWidth - self.width
        self.reset()

    def getPoints(self):
        if self.fruitType == "pear":
            return -100
        else:
            return 15



    def reset(self):
        # Pick a random starting position
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(-450, -self.height)
        self.image.setLoc((self.x, self.y))


    def update(self):
        # check for going off screen, move to above the windows
        if self.y > self.windowHeight:
            self.reset()

        # move location
        self.y = self.y + self.ySpeed
        self.image.setLoc((self.x, self.y))



    def getRect(self):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return myRect

    def draw(self):
        self.image.draw()

