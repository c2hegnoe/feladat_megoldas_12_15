import unittest

print("Input: ", end="")  
jelszo = (str(input()))

def jelszo_erosseg(jelszo):
    if len(jelszo) == 0:
        return 0

    if 'jelszo' in jelszo or '123' in jelszo:
        return 0
    
    erosseg = 1  

    if len(jelszo) >= 5:
        erosseg += 1
    if len(jelszo) >= 8:
        erosseg += 2

    for karakter in jelszo:
        if karakter in ['_', '-', '.']:
            erosseg += 2
    
    return erosseg

print(f'Return: {jelszo_erosseg(jelszo)}')

class TesztSzamok(unittest.TestCase):

    def test_jelszo(self):
        self.assertGreater(jelszo_erosseg('ez1feltorhetetlenjelszo'), 7)

unittest.main()