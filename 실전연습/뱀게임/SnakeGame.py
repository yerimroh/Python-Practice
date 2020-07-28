import pygame

pygame.init() # Initializing

#############################################################
# The node class that composese the snake's body
headSize = 20
class Node(pygame.Rect, Snake):
    def __init__(self, x, y):
        super().__init__(x, y, headSize, headSize) # Initialte the Rect class
##############################################################
# Class that represents the snake
class Snake:
    def __init__(self, nodes):
        self.nodes = nodes

    def growBody(self):
        newNode = Node(nodes[nodes.index(self) - 1].left, nodes[nodes.index(self) - 1].top)


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
background = pygame.image.load("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\background.png")

eatingSound = pygame.mixer.Sound("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\eating sound effect.wav")

apple = pygame.image.load("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\apple.png")
#############################################################
# Snake Setting
snakeSpeed = 0.6

toX = 0
toY = 0

totalApple = 0 # keep track of the number of apples that the snake got

# Snake Head
head = Node((screenWidth / 2 - headSize / 2), (screenHeight / 2 - headSize / 2)) # Create head

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
            elif event.key == pygame.K_LEFT:
                toX -= snakeSpeed
                toY = 0
            elif event.key == pygame.K_UP:
                toY -= snakeSpeed
                toX = 0
            elif event.key == pygame.K_DOWN:
                toY += snakeSpeed
                toX = 0

            # When the player let go of the keyboard (do not move)
        if event.type == pygame.KEYUP and isGameOver == False:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0

    # move around the head
    head.left += int(toX * dt)
    head.top += int(toY * dt)

    ######################################################################
    # Handle game events
    # If the snake collides with any of the edges of the screen
    if head.left > screenWidth - headSize or head.left < -5:
        isGameOver = True
        background = pygame.image.load("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\background.png")
    elif head.top > screenHeight - headSize or head.left < -5:
        isGameOver = True
        background = pygame.image.load("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\background.png")



    #####################################################################
    # Draw components on the screen
    screen.blit(background, (0, 0)) # background

    if isGameOver == False:
        pygame.draw.rect(screen, snakeColor, head)

    pygame.display.update() # update the screen each time


# Exit out from the game
pygame.time.delay(1000)
pygame.quit()

