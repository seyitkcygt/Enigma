import random

#### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! alphabet should be even number of letters or characters this is soooo important here because of  the way most significant rotor works

class Rotor:
	def __init__(self,name,alphabet=None,mapped=None,routerOffset = 0):
		self.name = "Rotor {0}".format(name) 
		self.revaluation = 1
		self.routerOffset = routerOffset
		self.alphabet = list(map(chr, range(97, 123))) + [str(i) for i in range(10)] + [" ", ".", "\n","ü","ş","ı","ö","ç"] if alphabet == None else alphabet
		self.mapped = random.sample(self.alphabet,len(self.alphabet)) if mapped == None else mapped
		self.LeftRouter = None
		self.RightRouter = None

	def __str__(self):
		return self.name + " : " + " Offset " + str(self.routerOffset) + " " + str(self.alphabet) + " ==> " + str(self.mapped) + " " + str(self.revaluation)

	def set_offset(self,offset):
		self.routerOffset = offset

	def reset_rev(self):
		self.revaluation = 1


	def set_leftrotor(self,rotor):
		self.LeftRouter = rotor

	def set_rightrotor(self,rotor):
		self.RightRouter = rotor

	def get_forward_letter(self,letter):
		if(self.RightRouter == None or self.RightRouter.revaluation == 0):
			# right router finished a full revaluation and we need to increase this ones offset
			
			self.routerOffset += 1
			self.routerOffset = self.routerOffset % len(self.alphabet) ## to create a cicular motion

			self.revaluation += 1
			self.revaluation = self.revaluation % len(self.alphabet) 

		idx = self.alphabet.index(letter) + self.routerOffset
		idx = idx % len(self.alphabet)

		return self.mapped[idx]

	def get_backward_letter(self,letter):

		# here because we are turning the router. we need to calculate (-) offset for backward
		idx = self.mapped.index(letter) - self.routerOffset + len(self.alphabet)
		idx = idx % len(self.alphabet)

		#if left rotor is none which means this router is the most significant one

		if(self.LeftRouter == None):
			idx = self.mapped.index(letter) +  len(self.alphabet)//2 - self.routerOffset + len(self.alphabet)
			idx = idx % len(self.alphabet)

		return self.alphabet[idx]



if __name__ == "__main__":
	rotor = Rotor(1)
	rotor.set_leftrotor(rotor)
	print(rotor.alphabet)
	print(len(rotor.alphabet))
	print(len(rotor.alphabet) // 2)
	print(rotor.mapped)
	x = rotor.get_forward_letter("a")
	print(x)
	print(rotor.get_backward_letter(x))
	print(rotor)
