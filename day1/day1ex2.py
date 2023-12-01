with open('calibrations.txt', 'r') as file:
    content = file.read()


digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }


def find_first_digit(line: str) -> str:
    """
    Extracts the first digit from a given line of text.

    If a digit (0, 1, ..., 9) is found before a spelled digit,
    returns the digit. Else, returns the first spelled digit found.
    If no digit is found, returns an empty string.

    Parameters:
    line (str): The line of text from which to extract the digit.

    Returns:
    str: The first digit from the line of text.
    """

    # Iterate through each character in the line
    for i in range(len(line)):

        # If a digit is found before a spelled digit
        if line[i].isdigit():
            return line[i]

        else:
            # If a spelled digit is found
            substring = line[:i+1]
            # Iterate through each spelled digit and digit pair
            for spelled_digit, digit in digits.items():
                # If the spelled digit is found in the substring
                if spelled_digit in substring:
                    return digit

    # If no digit is found
    return ""


def find_last_digit(line: str) -> str:
    """
    Extracts the last digit from a given line of text.

    Iterates through each character in the line in reverse:
    If a digit (0, 1, ..., 9) is found before a spelled digit,
    returns the digit. Else, returns the first spelled digit found.
    If no digit is found, returns an empty string.

    Parameters:
    line (str): The line of text from which to extract the digit.

    Returns:
    str: The last digit from the line of text.
    """

    # Iterate through each character in the line in reverse
    for i in range(len(line) - 1, -1, -1):

        # If a digit is found before a spelled digit
        if line[i].isdigit():
            return line[i]

        else:
            # If a spelled digit is found
            substring = line[i:]
            # Iterate through each spelled digit and digit pair
            for spelled_digit, digit in digits.items():
                # If the spelled digit is found in the substring
                if spelled_digit in substring:
                    return digit

    # If no digit is found
    return ""


def find_first_and_last_digit(line_of_text: str) -> str:
    """
    Extracts the first and last digit from a given line of text and returns
    them as a string. If just one digit is found, it is returned twice.

    Parameters:
    line_of_text (str): The line of text from which to extract the digits.

    Returns:
    str: The first and last digit from the line of text,
    or the same digit twice if only one digit is found.
    """
    return f"{find_first_digit(line_of_text)}{find_last_digit(line_of_text)}"


def get_sum_of_first_and_last_digits(text: str) -> int:
    """
    Calculates the sum of the numbers made from concatenating
    the first and last digits found in each line of the text using
    the find_first_and_last_digit function.

    Parameters:
    text (str): The text from which to calculate the sum.

    Returns:
    int: The sum of the numbers made from concatenating the
    first and last digits found in each line of the text.
    """

    numbers = []
    for line in text.splitlines():
        numbers.append(find_first_and_last_digit(line))

    return sum(int(i) for i in numbers)


if __name__ == "__main__":
    print(get_sum_of_first_and_last_digits(content))
