from Enigma import Enigma
from Rotor import Rotor



alphabet = list(map(chr, range(97, 123)))
mapped1 = [i for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ".lower()]
mapped2 = [i for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE".lower()]
mapped3 = [i for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO".lower()]
mapped4 = [i for i in "ESOVPZJAYQUIRHXLNFTGKDCMWB".lower()]
mapped5 = [i for i in "VZBRGITYUPSDNHLXAWMJQOFECK".lower()]


rotor1 = Rotor(1,alphabet=alphabet,mapped=mapped1)
rotor2 = Rotor(2,alphabet=alphabet,mapped=mapped2)
rotor3 = Rotor(3,alphabet=alphabet,mapped=mapped3)
rotor4 = Rotor(4,alphabet=alphabet,mapped=mapped4)
rotor5 = Rotor(5,alphabet=alphabet,mapped=mapped5)


enigma = Enigma(rotors=[rotor1,rotor2,rotor3,rotor4,rotor5],selectedRotors=[1,2,3],selectedOffset=[0,0,0])

plainText = "halimemsenicokseviyorumguzelim"
cipherText = enigma.encode(plainText)
print(plainText)
print(cipherText)
print(enigma.decode(cipherText,enigma.selectedOffset))