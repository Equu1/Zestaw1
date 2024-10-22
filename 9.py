a = int(input("Wprowadź liczbę którą chcesz sprawdzić: "))
dzielniki = ""
suma = 0
for i in range(1, a+1):
    if a%i==0:
        dzielniki += str(i) + ", "
        suma += i
print(dzielniki)
if (suma-a)==a:
    print("Wprowadzona liczba jest liczbą doskonałą")
else:
    print("Wprowadzona liczba nie jest liczbą doskonałą")
