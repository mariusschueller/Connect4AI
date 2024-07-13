import position
import best_move
import transposition_table

columnOrder = [0] * position.Position.WIDTH
for i in range(position.Position.WIDTH):
    columnOrder[i] = position.Position.WIDTH // 2 + (1 - 2 * (i % 2)) * (i + 1) // 2

transTable = transposition_table.TranspositionTable(8388593)


class Solver:

    def __init__(self):
        self.node_count = 0
        self.best_move = None

    def negamax(self, p, alpha, beta):
        self.node_count += 1  # Increment counter of explored nodes

        if p.nb_moves() == p.WIDTH * p.HEIGHT:  # Check for draw game
            return 0

        for x in range(p.WIDTH):  # Check if current player can win next move
            if p.can_play(x) and p.is_winning_move(x):
                return (p.WIDTH * p.HEIGHT + 1 - p.nb_moves()) // 2

        max = (p.WIDTH * p.HEIGHT - 1 - p.nb_moves()) // 2  # Init the best possible score with a lower bound of score.

        val = transTable.get(p.key())
        if val:
            max = val + p.MIN_SCORE - 1

        if beta > max:
            beta = max
            if alpha >= beta:
                return beta

        for x in range(p.WIDTH):
            if p.can_play(columnOrder[x]):
                p2 = position.Position(not p.cur_player)
                p2.current_position = p.current_position
                p2.mask = p.mask
                p2.moves = p.moves


                p2.play(columnOrder[x])

                score = -self.negamax(p2, -beta, -alpha)

                if score >= beta:
                    return score
                if score > alpha:
                    alpha = score
                    best_move.best_score(columnOrder[x], alpha, p.cur_player)
        transTable.put(p.key(), alpha - p.MIN_SCORE + 1)
        return alpha

    def solve(self, p, weak=False):
        self.node_count = 0
        self.best_move = None
        if weak:
            return self.negamax(p, -1, 1)
        else:
            return self.negamax(p, -position.Position.WIDTH * position.Position.HEIGHT / 2,
                                position.Position.WIDTH * position.Position.HEIGHT / 2)

    def get_node_count(self):
        return self.node_count
