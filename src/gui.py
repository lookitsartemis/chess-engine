import pygame

def draw_board(screen, board):
    # Define colors for the chessboard squares
    colors = [pygame.Color("white"), pygame.Color("gray")]
    
    # Loop through the rows and columns of the board
    for row in range(8):
        for col in range(8):
            # Determine which color to use based on the row and column
            color = colors[(row + col) % 2]
            # Draw the square on the screen
            pygame.draw.rect(screen, color, pygame.Rect(col * 80, row * 80, 80, 80))
            
    # Draw all the pieces on the board
    board.draw(screen)
