import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
SPEED = 500  # Milliseconds per move

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tetrominoes
tetrominoes = [
    [[1, 1, 1, 1]],  # I-Piece
    [[1, 1], [1, 1]],  # O-Piece
    [[1, 1, 1], [0, 1, 0]],  # T-Piece
    [[1, 1, 1], [1, 0, 0]],  # L-Piece
    [[1, 1, 1], [0, 0, 1]],  # J-Piece
    [[1, 1, 0], [0, 1, 1]],  # S-Piece
    [[0, 1, 1], [1, 1, 0]]  # Z-Piece
]

tetromino_colors = [CYAN, YELLOW, GREEN, PURPLE, RED, BLUE, ORANGE]

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game")

# Initialize variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_tetromino = None
current_tetromino_color = None
current_x, current_y = 0, 0
score = 0

# Functions


def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface, tetromino_colors[cell - 1], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                )


def new_tetromino():
    global current_tetromino, current_tetromino_color, current_x, current_y
    current_tetromino = random.choice(tetrominoes)
    current_tetromino_color = random.choice(tetromino_colors)
    current_x = GRID_WIDTH // 2 - len(current_tetromino[0]) // 2
    current_y = 0


def move_tetromino(dx, dy):
    global current_x, current_y
    new_x = current_x + dx
    new_y = current_y + dy

    if is_valid_move(current_tetromino, new_x, new_y):
        current_x = new_x
        current_y = new_y
        return True
    return False


def rotate_tetromino():
    global current_tetromino
    current_tetromino = list(zip(*current_tetromino[::-1]))


def is_valid_move(tetromino, x, y):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[0])):
            if tetromino[row][col]:
                grid_row = y + row
                grid_col = x + col
                if (
                    grid_row >= GRID_HEIGHT
                    or grid_col < 0
                    or grid_col >= GRID_WIDTH
                    or grid[grid_row][grid_col]
                ):
                    return False
    return True


def place_tetromino():
    for row in range(len(current_tetromino)):
        for col in range(len(current_tetromino[0])):
            if current_tetromino[row][col]:
                grid[current_y + row][current_x + col] = tetromino_colors.index(current_tetromino_color) + 1


def check_lines():
    global grid, score
    full_lines = [i for i, row in enumerate(grid) if all(row)]
    for row in full_lines:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)
        score += 100


def game_over():
    pygame.quit()
    quit()

# Main game loop


running = True
fall_time = 0
new_tetromino()

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_tetromino(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_tetromino(1, 0)
            elif event.key == pygame.K_DOWN:
                move_tetromino(0, 1)
            elif event.key == pygame.K_UP:
                rotate_tetromino()

    # Move tetromino down
    current_time = pygame.time.get_ticks()
    if current_time - fall_time > SPEED:
        if not move_tetromino(0, 1):
            place_tetromino()
            check_lines()
            new_tetromino()
            if not is_valid_move(current_tetromino, current_x, current_y):
                game_over()
        fall_time = current_time

    # Draw the background
    screen.fill(BLACK)

    # Draw the grid
    draw_grid(screen, grid)

    # Draw the current tetromino
    for row in range(len(current_tetromino)):
        for col in range(len(current_tetromino[0])):
            if current_tetromino[row][col]:
                pygame.draw.rect(
                    screen,
                    current_tetromino_color,
                    ((current_x + col) * GRID_SIZE, (current_y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

    pygame.display.flip()

    clock.tick(30)

# Quit the game
pygame.quit()
