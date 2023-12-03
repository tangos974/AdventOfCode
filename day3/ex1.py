

def read_file(filename):
    """Reads a file and returns a list of lines"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


symbols = ['*', '/', '+', '-', '=', '&', '#', '%', '@', '$']
lines = read_file('parts.txt')


def is_adjacent_symbol(index: int, line_number: int, lines: list[str]) -> bool:
    """
    Given a line number and an index, returns True if the character at the
    given index is adjacent to a symbol in the given line, False otherwise.
    A character is adjacent to a symbol if the symbol is directly left, right,
    below or above the character, or in diagonals.
    """

    max_index = len(lines[line_number]) - 1
    max_line_number = len(lines) - 1

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif line_number + i < 0 or line_number + i > max_line_number:
                continue
            elif index + j < 0 or index + j > max_index:
                continue
            elif lines[line_number + i][index + j] in symbols:
                return True
    return False


def get_number_size(index_first_digit: int, line_number: int, lines: list[str]) -> int:
    """
    Given the index of the first digit in a number, returns the number of
    digits in the number.
    """

    if lines[line_number][index_first_digit].isdigit() == 0:
        return 0

    max_index = len(lines[line_number]) - 1
    i = 0
    while index_first_digit + i <= max_index and lines[line_number][index_first_digit + i].isdigit():
        i += 1
    return i


def is_number_adjacent_symbol(index: int, line: int, lines: list[str]) -> bool:
    """
    Given an index and a line number corresponding to the first digit of a number,
    returns True if any digits of the number are adjacent to a symbol, False otherwise.
    """

    for i in range(get_number_size(index, line, lines)):
        if is_adjacent_symbol(index + i, line, lines):
            return True
    return False


def get_number(index: int, line: int, lines: list[str]) -> int:
    """
    Given an index and a line number corresponding to the first digit of a number,
    returns the number.
    """
    number_str = ""
    size = get_number_size(index, line, lines)
    i = 0
    while i < size:
        number_str += lines[line][index + i]
        i += 1
    return int(number_str)


def main():
    res = 0
    can_add = False
    for line in lines:
        i = 0
        while i < len(line):
            if line[i].isdigit():
                for j in range(get_number_size(i, lines.index(line), lines)):
                    if is_adjacent_symbol(i + j, lines.index(line), lines):
                        can_add = True
                if can_add:
                    res += get_number(i, lines.index(line), lines)
                    i += get_number_size(i, lines.index(line), lines)
                can_add = False
            i += 1
    print(res)


if __name__ == '__main__':
    main()