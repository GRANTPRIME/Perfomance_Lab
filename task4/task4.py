import sys

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def min_moves_to_same_value(numbers):
    n = len(numbers)
    if n == 0:
        return 0

    average = sum(numbers) // n

    total_moves = sum(abs(num - average) for num in numbers)

    return total_moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py input_file")
    else:
        input_file = sys.argv[1]
        numbers = read_numbers(input_file)
        moves = min_moves_to_same_value(numbers)
        print(moves)
