# Program for printing "fizz" for any number that is completely divisible by "3" 'buzz' if by '5' and "fizzbuzz" if by "3" and "5"
for i in range(51):
    if (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif (i % 3 == 0):
        print("fizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)
