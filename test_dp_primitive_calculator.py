if __name__ == "__name__":
    pass


def dp_calculator(number: int) -> int:
    return dp_calculator_cache(number)[int(number)]


def dp_calculator_cache(number: int):
    min_operations = [99999999] * (number + 1)

    min_operations[1] = 0
    min_operations[0] = 0
    min_operations[2] = 1
    min_operations[3] = 1

    for i in range(4, number + 1):
        current_count_ops = min_operations[i]
        if i % 2 == 0:
            current_count_ops = min(current_count_ops, min_operations[int(i / 2)] + 1)
        elif i % 3 == 0:
            current_count_ops = min(current_count_ops, min_operations[int(i / 3)] + 1)
        else:
            current_count_ops = min_operations[i - 1] + 1  # +1
        min_operations[i] = current_count_ops

    return min_operations


def backtraking(number: int):
    min_operations = dp_calculator_cache(number)
    print(min_operations)

    operations = []
    while number > 1:
        if (
            number % 3 == 0
            and min_operations[int(number)] == min_operations[int(number / 3)] + 1
        ):
            operations.append("*3")
            number /= 3
        elif (
            number % 2 == 0
            and min_operations[int(number)] == min_operations[int(number / 2)] + 1
        ):
            operations.append("*2")
            number /= 2
        else:
            operations.append("+1")
            number -= 1
    operations.reverse()
    return operations


def test_calculator_given_8_when_called_then_returns_3_operations():
    # given when then
    assert dp_calculator(8) == 3
    print(backtraking(8))
    print(backtraking(34))
    assert dp_calculator(34) == 6
    print(backtraking(99))
    print(backtraking(96))
    assert dp_calculator(99) == 7
    assert False
