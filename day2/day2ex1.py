def parse_cubes_file(filename: str) -> list:
    """
    Parses the cubes file and returns a list of list of dictionaries.
    Each dictionary contains the number of green, red, and blue cubes
    for a round in a game. Rounds are separated by a ';'.
    Each game is separated by a newline. Example output:
    [[{'green': 5, 'red': 3, 'blue': 2},
    {'green': 2, 'red': 5, 'blue': 3},
    {'green': 12, 'red': 3, 'blue': 9}],
    ...]
    """
    games = []
    with open(filename) as f:
        for line in f:
            games.append(parse_game(line))
    return games


def parse_game(line: str) -> list:
    """
    Parses a line of text and returns a list of dictionaries.
    Each dictionary contains the number of green, red, and blue cubes
    for a round in a game. Rounds are separated by a ';'.
    Each game is separated by a newline.
    Example output:
    [{'green': 5, 'red': 3, 'blue': 2},
    {'green': 2, 'red': 5, 'blue': 3},
    {'green': 12, 'red': 3, 'blue': 9}]
    """
    cubes = []
    # Remove the beginning of the line 'Game game_number: '
    line = line.split(': ')[1]
    for round in line.split(';'):
        cubes.append(parse_round(round))
    return cubes


def parse_round(line: str) -> dict:
    """
    Parses a line of text and returns a dictionary.
    Each dictionary contains the number of green, red, and blue cubes
    for a round in a game.
    Example of output: {'green': 5, 'red': 3, 'blue': 2}
    """
    cubes = {}
    for color in line.split(', '):
        cubes[color.split()[1].strip()] = int(color.split()[0])
    return cubes


def game_possible_cubes(cubes: dict, game_number: int, games: list) -> bool:
    """
    Returns True if the game with given id is possible with the given cubes,
    False otherwise. A game is possible given a set of cubes if, for each color
    in the game, the amount of cube is not superior to the amount in the cubes
    set.
    """
    for round in games[game_number]:
        for color in round:
            if round[color] > cubes[color]:
                return False
    return True


def which_games_possible(cubes: dict, games: list) -> list:
    """
    Returns a list of the ids of the games that are possible
    with the given cubes. Ids start at 1.
    """
    possible_games = []
    for i in range(len(games)):
        if game_possible_cubes(cubes, i, games):
            possible_games.append(i + 1)
    return possible_games


if __name__ == '__main__':
    games_list = parse_cubes_file('cubes.txt')
    cubes = {'green': 13, 'red': 12, 'blue': 14}
    print(which_games_possible(cubes, games_list))
    print(sum(which_games_possible(cubes, games_list)))
