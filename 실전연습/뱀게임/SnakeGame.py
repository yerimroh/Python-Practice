import pygame
import sys

from pygame.locals import *
from random import*

pygame.init() # Initializing

#############################################################
# The node class that composese the snake's body
headSize = 20
class Node(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(int(x), int(y), headSize, headSize) # Initialte the Rect class
##############################################################


# Screen setting
screenWidth = 460
screenHeight = 640

screen =pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Snake Game") # The title of the game

##############################################################
# Other settings
gameFont = pygame.font.Font(None, 30) # Game Font

snakeColor = (55, 120, 120) # color of the snake

clock = pygame.time.Clock() # FPS
##############################################################
# Load sources
background = pygame.image.load("sources\\background.png")

eatingSound = pygame.mixer.Sound("sources\\eating sound effect.wav")

apple = pygame.image.load("sources\\apple.png")
appleSize = apple.get_rect().size 
appleWidth = appleSize[0]
appleHeight = appleSize[1]
appleX = randrange(5, screenWidth - appleWidth)
appleY = randrange(5, screenHeight - appleHeight)
#############################################################
# Snake Setting
snakeSpeed = 0.3

toX = 0
toY = 0

totalApple = 0 # keep track of the number of apples that the snake got

# Snake Head
head = Node((screenWidth / 2 - headSize / 2), (screenHeight / 2 - headSize / 2)) # Create head

# Snake Body
nodes = []
nodes.append(head) # add head to the list before the game loop
direction = None

# method that will grow body each time the snake obtains the apple
def growBody():
    if direction == "LEFT":
        newNode = Node(nodes[len(nodes) - 1].left + headSize, nodes[len(nodes) - 1].top) 
        nodes.append(newNode)
    elif direction == "RIGHT":
        newNode = Node(nodes[len(nodes) - 1].left - headSize, nodes[len(nodes) - 1].top) 
        nodes.append(newNode)
    elif direction == "UP":
        newNode = Node(nodes[len(nodes) - 1].left, nodes[len(nodes) - 1].top + headSize)
        nodes.append(newNode)
    elif direction == "DOWN":
        newNode = Node(nodes[len(nodes) - 1].left, nodes[len(nodes) - 1].top - headSize) 
        nodes.append(newNode)
 
##############################################################
# Game Loop
isRunning = True
isGameOver = False
while(isRunning):
    dt = clock.tick(30) # FPS = 30
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            # Handle keyboard inputs
        if event.type == pygame.KEYDOWN and isGameOver == False:
            if event.key == pygame.K_RIGHT:
                toX += snakeSpeed
                toY = 0
                direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                toX -= snakeSpeed
                toY = 0
                direction = "LEFT"
            elif event.key == pygame.K_UP:
                toY -= snakeSpeed
                toX = 0
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                toY += snakeSpeed
                toX = 0
                direction = "DOWN"

            # When the player let go of the keyboard (do not move)
        if event.type == pygame.KEYUP and isGameOver == False:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                toX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0

    if isGameOver == False and event.type == pygame.KEYDOWN:
        # store the movement to trace the path the head took
        newX = []
        newY = []
        for i in range(0, len(nodes) - 1):
            newX.append(nodes[i].left)
            newY.append(nodes[i].top)

        # move around the head
        head.left += int(toX * dt)
        head.top += int(toY * dt)
        
        # make the body to follow the trace of the path 
        for j in range(0, len(newX)):
            nodes[j + 1].left = newX[j]
            nodes[j + 1].top = newY[j]


    ######################################################################
    # Handle game events
    # If the snake collides with any of the edges of the screen
    if head.left > screenWidth - headSize or head.left < -5:
        isGameOver = True
        background = pygame.image.load("sources\\gameover.png")
    elif head.top > screenHeight - headSize or head.left < -5:
        isGameOver = True
        background = pygame.image.load("sources\\gameover.png")

    appleRect = apple.get_rect() # apple
    appleRect.left = appleX
    appleRect.top = appleY 

    # when the snake obtains the apple
    if head.colliderect(appleRect):
        pygame.mixer.Sound.play(eatingSound)
        appleX = randrange(5, screenWidth - appleWidth)
        appleY = randrange(5, screenHeight - appleHeight) 
        totalApple += 1
        growBody()

    # When the snake head collides with its body
    for node in nodes:
        if head.colliderect(node) and nodes.index(node) > 4:
            isGameOver = True
            background = pygame.image.load("sources\\gameover.png")


    #####################################################################
    # Draw components on the screen
    screen.blit(background, (0, 0)) # background

    if isGameOver == False:
        for node in nodes:
            pygame.draw.rect(screen, snakeColor, node) # draw snake
        screen.blit(apple, (appleX, appleY)) # draw apple
    pygame.display.update() # update the screen each time


# Exit out from the game
pygame.time.delay(1000)
pygame.quit()

