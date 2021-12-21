
from functools import lru_cache

def practice(p1, p2):
    pos = [p1-1, p2-1]
    score = [0, 0]
    turn = 0
    p = 0
    while True:
        pos[p] = (pos[p] + 9*turn + 6) % 10
        score[p] += pos[p] + 1
        turn += 1
        if score[p] >= 1000:
            break
        p = 1-p
    print('losing player * dice rolled:', score[1-p] * 3 * turn)

@lru_cache(maxsize=None)
def dirac(p, pos, score):
    if score[0] >= 21:
        return (1, 0)
    elif score[1] >= 21:
        return (0, 1)
    result = [0, 0]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                pos2 = [pos[0], pos[1]]
                score2 = [score[0], score[1]]
                pos2[p] = (pos[p] + 3 + i + j + k) % 10
                score2[p] = score[p] + pos2[p] + 1
                p1_wins, p2_wins = dirac(1-p, tuple(pos2), tuple(score2))
                result[0] += p1_wins
                result[1] += p2_wins
    return result

def dirac_game(p1, p2):
    p1_wins, p2_wins = dirac(0, (p1-1, p2-1), (0, 0))
    print(f'p1 wins: {p1_wins}, p2 wins: {p2_wins} -> max: {max(p1_wins, p2_wins)}')

pos1, pos2 = 8, 9 # Real
# pos1, pos2 = 4, 8 # Test
practice(pos1, pos2)

dirac_game(pos1, pos2)
