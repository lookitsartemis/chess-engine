from pieces import Piece

class Board:
    def __init__(self):
        self.board = self.create_board()  # Init board with pieces
        
    def create_board(self):
        # Create an 8x8 board with pieces in starting positions
        board = [[None for _ in range(8)] for _ in range(8)]  # Initialize to 8x8
        
        # Add pawns
        for col in range(8):
            board[1][col] = Piece("black", "pawn")
            board[6][col] = Piece("white", "pawn")
        
        # Add other pieces
        piece_order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for col, piece in enumerate(piece_order):
            board[0][col] = Piece("black", piece)
            board[7][col] = Piece("white", piece)
                
        return board
    
    def draw(self, screen):
        # Draw all pieces on the board
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None:
                    piece.draw(screen, (col, row))
