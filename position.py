class Position:
    WIDTH = 7
    HEIGHT = 6

    def __init__(self):
        self.current_position = 0
        self.mask = 0
        self.moves = 0

    def can_play(self, col: int):
        return self.mask & self.top_mask(col) == 0

    def play(self, col: int):
        self.current_position ^= self.mask
        self.mask |= self.mask + self.bottom_mask(col)
        self.moves += 1

    def play_sequence(self, seq: str):
        for i, move in enumerate(seq):
            col = int(move) - 1
            if col < 0 or col >= self.WIDTH or not self.can_play(col) or self.is_winning_move(col):
                return i
            self.play(col)
        return len(seq)

    def is_winning_move(self, col: int):
        pos = self.current_position
        pos |= (self.mask + self.bottom_mask(col)) & self.column_mask(col)
        return self.alignment(pos)

    def nb_moves(self):
        return self.moves

    def key(self):
        return self.current_position + self.mask

    def alignment(self, pos):
        # horizontal
        m = pos & (pos >> (self.HEIGHT + 1))
        if m & (m >> (2 * (self.HEIGHT + 1))):
            return True

        m = pos & (pos >> self.HEIGHT)
        if m & (m >> (2 * self.HEIGHT)):
            return True

        m = pos & (pos >> (self.HEIGHT + 2))
        if m & (m >> (2 * (self.HEIGHT + 2))):
            return True

        m = pos & (pos >> 1)
        if m & (m >> 2):
            return True

        return False

    def top_mask(self, col: int):
        return (1 << (self.HEIGHT - 1)) << col * (self.HEIGHT + 1)

    def bottom_mask(self, col: int):
        return 1 << col * (self.HEIGHT + 1)

    def column_mask(self, col: int):
        return ((1 << self.HEIGHT) - 1) << col * (self.HEIGHT + 1)
