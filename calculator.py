def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


a = "add"
b = "subtract"
c = "multiply"
d = "divide"
g = "yes"
h = "no"

print("Select Operation")
print("a.", a)
print("b.", b)
print("c.", c)
print("d.", d)

e = input()

if e in ('a', 'b', 'c', 'd'):
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if e == 'a':
        print(num1, "+", num2, "=", add(num1, num2))

    elif e == 'b':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif e == 'c':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif e == 'd':
        print(num1, "/", num2, "=", divide(num1, num2))

print("Do you want to continue?")
f = input()

if f == g:
    while True:
        print("Select Operation")
        print("a.", a)
        print("b.", b)
        print("c.", c)
        print("d.", d)

        e = input()

        if e in ('a', 'b', 'c', 'd'):
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))

            if e == 'a':
                print(num1, "+", num2, "=", add(num1, num2))

            elif e == 'b':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif e == 'c':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif e == 'd':
                print(num1, "/", num2, "=", divide(num1, num2))

        print("Do you want to continue?")
        f = input()

        if f == g:
            pass
        else:
            quit()

else:
    quit()
