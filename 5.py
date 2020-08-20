def max_from_count(up_to):
  final = 1
  for i in range(1,up_to):
    final *= i
  return final

max_number = max_from_count(21)
print("Max number is %i" % max_number)
number_fit = 0
number = 0
while number_fit == 0:
  number += 5
  if number > max_number:
    print("Number is above %i!" % max_number)
    break
  if number % 10000000 == 0:
    print("Checking from %i" % number, end=" ")
    print("(%f %%)" % (float(number) / max_number * 100))
  num_of_rule = 0
  for divi in range(1,21):
    #print("%i / %i r %i" % (number, divi, number % divi))
    if number % divi == 0:
      num_of_rule += 1
    if num_of_rule == 20:
      number_fit = number

print(number_fit)
# It should print after some minutes:
# Checking from 230000000 (0.000000 %)
# 232792560