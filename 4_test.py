num1 = 0
num2 = 0

def palindrome_maker(number):
  part1 = str(number)
  part2 = ""
  for digit_n in range(1, len(part1)+1):
    part2 += part1[-digit_n]
  return int(part1 + part2)

all_palindromes = []
for number in range(10, 99):
  all_palindromes.append(palindrome_maker(number))

for num1_candidate in range(10, 100):
  for num2_candidate in range(10, 100):
    if (num1_candidate * num2_candidate) in all_palindromes:
      num1 = num1_candidate
      num2 = num2_candidate
final_number = num1 * num2
print("The palindrome is %i from numbers %i %i" % (final_number, num1, num2))