ciag_liczb = ""
suma = 0
liczba_elementow = 0
najmniejsza = None
najwieksza = None
while True:
    a = int(input("Wprowadź liczbe: "))
    ciag_liczb += str(a) + ", "
    if a == 0:
        print("Użytkownik podał ciąg: "+ciag_liczb)
        break
    suma += a
    liczba_elementow += 1

    if najmniejsza is None or a < najmniejsza:
        najmniejsza = a
    if najwieksza is None or a > najwieksza:
        najwieksza = a

if liczba_elementow > 0:
    print(f"Suma min. i maks.: {najmniejsza+najwieksza}")
    print(f"Średnia arytmetyczna wynosi: {suma/liczba_elementow}")
