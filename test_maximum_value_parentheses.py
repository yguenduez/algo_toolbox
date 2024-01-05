def parse_expression(expression: str):
    numbers = []
    operations = []
    for i, symbol in enumerate(expression):
        if i % 2 == 0:
            numbers.append(int(symbol))
        else:
            operations.append(symbol)
    return (numbers, operations)


def evaluate(a, b, operation) -> int:
    if operation == "+":
        return a + b
    elif operation == "*":
        return a * b
    elif operation == "-":
        return a - b
    else:
        return int(a / b)


def parentheses(numbers: [int], operations: [str]) -> int:
    # init cache matrices. One for max one for min
    length = len(numbers)
    mins = [[None for n in range(length)] for n in range(length)]
    maxes = [[None for n in range(length)] for n in range(length)]

    for i in range(len(numbers)):
        mins[i][i] = numbers[i]
        maxes[i][i] = numbers[i]

    for s in range(1, length):
        for i in range(length - s):
            j = i + s
            min, max = min_and_max(i, j, maxes, mins, operations)
            mins[i][j] = min
            maxes[i][j] = max

    return maxes[0][length - 1]


def min_and_max(
    i: int, j: int, maxes: [int], mins: [int], operations: [str]
) -> (int, int):
    max_val = -9999999
    min_val = 9999999

    # Bug is here! As we do not loop in the first iteration - we keep -99999 as max and 99999 as min. That is stupid
    # I do not know if this is intended. But the inf numbers get dragged all the way through the matrix
    for k in range(i, j):
        a = evaluate(maxes[i][k], maxes[k + 1][j], operations[k])
        b = evaluate(maxes[i][k], mins[k + 1][j], operations[k])
        c = evaluate(mins[i][k], maxes[k + 1][j], operations[k])
        d = evaluate(mins[i][k], mins[k + 1][j], operations[k])
        min_val = min(min(min(min(a, b), c), d), min_val)
        max_val = max(max(max(max(a, b), c), d), max_val)
    return (min_val, max_val)


def test_evaluate_given_numbers_and_operation_when_called_then_computes_negative_expression_value():
    # given
    a, b, operation = (5, 8, "-")

    # when
    result = evaluate(a, b, operation)

    # then
    assert result == -3


def test_evaluate_given_numbers_and_operation_when_called_then_computes_expression_value():
    # given
    a, b, operation = (5, 4, "*")

    # when
    result = evaluate(a, b, operation)

    # then
    assert result == 20


def test_parse_expression_given_an_expression_when_called_then_parses_correctly():
    # given
    expression = "5-8+7*4-8+9"

    # when
    numbers, operations = parse_expression(expression)

    # then
    assert numbers == [5, 8, 7, 4, 8, 9]
    assert operations == ["-", "+", "*", "-", "+"]


def test_given_simple_input_when_called_then_returns_expected_max_value():
    expression = "5-8"
    numbers, operations = parse_expression(expression)

    # when
    max_value = parentheses(numbers, operations)

    # then
    assert max_value == -3


def test_given_input_when_called_then_returns_expected_max_value():
    expression = "5-8+7*4-8+9"
    numbers, operations = parse_expression(expression)

    # when
    max_value = parentheses(numbers, operations)

    # then
    assert max_value == 200


if __name__ == "__main__":
    expression = input()
    numbers, operations = parse_expression(expression)

    print(parentheses(numbers, operations))
