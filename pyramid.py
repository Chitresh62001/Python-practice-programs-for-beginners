# Program to print different types of pyramid
def horizontal_pyramid(n):
    print("Horizontal Pyramid")
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("*")
    for i in range(n, -1, -1):
        for j in range(i):
            print("*", end=" ")
        print("*")


def half_pyramid(n):
    print("Half Pyramid")
    for i in range(n+1):
        print(i*"* ")


def pyramid(n):
    print("Pyramid")
    for i in range(n+1):
        print(" "*(n-i), i*"* ")


def inverted_pyramid(n):
    print("Inverted Pyramid")
    for i in range(n, 0, -1):
        print(" "*(n-i), " *"*i)


horizontal_pyramid(5)
half_pyramid(5)
pyramid(5)
inverted_pyramid(5)
