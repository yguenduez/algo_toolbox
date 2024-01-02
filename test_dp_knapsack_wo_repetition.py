def knapsack(knapsack_weight: int, item_weights: [int]) -> int:
    cache = [[0] * (knapsack_weight + 1) for y in range(len(item_weights) + 1)]

    for y in range(1, len(item_weights) + 1):
        for weight in range(1, knapsack_weight + 1):
            cache[y][weight] = cache[y - 1][weight]
            curr_weight = item_weights[y - 1]
            if curr_weight <= weight:
                current_value = curr_weight
                value = cache[y - 1][weight - curr_weight] + current_value
                cache[y][weight] = max(cache[y][weight], value)

    return cache[len(item_weights)][knapsack_weight]


def test_given_weigt_with_items_returns_max_value():
    # given
    weights = [1, 4, 8]
    weight = 10

    # when
    value = knapsack(weight, weights)

    # then
    assert value == 9


if __name__ == "__main__":
    weight, gold_bars = map(int, input().split())
    bar_weights = [int(x) for x in input().split()]

    print(knapsack(weight, bar_weights))
