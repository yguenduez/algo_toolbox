import sys

def get_max_pair(numbers):
    result = 0
    list_size = len(numbers) 
    for i in range(0, list_size):
        for j in range(i+1, list_size):
            result = max(result, numbers[i] * numbers[j])
    return result

def get_faster_max_pair(numbers):
    max_number = max(numbers)
    numbers.remove(max_number)
    second_max_number = max(numbers)

    return max_number * second_max_number

def main():
    _ = int(input())
    numbers = list(map(int, input().split())) 
    result = get_faster_max_pair(numbers)

    print(result)

if __name__ == "__main__":
    main()