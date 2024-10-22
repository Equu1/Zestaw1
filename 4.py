a = int(input("Wprowadź dodatnią liczbę: "))
podstawa = int(input("Wprowadź podstawę: "))
potega, b = 0, 0
while a>b:
    b = pow(podstawa, potega)
    potega = potega+1
    if b<a:
        print(b)
