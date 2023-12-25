import sys
from max_pair_wise import get_max_pair, get_faster_max_pair

def test_get_max_pairs_given_list_of_numbers_when_called_then_returns_max_pairs():
    # given
    numbers = [1,3,4,2,4,7,9]

    # when
    max_pair = get_max_pair(numbers)

    # then
    assert max_pair == 63


def test_get_faster_max_pairs_given_list_of_numbers_when_called_then_returns_max_pairs():
    # given
    numbers = [1,3,4,2,4,7,9]

    # when
    max_pair = get_faster_max_pair(numbers)

    # then
    assert max_pair == 63