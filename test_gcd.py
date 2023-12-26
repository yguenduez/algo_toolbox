def gcd(a: int, b: int):
    if b == 0:
        return a
    else: 
        remainder = a % b
        return gcd(b, remainder)

def test_gcd_given_two_numbers_when_called_then_returns_gcd():
    # given
    a = 20
    b = 25

    # when
    result = gcd(a,b)

    # then
    assert result == 5