import pygame
import chess
import sys
import math

# Khởi tạo pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess AI")


# Định nghĩa các giá trị quân cờ
PIECE_VALUES = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 900
}

# Sửa các tham số màu và font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (80, 80, 80)  # Tạo độ tương phản cao
SQUARE_SIZE = WIDTH // 8
font = pygame.font.SysFont('Segoe UI Symbol', 64)  # Font hỗ trợ Unicode

# Cập nhật mapping Unicode đúng cho các quân
PIECE_SYMBOLS = {
    'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
    'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙'
}

# Hàm để vẽ bàn cờ
def draw_board(screen, board):
    for row in range(8):
        for col in range(8):
            is_light = (row + col) % 2 == 0
            square_color = WHITE if is_light else DARK_GRAY
            pygame.draw.rect(screen, square_color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            piece = board.piece_at(chess.square(col, 7-row))
            if piece:
                text_color = BLACK if is_light else WHITE  # Đảm bảo độ tương phản
                symbol = PIECE_SYMBOLS[piece.symbol()]
                text = font.render(symbol, True, text_color)
                text_rect = text.get_rect(center=(col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2))
                screen.blit(text, text_rect)

# Hàm đánh giá bàn cờ
def evaluate_board(board):
    if board.is_checkmate():
        return 10000 if board.turn else -10000
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            evaluation += value * (-1 if piece.color else 1)
    return evaluation

# Hàm Minimax với Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            evaluation = minimax(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            evaluation = minimax(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval

# Hàm tìm nước đi tốt nhất cho AI
def get_ai_move(board, depth=3):
    best_move = None
    best_value = -math.inf
    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, depth-1, -math.inf, math.inf, False)
        board.pop()
        if value > best_value:
            best_value = value
            best_move = move
    return best_move

# Hàm chính để chạy trò chơi
def main():
    board = chess.Board()
    selected = None
    player_color = chess.WHITE

    while not board.is_game_over():
        if board.turn == player_color:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    col = x // SQUARE_SIZE
                    row = y // SQUARE_SIZE
                    square = chess.square(col, 7-row)
                    piece = board.piece_at(square)
                    
                    if selected:
                        move = chess.Move(selected, square)
                        if move in board.legal_moves:
                            board.push(move)
                            selected = None
                        elif piece and piece.color == player_color:
                            selected = square
                        else:
                            selected = None
                    elif piece and piece.color == player_color:
                        selected = square
        
        else:
            ai_move = get_ai_move(board, depth=3)
            board.push(ai_move)
        
        screen.fill(WHITE)
        draw_board(screen, board)
        if selected:
            pygame.draw.rect(screen, (255, 0, 0), 
                           ((selected % 8)*SQUARE_SIZE, (7 - selected // 8)*SQUARE_SIZE, 
                            SQUARE_SIZE, SQUARE_SIZE), 3)
        pygame.display.flip()

if __name__ == "__main__":
    main()