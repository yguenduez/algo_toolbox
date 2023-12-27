def gcd(a: int, b: int):
    if b == 0:
        return a
    else: 
        remainder = a % b
        return gcd(b, remainder)

def lcm(a: int, b: int):
    return a * int((b/gcd(a,b)))
    

def test_gcd_given_two_numbers_when_called_then_returns_gcd():
    # given
    a = 20
    b = 25

    # when
    result = gcd(a,b)

    # then
    assert result == 5

def test_lcm_given_two_numbers_when_called_then_returns_lcm():
    # given
    a = 4
    b = 6

    # when
    result = lcm(a,b)

    # then
    assert result == 12

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
