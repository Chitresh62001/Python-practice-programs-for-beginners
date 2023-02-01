# Program to print fibonacci series starting from 0 and 1
fibonacci_series = [0, 1]
while True:
    fibonacci_numbers = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(fibonacci_numbers)
    if fibonacci_numbers > 50:
        break
print(fibonacci_series)
