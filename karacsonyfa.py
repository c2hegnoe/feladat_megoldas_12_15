magassag = int(input())

# lomb
for sor in range(magassag):
    szokozok = magassag - sor - 1
    csillagok = 2 * sor + 1
    print(" " * szokozok + "*" * csillagok)

# törzs (2 sor, 3 darab | jel)
torzs_szokoz = magassag - 2
for _ in range(2):
    print(" " * torzs_szokoz + "|||")