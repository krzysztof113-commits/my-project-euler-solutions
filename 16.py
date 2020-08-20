class DigitsOfXtoPowerOfY(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def digits(self):
		return self.x ** self.y

	def sum(self):
		sum_of_digits = 0
		for digit in str(self.digits()):
			sum_of_digits += int(digit)
		return sum_of_digits


print(DigitsOfXtoPowerOfY(2, 1000).sum())