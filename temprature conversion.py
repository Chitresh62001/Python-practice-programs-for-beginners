# program for converting temprature from one convention to other
temprature = input(
    "Enter the temprature in proper convention(eg: 140F, 240C)\n").lower()
convention = temprature[-1]
degree = temprature[:-1]

if convention == "f":
    result = round((((int(degree)-32)/9)*5), 2)
    print(str(result) + "degree Celsius")
elif convention == "c":
    result = round(((int(degree)*9)/5 + 32), 2)
    print(str(result) + "degree Farenheight")
else:
    print("enter proper conventions")
