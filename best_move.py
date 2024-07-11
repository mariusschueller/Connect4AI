best = -1
best_alpha = -1


def best_score(move, alpha):
    global best_alpha
    if alpha > best_alpha:
        best_alpha = alpha
        global best
        best = move
