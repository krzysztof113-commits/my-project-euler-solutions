fabb_array = [1, 2]
sum = 0
while (fabb_array[-1] + fabb_array[-2]) <= 4000000:
  fabb_array.append(fabb_array[-1] + fabb_array[-2])
for i in fabb_array:
  if i % 2 == 0:
    sum += i
    print(i, end=" ")
print("")
print(fabb_array)
print(sum)