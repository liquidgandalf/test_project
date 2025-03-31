import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (50, 50, 50)

# Setup display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Tic-tac-toe')

def draw_grid():
    """Draw the game grid"""
    for i in range(1, GRID_SIZE):
        # Vertical lines
        pygame.draw.line(screen, GRID_COLOR, 
                        (i * CELL_SIZE, 0), 
                        (i * CELL_SIZE, WINDOW_SIZE), 2)
        # Horizontal lines
        pygame.draw.line(screen, GRID_COLOR, 
                        (0, i * CELL_SIZE), 
                        (WINDOW_SIZE, i * CELL_SIZE), 2)

def main():
    """Main game loop"""
    running = True
    
    while running:
        screen.fill(WHITE)
        draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the click
                x, y = event.pos
                # Convert to grid coordinates
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                print(f"Clicked cell: {row}, {col}")  # For debugging
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
