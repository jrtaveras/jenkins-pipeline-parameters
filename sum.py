import sys

def sum_numbers(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sum.py <number1> <number2>")
        sys.exit(1)

    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])

    result = sum_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {result}")
