print("Input: ")
szoveg = input()

def maganhangzo_torol(szoveg):
    maganhangzok = "aeiouAEIOU"
    return ''.join(karakter for karakter in szoveg if karakter not in maganhangzok)

import unittest

class TestMaganhangzoTorles(unittest.TestCase):
    def test_maganhangzo_torles(self):
        self.assertEqual(maganhangzo_torol("x"), "x")
        self.assertEqual(maganhangzo_torol("hello"), "hll")
        self.assertEqual(maganhangzo_torol("aeiou"), "")
        self.assertEqual(maganhangzo_torol("HELLO"), "HLL")

if __name__ == '__main__':
    print("Return:", maganhangzo_torol(szoveg))
    unittest.main()
