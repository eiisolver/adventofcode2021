from collections import namedtuple
from enum import Enum

class M(Enum):
    """Types of moves"""
    ROOM_ROOM = 1
    ROOM_HALL = 2
    HALL_ROOM = 3

# Used when undoing a move
opposite = {M.ROOM_ROOM: M.ROOM_ROOM, M.ROOM_HALL: M.HALL_ROOM, M.HALL_ROOM: M.ROOM_HALL}

# fr/to: from/to, room index for rooms, hall index for halls
Move = namedtuple('Move', 'type fr to')

class Board(object):
    rest_spots = [0, 1, 3, 5, 7, 9, 10] # Indices in the hallway where amphipods can stop
    cost = [1, 10, 100, 1000] # Energy cost for moving an amphipod
    hall_index = [2, 4, 6, 8] # Map from room index to hallway index

    def __init__(self, room):
        self.room = room
        self.hallway = 11 * [-1]
        self.N = len(room[0])
        self.nr_empty = 4 * [0] # for every room the number of empty spots
        self.precalculated_stops = dict()
        self._precalc_stops()

    def move(self, typ: M, fr: int, to: int) -> int:
        """Performs a move (also used to undo a move), returns used energy"""
        if typ == M.HALL_ROOM:
            # from a hall
            t = self.hallway[fr]
            assert(t>=0)
            self.hallway[fr] = -1
            steps = 0
            hall_ix = fr
        else:
            # from a room
            e = self.nr_empty[fr]
            t = self.room[fr][e]
            self.room[fr][e] = -1
            steps = e + 1
            hall_ix = Board.hall_index[fr]
            self.nr_empty[fr] += 1
        assert(t >= 0)
        if typ == M.ROOM_HALL:
            # to a hall
            self.hallway[to] = t
            steps += abs(to - hall_ix)
        else:
            # to a room
            steps += abs(hall_ix - Board.hall_index[to]) + self.nr_empty[to]
            self.nr_empty[to] -= 1
            self.room[to][self.nr_empty[to]] = t
        return Board.cost[t] * steps

    def is_hall_free(self, fr: int, to: int) -> bool:
        """Checks if hallway is free in interval (not including fr) fr..to"""
        assert(fr != to)
        step = 1 if to > fr else -1
        for i in range(fr + step, to, step):
            if self.hallway[i] >= 0:
                return False
        return True

    def contains_only(self, t: int) -> bool:
        """Checks if room t only contains amphipods of type t"""
        for i in range(self.nr_empty[t], self.N):
            if self.room[t][i] != t:
                return False
        return True

    def is_complete(self) -> bool:
        """Checks if all amphipods are at their final position"""
        for t in range(4):
            if self.nr_empty[t] > 0 or not self.contains_only(t):
                return False
        return True

    def gen_moves(self):
        moves = []
        # Check moves from hallway
        for ix in Board.rest_spots:
            t = self.hallway[ix]
            if t < 0: continue
            if self.is_hall_free(ix, Board.hall_index[t]) and self.contains_only(t):
                # No need to check other moves
                return [Move(M.HALL_ROOM, ix, t)]
        # Generate moves from rooms
        for r in range(3,-1,-1):
            e = self.nr_empty[r]
            if e >= self.N: continue
            t = self.room[r][e]
            if r == t and self.contains_only(t): continue
            fr_ix = Board.hall_index[r]
            to_ix = Board.hall_index[t]
            if self.contains_only(t) and self.is_hall_free(fr_ix, to_ix):
                # can go immediately from room to room; do it
                return [Move(M.ROOM_ROOM, r, t)]
            # Generate room to hall moves, greedily (energy effective moves first)
            for hall_ix in self.precalculated_stops[(r, t)]:
                if self.hallway[hall_ix] < 0 and self.is_hall_free(fr_ix, hall_ix):
                    moves.append(Move(M.ROOM_HALL, r, hall_ix))
        return moves

    def estimated_required_energy(self) -> int:
        """Returns a lower bound for the required energy for remaining moves"""
        energy = 0
        for ix, t in enumerate(self.hallway):
            if t >= 0:
                energy += Board.cost[t] * (abs(Board.hall_index[t] - ix) + 1)
        for r in range(4):
            for ix in range(self.nr_empty[r], self.N):
                t = self.room[r][ix]
                if t != r:
                    energy += Board.cost[t] * (ix + 2 + 2 * abs(r - t))
        return energy

    def _precalc_stops(self):
        """
        Calculates the order of stops for moving from room r to room t.
        Energy effective moves are generated first
        """
        for r in range(4):
            for t in range(4):
                fr_ix = Board.hall_index[r]
                to_ix = Board.hall_index[t]
                # Generate room to hall moves, greedily (energy effective moves first)
                min_ix = min(fr_ix, to_ix)
                max_ix = max(fr_ix, to_ix)
                # Stops between min_ix..max_ix do not lead to any deviation when moving from r to t; try these first
                stops = [ ix for ix in range(min_ix + 1, max_ix, 2)]
                for i in range(1, 9, 2):
                    if min_ix - i > 0:
                        stops.append(min_ix - i)
                    elif min_ix - i == -1:
                        stops.append(0)
                    if max_ix + i < 10:
                        stops.append(max_ix + i)
                    elif max_ix + i == 11:
                        stops.append(10)
                self.precalculated_stops[(r, t)] = stops

    def print(self):
        s = 'ABCD.'
        hallway = [s[i] for i in self.hallway]
        print(''.join(hallway))
        for i in range(self.N):
            h = [s[self.room[j][i]] for j in range(4)]
            print(f'  {h[0]} {h[1]} {h[2]} {h[3]}')


def parse(lines):
    rooms = []
    for r in range(4):
        room = []
        rooms.append(room)
        for depth in range(len(lines)):
            v = lines[depth][3+2*r]
            room.append(ord(v) - ord('A'))
    return rooms

class Solver(object):

    def __init__(self):
        self.best_energy = 1e9
        self.nodes = 0
        self.move_stack = []
        self.best_solution = []

    def search(self, b: Board, energy: int):
        self.nodes += 1
        estimate = b.estimated_required_energy()
        if energy + estimate >= self.best_energy:
            # Fail early, best score cannot be reached
            return
        moves = b.gen_moves()
        if not moves:
            if b.is_complete() and energy < self.best_energy:
                print('New best solution, energy: ', energy)
                self.best_solution = self.move_stack.copy()
                self.best_energy = energy
        for m in moves:
            e = b.move(m.type, m.fr, m.to)
            self.move_stack.append((m, e))
            self.search(b, energy + e)
            self.move_stack.pop()
            e2 = b.move(opposite[m.type], m.to, m.fr)
            assert(e == e2)

    def solve(self, lines):
        rooms = parse(lines)
        b = Board(rooms)
        print('Solve:')
        b.print()
        self.best_energy = 1e9
        self.nodes = 0
        self.search(b, 0)
        print('Best energy:', self.best_energy, ', nodes searched:', self.nodes, ', #moves required in best solution:', len(self.best_solution))
        show_solution = False
        if show_solution:
            print('Best solution:')
            b.print()
            for m, e in self.best_solution:
                print(m, ', energy:', e)
                e2 = b.move(m.type, m.fr, m.to)
                assert(e == e2)
                b.print()

lines = open('23_input.txt', 'r').read().splitlines()

part1_lines = lines[2:4]
Solver().solve(part1_lines)

line1 = '  #D#C#B#A#'
line2 = '  #D#B#A#C#'
part2_lines = [lines[2], line1, line2, lines[3]]
Solver().solve(part2_lines)
