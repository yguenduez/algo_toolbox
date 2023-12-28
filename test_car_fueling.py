from sys import stdin, maxsize
import math

def test_car_fueling():
    pass

def find_leftmost_element(threshold, elements):
    curr_distance = maxsize
    leftmost = -1
    for el in elements:
        if el > threshold:
            break
        dist = threshold - el
        if dist < curr_distance:
            curr_distance = dist
            leftmost = el
    return leftmost 

def min_refills(distance, tank, stops: [int]):
    left = 0
    segments = []

    if tank >= distance:
        return 0

    while left+tank < distance:
        right = find_leftmost_element(left + tank, stops)

        if right == left or right ==-1:
            return -1

        if right >= distance:
            break

        segments.append((left, right))
        left = right

    return len(segments) 

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))


def test_find_leftmost_element():
    # given
    threshold = 400
    elements = [200, 350, 380, 410]

    # when
    result = find_leftmost_element(threshold, elements)

    # then
    assert result == 380

def test_find_leftmost_element_given_no_left_elements_returns_min_1():
    # given
    threshold = 400
    elements = [410]

    # when
    result = find_leftmost_element(threshold, elements)

    # then
    assert result == -1


def test_given_valid_inputs_when_called_then_returns_counts_stops():
    # given
    city_distance = 950
    max_distance = 400
    stops = [200, 375, 550, 750]

    # when
    refills = min_refills(city_distance, max_distance, stops)

    # then
    assert refills == 2

def test_given_dist_with_no_needed_tank_when_called_then_returns_0():
    # given
    dist = 200
    tank = 250
    stops = [100,150]

    # when
    refills = min_refills(dist, tank, stops)

    # then
    assert refills == 0

def test_given_no_reachable_destination_when_called_then_returns_minus_1():
    # given
    dist = 10
    tank = 3
    stops = [1,2,5,9]

    # when
    refills = min_refills(dist, tank, stops)

    # then
    assert refills == -1