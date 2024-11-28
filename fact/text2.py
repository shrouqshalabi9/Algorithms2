import time

def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Get the number from the user
number = int(input("Enter a number to calculate its factorial: "))

# Measure time in nanoseconds
start_time = time.perf_counter_ns()
result = factorial(number)
end_time = time.perf_counter_ns()

# Calculate elapsed time in nanoseconds
elapsed_time_ns = end_time - start_time

# Print the result and the elapsed time
print(f"Factorial of {number} is {result}")
print(f"Time taken: {elapsed_time_ns} nanoseconds")