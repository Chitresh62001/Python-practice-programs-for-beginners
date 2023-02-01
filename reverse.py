# Reversing a string without using the strrev function
print("enter the word you want to reverse")
word = input()
for char in range(len(word) - 1, -1, -1):
    print(word[char], end=" ")
