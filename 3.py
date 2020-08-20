# my old way of thinking about it was that I will find all primes up to
# 600851475143 then check which one is the highest factor
# it would be really resourceful
"""
prime = 0
for i in range(1, 600851475143):
  factors = 0
  for x in range(1, i):
    if i % x == 0:
      factors += 1
  if factors <= 2:
    prime = i
print(prime)
"""
# but there is other way:
# 12 = 2 * 2 * 3; and here is 3, the higher prime
# so I can divide something by even number (2) or uneven (3, 5, 7...?)

import math
import logging
logging.basicConfig(level=logging.DEBUG)

test_num = 600851475143

def get_factor(number):
  factors = []
  for potential_factor in range(1, int(math.sqrt(number) + 1)):
    if  number % potential_factor == 0:
      factors.append(potential_factor)
      factors.append(number // potential_factor)
  return factors
logging.debug(get_factor(7))

def is_prime(number):
  return len(get_factor(number)) == 2 or number == 1
logging.debug(is_prime(7))

all_factors = get_factor(test_num)
highest_prime_factor = 0

for factor in all_factors:
  if is_prime(factor) and (factor > highest_prime_factor):
    highest_prime_factor = factor

print(highest_prime_factor)