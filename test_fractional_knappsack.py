from sys import stdin

def compute_fractions(weights, values):
    return list(map(lambda i: values[i]/weights[i], range(0, len(weights))))

def optimal_value(capacity, weights, values):
    fractions = compute_fractions(weights, values)
    best_indices = sort_weights_indices(weights, values)
    value = 0.
    current = 0
    current_indice = best_indices[current]

    while capacity > 0:
        if weights[current_indice] == 0:
            current += 1

            if current == len(weights):
                break
            current_indice = best_indices[current]

        current_indice = best_indices[current]
        current_fraction = fractions[current_indice]
        value += current_fraction
        weights[current_indice] -= 1
        capacity -= 1

    return value

def sort_weights_indices(weights, values):
    indices = []
    for i in range(0, len(weights)):
        indices.append((i, values[i]/weights[i]))
    indices.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], indices))


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


def test_diffetent_values():
    # given
    inputs = [([100,120],[50,30], 20), ([500],[30], 1000)]

    # when
    outputs = list(map(lambda x: int(optimal_value(capacity=x[2], weights=x[1], values=x[0])), inputs))

    # then
    assert outputs == [80, 500]

def test_optimal_value():
    # given
    values = [100, 120]
    weights = [50, 30]
    capacity = 20

    # when 
    opt_value = optimal_value(capacity, weights, values)

    # then
    assert opt_value == (120/30) * 20


def test_sort_indices():
    # given
    values = [100, 120]
    weights = [50, 30]

    # when
    indices = sort_weights_indices(weights, values)

    # then
    assert indices == [1,0]

def test_compute_fractions_given_valid_inputs_when_called_returns_correct_inputs():
    # given
    weights = [1,2,3,4]
    values = [4,3,2,1]

    # when
    fractions = compute_fractions(weights, values)

    # then
    assert fractions == [4., 1.5, 2/3, 1/4]