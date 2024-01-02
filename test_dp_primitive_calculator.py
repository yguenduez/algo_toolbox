def dp_calculator(number: int) -> int:
    cache = dp_calculator_cache(number)

    return cache[number]


def dp_calculator_cache(number: int):
    min_operations = [99999999] * max((number + 1), 2)

    min_operations[1] = 0
    min_operations[0] = 0

    for i in range(2, number + 1):
        current_count_ops = min_operations[i - 1] + 1  # +1
        if i % 3 == 0:
            current_count_ops = min(current_count_ops, min_operations[int(i / 3)] + 1)
        elif i % 2 == 0:
            current_count_ops = min(current_count_ops, min_operations[int(i / 2)] + 1)
        min_operations[i] = current_count_ops

    return min_operations


def backtraking(number: int):
    min_operations = dp_calculator_cache(number)
    operations = []
    while number > 0:
        operations.append(int(number))
        if (
            number % 3 == 0
            and min_operations[int(number)] == min_operations[int(number / 3)] + 1
        ):
            number /= 3
        elif (
            number % 2 == 0
            and min_operations[int(number)] == min_operations[int(number / 2)] + 1
        ):
            number /= 2
        else:
            number -= 1
    operations.reverse()
    return operations


def test_with_given_failed_testcase_when_called_should_return_solution_output():
    "1 3 9 10 11 vs. 1 2 4 5 10 11"
    assert dp_calculator(11) == 4
    assert dp_calculator(96234) == 14


def test_calculator_given_8_when_called_then_returns_3_operations():
    # given when then
    assert dp_calculator(8) == 3
    print(backtraking(8))
    print(backtraking(34))
    assert dp_calculator(34) == 6
    print(backtraking(99))
    assert dp_calculator(99) == 6


if __name__ == "__main__":
    number = int(input())
    num_operations = dp_calculator(number)
    path = backtraking(number)

    print(num_operations)
    s = ""
    for num in path:
        s += "{} ".format(num)
    print(s)
