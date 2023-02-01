# Program for converting temprature from one convention to another
run = True
while run:
    print("Enter the temprature (eg: 140F, 240C)")
    # Taking the input from the user
    temprature = input().lower()
    convention = temprature[-1]
    degree = temprature[:-1]
    # if the input is not in numbers asking the user to give input again
    if degree >= 'a' and degree <= 'z':
        print("Please enter Numbers only")
    else:
        # Checking if the temprature entered by the user is in farenheight or celcius
        if convention == "f":
            result = round((((int(degree)-32)/9)*5), 2)
            print(str(result) + " degree Celsius")
            # Asking whether the user wants to continue converting or not
            run_1 = True
            while run_1:
                print("\n\nDo you want to convert again ? (Yes/No)")
                response = input().lower()
                if response == "yes":
                    run_1 = False
                    continue
                if response == "no":
                    run = False
                    break
                else:
                    print("Enter correctly")
                    continue
        elif convention == "c":
            result = round(((int(degree)*9)/5 + 32), 2)
            print(str(result) + " degree Farenheight")
            run_1 = True
            while run_1:
                print("\n\nDo you want to convert again ? (Yes/No)")
                response = input().lower()
                if response == "yes":
                    run_1 = False
                    continue
                if response == "no":
                    run = False
                    break
                else:
                    print("Enter correctly")
                    continue
        # if the user does not add 'f' or 'c' at the end asking user to enter again
        else:
            print("Error : Enter proper conventions")
