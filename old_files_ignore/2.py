import pygame
x = pygame.init()
screen_width = 900
screen_height = 500
# Colors =>
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("My First Game")
pygame.display.update()
# Game specific variables
gameExit = False
gameOver = False
snake_x = 45
snake_y = 55  # Initial Coordinates of Snake
velocity_x = 10
velocity_y = 10
snake_size = 10
fps = 30  # frames per second
clock = pygame.time.Clock()
# Creating a Game Loop
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [
                     snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
print(x)
