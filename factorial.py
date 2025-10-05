
# Part1:- Calculate the factorial of a given number
# Part2:- Find the number of trailing zeros in that factorial.

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Part 2: Find trailing zeros in factorial


def trailing_zeros(n: int) -> int:
    # The number of trailing zeros is determined
    # by the number of times 5 divides n!
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count


# Main program
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    fact = factorial(num)
    zeros = trailing_zeros(num)

    print(f"Factorial of {num} is: {fact}")
    print(f"Number of trailing zeros in {num}! is: {zeros}")
