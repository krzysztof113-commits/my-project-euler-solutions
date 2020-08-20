number_names = {
			0: "zero",
			1: "one",
			2: "two",
			3: "three",
			4: "four",
			5: "five",
			6: "six",
			7: "seven",
			8: "eight",
			9: "nine",
			10: "ten",
			11: "eleven",
			12: "twelve",
			13: "thirteen",
			14: "fourteen",
			15: "fifteen",
			16: "sixteen",
			17: "seventeen",
			18: "eighteen",
			19: "nineteen",
			20: "twenty",
			30: "thirty",
			40: "forty",
			50: "fifty",
			60: "sixty",
			70: "seventy",
			80: "eighty",
			90: "ninety",
		}

for teen_number_before in range(20, 100, 10):
	for number_name_between in range(teen_number_before+1, teen_number_before+10):
		first_part = number_names[teen_number_before]
		second_part = number_names[int(str(number_name_between)[1])]
		number_names[number_name_between] = "%s %s" % (first_part, second_part)


class NumberToLetters(object):
	def __init__(self, number):
		self.number = number

	def name(self):
		hundreds = ""
		thousands = ""
		# cutting
		if len(str(self.number)) > 3:
			thousands = str(self.number)[-4:-5:-1][::-1]
			# print(thousands)
		if len(str(self.number)) > 2:
			hundreds = str(self.number)[-3:-4:-1][::-1]
			# print(hundreds)
		tens = str(self.number)[:-3:-1][::-1]
		# print(tens)

		# simple scheme
		"""if len(str(self.number)) > 3:
			print("%s thousands" % thousands, end="")
			if hundreds == "0" and tens != "00":
				print(" and %s" % tens)
			else:
				if tens == "00":
					if hundreds != "0":
						print(" and %s hundreds" % hundreds, end="")
				else:
					print(" %s hundreds and %s" % (hundreds, tens))
		elif len(str(self.number)) > 2:
			print("%s hundreds" % hundreds, end="")
			if tens != "00":
				print(" and %s" % tens)
		else:
			print(tens)"""

		# present number in name format
		name_number = []
		name_tens = number_names[int(tens)]
		if hundreds != "":
			name_hundreds = number_names[int(hundreds)]
		else:
			name_hundreds = ""
		if thousands != "":
			name_thousands = number_names[int(thousands)]
		else:
			name_thousands = ""

		if len(str(self.number)) > 3:

			name_number.append("%s thousand" % name_thousands)

			if hundreds == "0" and tens != "00":
				name_number.append(" and %s" % name_tens)
			else:
				if tens == "00":
					if hundreds != "0":

						name_number.append(" and %s hundred" % name_hundreds)
				else:

					name_number.append(" %s hundred and %s" % (name_hundreds, name_tens))
		elif len(str(self.number)) > 2:
			name_number.append("%s hundred" % name_hundreds)
			if tens != "00":
				name_number.append(" and %s" % name_tens)
		else:
			name_number.append(name_tens)
		return name_number


letters = 0
for _number in range(1, 1001):
	# print("".join(NumberToLetters(_number).name()))
	len_of_number_letters = len("".join(NumberToLetters(_number).name()).replace(" ", ""))
	letters += len_of_number_letters
print(letters)
