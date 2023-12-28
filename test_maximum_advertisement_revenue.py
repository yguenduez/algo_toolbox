def max_dot_product(prices, clicks):
    clicks.sort()
    prices.sort()
    result = 0
    for i in range(0, len(clicks)):
        result += clicks[i] * prices[i]

    return result

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

def test_when_called_then_returns_max_product():
    # given
    prices = [23]
    clicks = [39]  

    # when
    result = max_dot_product(prices, clicks)

    # then
    assert result == 897
