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


# Resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,46)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0)    # we will fill background color as black
black = pygame.Color(0,0,0)

gameClock = pygame.time.Clock()

def checkCollision(posA,As ,posB , Bs):    # As is the size of a and Bs is the size of b
    if(posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

# to check the boundaries  here we are not limiting boundaries like it can pass through screen and come from other side

def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x < 0):    # this will be checked when some part of snake is on other side and some on opposite side
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0):   # this also same half half
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE
        
        
        #the snake food is called apple
class Apple:
    def __init__(self, x ,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")     # color of food

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)
        
        
class segment:
    # initially snake will move in up direction
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]
        self.color = "white"
 
        
class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]
        self.stack =[]   # initially it will be empty
        self.stack.append(self)
        blackBox = segment(self.x , self.y + SEPARATION)
        blackBox.direction = KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)
