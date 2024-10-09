import pygame
from gui import draw_board
from board import Board

def main():
    # Initialize Pygame-CE
    pygame.init()
    
    # Set up the game window
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Chess Engine") # Window title
    icon = pygame.image.load('resources/images/black_king.png')
    pygame.display.set_icon(icon)
    
    # Create a clock to control frame rate
    clock = pygame.time.Clock()
    running = True # Variable to control the main loop

    # Create the board instance here
    board = Board()  # Create the board once
    
    # Main game loop
    while running:
        for event in pygame.event.get(): # Process event queue
            if event.type == pygame.QUIT: # Check for quit event
                running = False # Stop the loop to close the game
                
        # Draw the board and pieces
        draw_board(screen, board)  # Pass the board to the draw function
        
        # Update the display
        pygame.display.flip()
        
        # Limit the frame rate to 60 FPS
        clock.tick(60)
        
    pygame.quit() # Clean up and close Pygame
    
if __name__ == "__main__":
    main() # Run the main function when the script is executed
