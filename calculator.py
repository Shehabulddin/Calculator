def calc(input_string: str) -> int:
    if input_string == "":
        return 0

    # Check if there's a custom delimiter defined on the first line
    if input_string.startswith("//"):
        delimiter_line, numbers_line = input_string.split("\n", 1)
        delimiter = delimiter_line[2:]  # Extract the delimiter after the "//"
    else:
        # Default delimiter is a comma
        delimiter = ","
        numbers_line = input_string

    # Replace newlines with the delimiter and split the numbers
    numbers = numbers_line.replace("\n", delimiter).split(delimiter)

    # Convert to integers and filter numbers greater than 1000
    int_numbers = [int(num) for num in numbers if int(num) < 1000]

    # Check for negatives
    negatives = [num for num in int_numbers if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(int_numbers)
