import re

with open('calibrations.txt', 'r') as file:
    content = file.readlines()


def get_first_and_last_number(line_of_text: str) -> str:
    """
    Extracts the first and last number from a given line of text and returns
    them as a string. If just one number is found, it is returned twice.

    Parameters:
    line_of_text (str): The line of text from which to extract the numbers.

    Returns:
    str: The first and last number from the line of text,
    or the same number twice if only one number is found.
    """

    found_numbers = re.findall(r'\d+', line_of_text)
    numbers = "".join(i for i in found_numbers)

    # If only one number is found
    if len(numbers) == 1:
        return f"{numbers[0]}{numbers[0]}"

    else:
        return f"{numbers[0]}{numbers[-1]}"


numbers = []
for line in content:
    numbers.append(get_first_and_last_number(line))

print(sum([int(i) for i in numbers]))
