import random

### Wybierz X z 5 lub 7 linii! ###

# x = int(input("Podaj maksymalną liczbę:"))

x = 100

print("Wylosowałem liczbę między 1 a", x)
tn = 0

n = random.randrange(1, x)

t = 0

while t != n:
    try:
        tn += 1
        t = int(input("Zgadnij liczbę!: "))
        if n > t:
            print("Wylosowana liczba jest ^^^ WIĘKSZA od Twojej!")
        elif n < t:
            print("Wylosowana liczba jest ¬¬¬ MNIEJSZA od Twojej!")
        else:
            print("BRAWO! wylosowana liczba to", n, "! Zgadłeś za", tn, "razem")
    except:
        print("!!! Tylko LICZBY !!!")

print("😝😝😁😁😝😝")