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
WIN_COLOR = (255, 215, 0)  # Gold color for winner

# Setup display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Tic-tac-toe')

# Initialize game state
board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 'X'
game_over = False
winner = None

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

def draw_x(row, col):
    """Draw an X at the specified position"""
    x = col * CELL_SIZE + CELL_SIZE//2
    y = row * CELL_SIZE + CELL_SIZE//2
    pygame.draw.line(screen, BLACK, (x-50, y-50), (x+50, y+50), 5)
    pygame.draw.line(screen, BLACK, (x+50, y-50), (x-50, y+50), 5)

def draw_o(row, col):
    """Draw an O at the specified position"""
    x = col * CELL_SIZE + CELL_SIZE//2
    y = row * CELL_SIZE + CELL_SIZE//2
    pygame.draw.circle(screen, BLACK, (x, y), 50, 5)

def draw_board():
    """Draw the current board state"""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)

def check_winner():
    """Check if there's a winner"""
    # Check rows
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    
    # Check columns
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def draw_winner():
    """Draw the winner message"""
    if winner:
        font = pygame.font.Font(None, 74)
        text = font.render(f"{winner} wins!", True, WIN_COLOR)
        text_rect = text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2))
        screen.blit(text, text_rect)

def handle_events():
    """Handle Pygame events"""
    global current_player
    global board
    global game_over
    global winner
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            
            # Only place a mark if the cell is empty
            if board[row][col] is None:
                board[row][col] = current_player
                current_player = 'O' if current_player == 'X' else 'X'
                
                # Check for winner after each move
                winner = check_winner()
                if winner:
                    game_over = True

def main():
    """Main game loop"""
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(WHITE)
        draw_grid()
        draw_board()
        draw_winner()
        
        handle_events()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
