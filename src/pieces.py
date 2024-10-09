import pygame

class Piece:
    def __init__(self, color, piece_type):
        self.color = color          # Color of the piece (e.g., 'white' or 'black')
        self.piece_type = piece_type  # Type of the piece (e.g., 'pawn', 'knight')

        # Load the corresponding image for the piece
        img_path = f'resources/images/{color}_{piece_type}.png'
        self.image = pygame.image.load(img_path)

        # Resize the image to fit in the 80x80 square
        self.image = pygame.transform.scale(self.image, (80, 80))

    def draw(self, screen, position):
        x, y = position  # Unpack the position tuple (x, y)
        # Draw the piece image on the board at the calculated position
        screen.blit(self.image, (x * 80, y * 80))
