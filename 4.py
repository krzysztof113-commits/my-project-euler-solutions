num1 = 0 # from 100 up to 999
num2 = 0
final_number = 0
# palindrome from 3 digit number
# there are range(100, 1000) possible palindromes
# max palindrome from product of 2 digit numbers i 999*999
# < 998,001; so it is = 997,799 
def palindrome_maker(number): #number must be 3 digit
  part1 = str(number)
  part2 = ""
  for digit_n in range(1, len(part1)+1):
    part2 += part1[-digit_n]
  return int(part1 + part2)
# check every palindrome from number 100 to 997
# it must be a product of two 3-digit numbers: num1 and num2
# final_number / num1 = num2
# len(final_number / num1) == 3
# find max num1 that creates len() == 3 from
# we search for all num1 * num2 and
# see if the result is palindrome from all_plandromes array
all_palindromes = []
for number in range(100, 998):
  all_palindromes.append(palindrome_maker(number))

# minimum value of num1 is 100 just like num2
# we could optimize it but maybe later
for num1_candidate in range(100, 1000):
  for num2_candidate in range(100, 1000):
    final_number_candidate = num1_candidate * num2_candidate
    if final_number_candidate in all_palindromes:
      if final_number_candidate > final_number:
        num1 = num1_candidate
        num2 = num2_candidate
        final_number = final_number_candidate
print("The palindrome is %i from numbers %i %i" % (final_number, num1, num2))