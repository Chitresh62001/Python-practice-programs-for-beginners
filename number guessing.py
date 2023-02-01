# using while to check if the user guesses the correct number and exiting the loop if he does
while True:
    print("enter the number until you guess it correct")
    number = input()
    if int(number) >= 1 and int(number) <= 9:
        print("well guessed")
        break
    else:
        print("Try again from the start")
