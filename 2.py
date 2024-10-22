cena = float(input("Podaj cenę towaru (od 100 zł do 10000 zł): "))
while (cena<100 or cena>10000):
    cena = float(input("Niepoprawna cena. Podaj cenę towaru (od 100 zł do 10000 zł): "))

liczba_rat = int(input("Podaj liczbę rat (od 6 do 48): "))
while (liczba_rat<6 or liczba_rat>48):
    liczba_rat = int(input("Niepoprawna liczba rat. Podaj liczbę rat (od 6 do 48): "))

if 6 <= liczba_rat <= 12:
    oprocentowanie = 0.025
elif 13 <= liczba_rat <=24:
    oprocentowanie = 0.05
else:
    oprocentowanie = 0.1

odsetki = cena*oprocentowanie
cena_odsetki = odsetki+cena
rata = cena_odsetki/liczba_rat

print(f"Miesięczna rata wynosi: {round(rata,2)} zł")
