# Program for printing each element of the list and checking if the desired element is what user is looking for
fruits = ["apple", "pears", "grapes", "mango"]

for i in range(len(fruits)):
    print("is", fruits[i], "what you were looking for")
    ans = input().lower()
    if ans == "yes":
        print(fruits[i], "found in the list")
        if i < len(fruits)-1:
            print("do you want to continue")
            ans = input().lower()
            if ans == "yes":
                continue
            elif ans == "no":
                print("Have a nice day\n", "Program Ended......")
                break
        elif i == len(fruits)-1:
            print("List has ended\n", "Hope you got what you were looking for")
    else:
        print("Moving Forward")
        if i == len(fruits)-1:
            print("List has ended\n",
                  "Item you were looking for was not in the list")
