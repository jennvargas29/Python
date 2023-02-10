import pygame
from pygame.locals import *
import pygwidgets
import random


# Basket class
class Basket():

    def __init__(self, window, windowWidth, windowHeight, ):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygwidgets.Image(window, (0, 0), 'images/basket.png')

        # A rect is made up of [x, y, width, height]
        startingRect = self.image.getRect()
        self.width = startingRect[2]  # width
        self.height = startingRect[3]  # height

        self.halfHeight = self.height / 2
        self.halfWidth = self.width / 2

        self.x = self.windowWidth / 2
        self.y = windowHeight - self.height - 20
        self.maxX = self.windowWidth - self.width
        self.image.setLoc((self.x, self.y))

        # Choose speed in the x direction
        self.xSpeed = 8

    def move(self, leftOrRight):
    # Get the current position of the basket
        x, y = self.image.getLoc()
    
    # Calculate the new position of the basket
        if leftOrRight == "left":
            x -= self.xSpeed
        elif leftOrRight == "right":
            x += self.xSpeed
        
    # Restrict the basket to stay within the window
        if x < 0:
            x = 0
        elif x > self.maxX:
            x = self.maxX
        
    # Set the new position of the basket
        self.image.setLoc((x, y))

    def getRect(self):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return myRect


    def draw(self):
        self.image.draw()
