from day2ex1 import parse_cubes_file


def how_many_cubes_needed(game: list) -> dict:
    """
    Returns the number of cubes needed for each color in the game.
    Example of output: {'green': 5, 'red': 3, 'blue': 2}
    """
    cubes = {}
    for round in game:
        for color in round:
            if color in cubes:
                if round[color] > cubes[color]:
                    cubes[color] = round[color]
            else:
                cubes[color] = round[color]
    return cubes


def power_of_set(cubes: dict) -> int:
    """
    Returns the power of the set of cubes. The power is equal to the
    number of cubes of each color multiplied together.
    """
    power = 1
    for color in cubes:
        power *= cubes[color]
    return power


def cubes_needed_list(games: list) -> list:
    """
    Returns a list of the cubes needed for each game.
    """
    cubes_needed = []
    for game in games:
        cubes_needed.append(how_many_cubes_needed(game))
    return cubes_needed


def power_of_set_list(games: list) -> list:
    """
    Returns a list of the powers of the sets of cubes for each game.
    """
    cubes_needed = cubes_needed_list(games)
    powers = []
    for cubes in cubes_needed:
        powers.append(power_of_set(cubes))
    return powers


if __name__ == '__main__':
    cubes = parse_cubes_file('cubes.txt')
    powers_list = power_of_set_list(cubes)
    print(sum(powers_list))
