import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
dx, dy = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0

    x, y = snake[0]
    new_x, new_y = x + dx, y + dy
    if new_x == food[0] and new_y == food[1]:
        snake.insert(0, food)
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.insert(0, (new_x, new_y))
        snake.pop()

    if (
        new_x < 0
        or new_x >= GRID_WIDTH
        or new_y < 0
        or new_y >= GRID_HEIGHT
        or (new_x, new_y) in snake[1:]
    ):
        running = False

    screen.fill(WHITE)

    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    pygame.display.flip()

    pygame.time.Clock().tick(SNAKE_SPEED)

pygame.quit()
