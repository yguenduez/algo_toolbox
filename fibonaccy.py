def fibonacci_number(n: int):
    numbers = [0,1]

    for i in range(2,n+1):
       numbers.append(numbers[i-1] + numbers[i-2])
    return numbers[n]

def last_digit_fibonacci(n:int):
    """Seems the last digit of a fibonacci is a sequence itself. So the first 60 fibonacci numbers repeat themselves, so you just have to cache the first 60 numbers.
    """
    precomputed_numbers = [fibonacci_number(x) for x in range(0,61)]
    return precomputed_numbers[n % 60] % 10

if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))
#    print(last_digit_fibonacci(input_n))
