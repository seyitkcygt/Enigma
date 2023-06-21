from Rotor import Rotor

class Enigma:
	def __init__(self,rotors=None,selectedRotors=[1,2,3],selectedOffset=[0,0,0]):
		# selected rotor is from 1 to 5 which we have 5 rotor

		self.rotors = [Rotor(i+1) for i in range(5)] if rotors == None else rotors
		self.selectedRotors = [self.rotors[i-1] for i in selectedRotors]
		self.selectedOffset = selectedOffset
		self.selectedRotors = self.__initilizeRotors(self.selectedOffset)

		#rotor will be placed from left to right and left rotor will be most significant one that means it will be the slowest in terms of revolution
		# left most rotor will start a position 0 in selectedrotors and so on ...
	def __initilizeRotors(self,offset):
		for i in range(len(self.selectedRotors)):
			self.selectedRotors[i].set_offset(offset[i])
			self.selectedRotors[i].reset_rev()
			if(i == 0):
				# most significant rotor add only right rotor to it
				self.selectedRotors[i].set_rightrotor(self.selectedRotors[i+1])
			elif(i == len(self.selectedRotors)-1):
				# least significant one add only left to it
				self.selectedRotors[i].set_leftrotor(self.selectedRotors[i-1])
			else:
				# add both to inbetween rotors
				self.selectedRotors[i].set_rightrotor(self.selectedRotors[i+1])
				self.selectedRotors[i].set_leftrotor(self.selectedRotors[i-1])
		return self.selectedRotors



	def encode(self,plainText):
		cipherText = ""

		for s in plainText:
			c = s
			for rotor in self.selectedRotors[::-1]:
				c = rotor.get_forward_letter(c)
			for rotor in self.selectedRotors:
				c = rotor.get_backward_letter(c)
			cipherText += c

		return cipherText

	def decode(self,cipherText,offset):
		self.selectedRotors = self.__initilizeRotors(offset)
		plainText = ""

		for c in cipherText:
			s = c
			for rotor in self.selectedRotors[::-1]:
				s = rotor.get_forward_letter(s)
			for rotor in self.selectedRotors:
				s = rotor.get_backward_letter(s)
			plainText += s

		return plainText



	def __str__(self):
		details  = ""

		for i in self.selectedRotors:
			details += str(i) + "\n"

		return details


if __name__ == "__main__":
	enigma = Enigma(selectedOffset=[10,0,5])
	print(enigma)
	plainText = "her gece rüyalarımda geliyorsun ziyaretime\nalevden yaratılmış parmaklıklar var aramızda\nloş bir ışık hüzmesi aydınlatıyor bu sensizlik mahzenini\niki küçük delikten geliyor umut oksijeni\nmahsur kaldım bu alevden parmaklıklar ardında\nellerimiz bir kavuşsa bu karanlık yok olacak\nmesafelere kötü bir haber\nbir ömür birkaç yıldan çok daha uzun..."
	print(plainText)
	cipherText = enigma.encode(plainText)

	print(cipherText)
	decoded = enigma.decode(cipherText,enigma.selectedOffset)
	print(decoded)
	