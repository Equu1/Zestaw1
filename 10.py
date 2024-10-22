n = int(input("Wprowadź liczbę całkowitą: "))
dzielniki = ""
ilosc_dziel = 0
if n<=1:
    print("Liczba musi być większa niż 1")
else:
    for i in range(1, n+1):
        if n%i==0:
            dzielniki+=str(i)+" "
            ilosc_dziel=ilosc_dziel+1
    print(f"Dzielniki: {dzielniki}")
    if ilosc_dziel == 2:
        print(f"Liczba {n} jest liczbą pierwszą")
    else:
        print(f"Liczba {n} nie jest liczbą pierwszą")

print(f"Liczby pierwsze od 1 do {n}:")
liczby_pierwsze = ""

for i in range(2, n+1):
    ilosc_dziel2 = 0
    for j in range(1, i+1):
        if i % j == 0:
            ilosc_dziel2=ilosc_dziel2+1
    if ilosc_dziel2 == 2:
        liczby_pierwsze += str(i) + " "

print(liczby_pierwsze)
