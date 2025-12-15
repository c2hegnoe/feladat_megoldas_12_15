import unittest

print("Input: ")

szam = (int(input()))

def armstrong_szam(num):
    szam_szoveg = str(num)
    n = len(szam_szoveg)
    total = 0

    for jegy in szam_szoveg:
        total += int(jegy) **n

    return total == num

print(f"Return: {armstrong_szam(szam)}")

class Tesztesetek(unittest.TestCase):

    def test_370(self):
        self.assertTrue(armstrong_szam(370))

unittest.main()
