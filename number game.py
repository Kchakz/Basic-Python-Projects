import random

while True:

    print("Do you want to roll?")
    c = random.randint(1, 10)
    a = 'yes'
    b = input()

    if a == b:
        print(c)

    if b != a:
        quit()
