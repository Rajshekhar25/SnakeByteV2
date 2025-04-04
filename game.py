import pygame
import sys
import os
import random 
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.seed()

SPEED = 0.36
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE     # keeping food and snake size same
SEPARATION = 10    # separation between two pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1 , "DOWN":2 , "LEFT":3, "RIGHT":4}

# initialise screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.HWSURFACE)

# used hw surface which stands for hardware surface refers to using memory on the video card for storing
# draws as opposed to main memory

