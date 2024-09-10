import pygame
x= pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")
pygame.display.update()
# Game specific variables
gameExit = False
gameOver = False
while not gameExit:
    for event in pygame.event.get():
        print(event)

pygame.quit()
print(x)