best = -1
best_alpha = -50


def best_score(move, alpha, cur_player):
    global best_alpha
    if cur_player and alpha > best_alpha:
        best_alpha = alpha
        global best
        best = move
