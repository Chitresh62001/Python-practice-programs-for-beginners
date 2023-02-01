# counting the even and odd numbers in the list
numbers = []
even_numbers = []
odd_numbers = []
# appending the numbers in the first list
for x in range(0, 10):
    numbers.append(x)
# if the number is completely divisible by 2 then appending it in even numbers list
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(str(number))
# if the number is not completely divisible by 2 then appending it in odd numbers list
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(str(num))

print("There are " + str(len(even_numbers)) + " odd numbers in the list and " +
      "There are " + str(len(odd_numbers)) + " even numbers in the list")
