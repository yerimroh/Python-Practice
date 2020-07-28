import pygame

pygame.init() # Initializing

#############################################################
# The node class that composese the snake's body
headSize = 20
class Node(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, headSize, headSize) # Initialte the Rect class

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
background = pygame.image.load("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\background.png")

eatingSound = pygame.mixer.Sound("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\eating sound effect.wav")

#############################################################
# Snake Setting
snakeSpeed = 0.6

toX = 0
toY = 0

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
            if event.key == pygame.K_RIGHT and not(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                toX += snakeSpeed
            elif event.key == pygame.K_LEFT and not(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                toX -= snakeSpeed
            elif event.key == pygame.K_UP and not(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                toY -= snakeSpeed
            elif event.key == pygame.K_DOWN and not(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                toY += snakeSpeed

            # If the snake collides any of the edges of the screen
        if event.type == pygame.KEYUP and isGameOver == False:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                toX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0

    # move around the head
    head.left += toX * dt
    head.top += toY * dt

        # Draw components on the screen
    screen.blit(background, (0, 0)) # background

    if isGameOver == False:
        screen.blit(head, (head.left, head.right))

    pygame.display.update() # update the screen each time


# Exit out from the game
pygame.time.delay(1000)
pygame.quit()

