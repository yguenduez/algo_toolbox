def longest_common_subsequence(seq1: [int], seq2: [int]) -> int:
    w, h = (len(seq1) + 1, len(seq2) + 1)

    cache = [[0 for x in range(w)] for y in range(h)]

    for x in range(1, w):
        for y in range(1, h):
            if seq1[x - 1] == seq2[y - 1]:
                """if the symbols are the same, then look to the diagonal of the matrix"""
                cache[y][x] = cache[y - 1][x - 1] + 1
            else:
                """otherwise search for the max of the subsequent sequences"""
                cache[y][x] = max(cache[y - 1][x], cache[y][x - 1])

    return cache[len(seq2)][len(seq1)]


def test_given_two_sequences_when_called_returns_the_longest_common_subsequence():
    # given
    seq_1 = [1, 4, 6, 3, 4]
    seq_2 = [5, 1, 6, 4, 8]

    # when
    longest_subsequence_len = longest_common_subsequence(seq_1, seq_2)

    # then
    assert longest_subsequence_len == 3


def test_given_two_sequences_with_no_common_when_called_returns_the_longest_zero():
    # given
    seq_1 = [7]
    seq_2 = [1, 2, 3, 4]

    # when
    longest_subsequence_len = longest_common_subsequence(seq_1, seq_2)

    # then
    assert longest_subsequence_len == 0


if __name__ == "__main__":
    _ = input()
    first_sequence = [int(x) for x in input().split(" ")]
    _ = input()
    second_sequence = [int(x) for x in input().split(" ")]

    longest_subsequence = longest_common_subsequence(first_sequence, second_sequence)
    print(longest_common_subsequence(first_sequence, second_sequence))
