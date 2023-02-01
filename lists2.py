# Program for checking whether the entered element is present in the lists
fruits = ["apple", "pears", "grapes", "mango"]
toys = ["car", "ball", "plane", "train"]
while True:
    # Taking input from the user
    response = input(
        'what are you looking for?(Type "exit" if you want to quit)\n').lower()
    # if the user types exit it breaks the while loop
    if response == "exit":
        break
    # checking the lists for the element and displaying output accordingly
    if response in fruits:
        print("Yes, it is present in the list of fruits")
    elif response in toys:
        print("Yes, it is present in the list of toys")
    elif response not in toys or fruits:
        print("NO, it is not present in any of the list")
