import random

print("Wybierz poziom trudnośći:\n-1- Łatwy (1-50)\n-2- Średni (1-100)\n-3- Trudny (1-200)")

poziom = int(input("Podaj poziom trudności (1, 2 albo 3): "))

if poziom==1:
    max_zakres = 50
elif poziom==2:
    max_zakres = 100
else:
    max_zakres = 200

wylosowana = random.randint(1, max_zakres+1)
liczba_prob = 0

while True:
    liczba_prob+=1
    a = int(input(f"Podaj liczbę (1-{max_zakres}): "))
    if a < wylosowana:
        print("Podałeś za małą wartość")
    elif a > wylosowana:
        print("Podałeś za dużą wartość")
    else:
        print(f"Gratulacje! Odgadłeś liczbę {wylosowana} w {liczba_prob} próbach.")
        break
