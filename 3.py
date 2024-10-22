a = int(input("Wprowadź pierwszą liczbę: "))
b = int(input("Wprowadź drugą liczbę: "))
while a<0 or b<0:
    print("Liczby muszą być dodatnie!")
    a = int(input("Wprowadź pierwszą liczbę: "))
    b = int(input("Wprowadź drugą liczbę: "))

if a<b:
    for i in range(a, b+1):
        if i%2!=0:
            print(i, end=" ")
else:
    for i in range(b, a+1):
        if i%2!=0:
            print(i, end=" ")
