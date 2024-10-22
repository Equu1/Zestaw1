liczba = int(input("Wprowadź liczbę całkowitą: "))
while liczba <=0:
    liczba = int(input("Niepoprawna liczba!\nWprowadź liczbę całkowitą: "))
suma = 0
parzyste = 0
nieparzyste = 0
suma_parz = 0
suma_nieparz = 0
for i in str(liczba):
    suma+=int(i)
    if int(i)%2==0:
        parzyste=parzyste+1
        suma_parz += int(i)
    else:
        nieparzyste=nieparzyste+1
        suma_nieparz += int(i)
print(f"Suma cyfr w liczbie {liczba} wynosi: {suma}")
if parzyste>0 and nieparzyste>0:
    print("Stosunek Średniej arytmetycznej cyfr parzystych do średniej arytmetycznej cyfr nieparzystych:",round((suma_parz/parzyste)/(suma_nieparz/nieparzyste),2))
else:
    print("Nie można podzielić z uwagi że nie wystepuje żadna cyfra parzysta bądź nieparzysta")
wybor = int(input("\nCzy chcesz podać dodatkową liczbę, wprowadź (1 - tak, 2 - nie): "))
suma2 = 0
if wybor == 1:
    liczba2 = int(input("Wprowadź liczbę całkowitą: "))
    for i in str(liczba2):
        suma2 += int(i)
    print(f"Stosunek sum cyfr liczby: {liczba} i liczby: {liczba2} wynosi {round(liczba/liczba2,2)}")
else:
    print("Koniec programu")
