class Position:
    WIDTH = 7
    HEIGHT = 6

    def __init__(self):
        self.board = [[0 for _ in range(self.HEIGHT)] for _ in range(self.WIDTH)]  # height and width change
        self.height = [0] * self.WIDTH
        self.moves = 0

    def can_play(self, col: int):
        return self.height[col] < self.HEIGHT

    def play(self, col: int):
        self.board[col][self.height[col]] = 1 + self.moves % 2
        self.height[col] += 1
        self.moves += 1

    def play_sequence(self, seq: str):
        for i, move in enumerate(seq):
            col = int(move) - 1
            if col < 0 or col >= self.WIDTH or not self.can_play(col) or self.is_winning_move(col):
                return i
            self.play(col)
        return len(seq)

    def is_winning_move(self, col: int):
        current_player = 1 + self.moves % 2
        if self.height[col] >= 3 and \
                self.board[col][self.height[col] - 1] == current_player and \
                self.board[col][self.height[col] - 2] == current_player and \
                self.board[col][self.height[col] - 3] == current_player:
            return True

        for dy in [-1, 0, 1]:
            nb = 0
            for dx in [-1, 1]:
                x, y = col + dx, self.height[col] + dx * dy
                while 0 <= x < Position.WIDTH and 0 <= y < Position.HEIGHT and self.board[x][y] == current_player:
                    nb += 1
                    x += dx
                    y += dx * dy
            if nb >= 3:
                return True
        return False

    def nb_moves(self):
        return self.moves
