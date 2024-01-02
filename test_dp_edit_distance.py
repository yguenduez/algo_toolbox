def edit_distance(first: str, second: str) -> int:
    w, h = (len(first), len(second))
    cache = [[9999 for x in range(w + 1)] for y in range(h + 1)]

    for x in range(w + 1):
        cache[0][x] = x
    for y in range(h + 1):
        cache[y][0] = y

    for y in range(1, h + 1):
        for x in range(1, w + 1):
            insertion = cache[y - 1][x] + 1
            deletion = cache[y][x - 1] + 1
            match = cache[y - 1][x - 1]
            mismatch = match + 1

            if first[x - 1] == second[y - 1]:
                cache[y][x] = min(min(insertion, deletion), match)
            else:
                cache[y][x] = min(min(insertion, deletion), mismatch)

    return cache[len(second)][len(first)]


def test_edit_distance_given_different_strings_returns_the_minumum_edit_distance():
    # given
    first_string = "edit"
    second_string = "distance"

    # when
    distance = edit_distance(first_string, second_string)

    # then
    assert distance == 6


def test_edit_distance_given_two_similar_strings_returns_the_minumum_edit_distance():
    # given
    first_string = "hallo"
    second_string = "nallo"

    # when
    distance = edit_distance(first_string, second_string)

    # then
    assert distance == 1


if __name__ == "__main__":
    first_word = input()
    second_word = input()

    min_distance = edit_distance(first_word, second_word)

    print(min_distance)
