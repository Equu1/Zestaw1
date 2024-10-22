a1 = float(input("Podaj a1: "))
b1 = float(input("Podaj b1: "))
c1 = float(input("Podaj c1: "))

a2 = float(input("Podaj a2: "))
b2 = float(input("Podaj b2: "))
c2 = float(input("Podaj c2: "))

wyznacznik = a1*b2-a2*b1

if wyznacznik == 0:
    if a1*c2==a2*c1 and b1*c2==b2*c1:
        print("Układ ma nieskończenie wiele rozwiązań.")
    else:
        print("Układ nie ma rozwiązań.")
else:
    x = (c1*b2-c2*b1)/wyznacznik
    y = (a1*c2-a2*c1)/wyznacznik

    print(f"Rozwiązanie układu: x= {x}, y= {y}")
