from src.common.file_utils import get_path, read_lines
from collections import deque


def parse_input(filename):
    lines = read_lines(get_path(__file__, filename))
    player1 = deque([int(l) for l in lines[lines.index(
        "Player 1:") + 1:lines.index("Player 2:") - 1]])
    player2 = deque([int(l) for l in lines[lines.index("Player 2:") + 1:]])
    return player1, player2


def part_one(filename: str) -> int:
    player1, player2 = parse_input(filename)

    while player1 and player2:
        one, two = player1.popleft(), player2.popleft()
        if one > two:
            player1 += deque([one, two])
        elif two > one:
            player2 += deque([two, one])
    return get_score(player1) if player1 else get_score(player2)


def part_two(filename: str) -> int:
    player1, player2 = parse_input(filename)

    winning_hand, _ = play_game(player1, player2, set())

    return get_score(winning_hand)


def play_game(player1, player2, seen):

    while player1 and player2:
        if (tuple(player1), tuple(player2)) in seen:
            return (player1, 1)
        seen.add((tuple(player1), tuple(player2)))

        one, two = player1.popleft(), player2.popleft()
        if one <= len(player1) and two <= len(player2):
            _, winner = play_game(
                deque(list(player1)[:one]), deque(list(player2)[:two]), set())
        else:
            winner = 1 if one > two else 2

        if winner == 1:
            player1 += deque([one, two])
        else:
            player2 += deque([two, one])

    return (player1, 1) if player1 else (player2, 2)


def get_score(arr):
    return sum((len(arr) - i) * a for i, a in enumerate(arr))


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
