import pygame

pygame.init()

#############################################################
# The node class that composese the snake's body
class Node(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20) # Initialte the Rect class

##############################################################
# Screen setting
screenWidth = 460
screenHeight = 640

screen =pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Snake Game") # The title of the game

##############################################################
# Other settings
gameFont = pygame.font.Font(None, 30) # Game Font


##############################################################
# Load images
background = pygame.image.load("C:\\Users\\yerim\\Desktop\\Code learning\\Python\\실전연습\\뱀게임\\background.png")



##############################################################
# Game Loop
isRunning = True
while(isRunning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:




    # Draw components on the screen
    screen.blit(background, (0, 0)) # background

    pygame.display.update() # update the screen each time


# Exit out from the game
pygame.time.delay(1000)
pygame.quit()

