# program for counting the even and odd numbers in the list
numbers = []
# appending the numbers in the first list
for x in range(0, 11):
    numbers.append(x)
# if the number is completely divisible by 2 then appending it in even numbers list
i = 0
for number in numbers:
    if number % 2 == 0:
        i = i+1
# if the number is not completely divisible by 2 then appending it in odd numbers list
j = 0
for num in numbers:
    if num % 2 != 0:
        j = j + 1

print("There are " + str(j) + " odd numbers in the list and " +
      "There are " + str(i) + " even numbers in the list")
