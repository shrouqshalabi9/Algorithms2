import time


def factorial_iterative(n):
    """Calculate the factorial of a number iteratively."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Get the number from the user
number = int(input("Enter a number to calculate its factorial: "))

# Measure time in nanoseconds
start_time = time.perf_counter_ns()
result = factorial_iterative(number)
end_time = time.perf_counter_ns()

# Calculate elapsed time in nanoseconds
elapsed_time_ns = end_time - start_time

# Print the result and the elapsed time
print(f"Factorial of {number} is {result}")
print(f"Time taken: {elapsed_time_ns} nanoseconds")
