import pygame
x = pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")
pygame.display.update()
# Game specific variables
gameExit = False
gameOver = False

# Creating a Game Loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
pygame.quit()
print(x)
