def longest_increasing_subsequence(sequence: [int]):
    cache = [None] * len(sequence)

    for i in range(len(sequence)):
        cache[i] = 1
        for j in range(i):
            if sequence[j] < sequence[i] and cache[i] < cache[j] + 1:
                cache[i] = cache[j] + 1

    return cache[len(sequence) - 1]


def test_given_sequence_when_called_then_returns_longest_subsequence_length():
    # given
    sequence = [1, 3, 2, 7, 6, 5, 4]

    # when
    max_len = longest_increasing_subsequence(sequence)

    # then
    assert max_len == 3


if __name__ == "__main__":
    pass
