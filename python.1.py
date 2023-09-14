def tiskni_vzor(pocet_cisel):
    for i in range(pocet_cisel):
        mezery = '-' * (pocet_cisel - i - 1)
        hvezdicky = '*' + '-' * i
        print(mezery + hvezdicky)

try:
    pocet_cisel = int(input("Zadej počet čísel: "))
    tiskni_vzor(pocet_cisel)
except ValueError:
    print("Zadej platné číslo.")
