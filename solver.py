import position


class Solver:
    def __init__(self):
        self.node_count = 0

    def negamax(self, p):
        self.node_count += 1  # Increment counter of explored nodes

        if p.nb_moves() == p.WIDTH * p.HEIGHT:  # Check for draw game
            return 0

        for x in range(p.WIDTH):  # Check if current player can win next move
            if p.can_play(x) and p.is_winning_move(x):
                return (p.WIDTH * p.HEIGHT + 1 - p.nb_moves()) // 2

        best_score = -p.WIDTH * p.HEIGHT  # Init the best possible score with a lower bound of score.

        for x in range(p.WIDTH):
            if p.can_play(x):
                p2 = position.Position()
                p2.board = [row[:] for row in p.board]
                p2.height = p.height[:]
                p2.moves = p.moves
                p2.play(x)
                score = -self.negamax(p2)
                if score > best_score:
                    best_score = score

        return best_score

    def solve(self, p, weak=False):
        self.node_count = 0

        return self.negamax(p)

    def get_node_count(self):
        return self.node_count
