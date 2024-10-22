wzrost = float(input("Podaj wzrost w metrach: "))
waga = float(input("Podaj wage w kilogramach: "))

while waga<=0 or wzrost<=0:
    print("Nieprawidłowe dane, wprowadź je jeszcze raz!")
    wzrost = float(input("Podaj wzrost w metrach: "))
    waga = float(input("Podaj wage w kilogramach: "))

BMI = round(waga/pow(wzrost,2), 1)

if BMI <= 18.5 :
    print(f"Niedowaga BMI wynosi: {BMI}")
elif BMI >= 24.9 :
    print(f"Nadwaga BMI wynosi: {BMI}")
else:
    print(f"Waga prawidłowa BMI wynosi: {BMI}")
