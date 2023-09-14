def tiskni_vzor(pocet_cisel):
    for i in range(pocet_cisel, 0, -1):
        cisla = ''.join(str(j) for j in range(1, i + 1))
        print(cisla if i % 2 == 1 else cisla[::-1])

try:
    pocet_cisel = int(input("Zadej počet čísel: "))
    tiskni_vzor(pocet_cisel)
except ValueError:
    print("Zadej platné číslo.")
