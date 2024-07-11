import time
import position
import solver
import best_move


def get_time_microsec():
    return int(time.time() * 1000000)


def main():
    s = solver.Solver()
    p = position.Position()

    sequence = input("Get sequence")
    p.play_sequence(sequence)

    start_time = get_time_microsec()
    score = s.solve(p)
    end_time = get_time_microsec()

    print(sequence + "  Score: " + str(score) + "  Node Count: " + str(s.get_node_count()) + "  Time:" + str(
        end_time - start_time) + "  Best Move: " + str(best_move.best))


if __name__ == "__main__":
    main()
