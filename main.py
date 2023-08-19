import random

### Choose X from 5th or 7th line! ###

# x = int(input("Enter the maximum number to draw:"))

x = 100

print("I drew a number between 1 and", x)
tn = 0

n = random.randrange(1, x)

t = 0

while t != n:
    try:
        tn += 1
        t = int(input("guess the number!: "))
        if n > t:
            print("The drawn number is ^^^ BIGGER than yours!")
        elif n < t:
            print("The drawn number is ¬¬¬ LESS than yours!")
        else:
            print("WAY TO GO! the drawn number is", n, "! number of tries", tn)
    except:
        print("!!! NUMBERS ONLY !!!")

print("😝😝😁😁😝😝")
