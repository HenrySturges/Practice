class Number:
	temp1=0
	def set(self, x):
		self.temp1 = x
	def multiplyBy10(self, x):
		self.temp1 = self.temp1 *10 + x
		return self.temp1
	def divideBy10(self):
		return ((self.temp1)/10)
	def printNumber(self):
		print self.temp1


#x = Number()
#x.set(234)
#x.printNumber()
#x.multiplyBy10(4)
#x.set(2)
#x.printNumber()
#x.multiplyBy10(3)
#x.printNumber()

