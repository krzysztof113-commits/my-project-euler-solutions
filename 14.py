chain_lengths = []
start = 13
for i in range(start, 1000001):
	sequence = []
	while i >= 1:
		sequence.append(i)
		if i % 2 == 0:
			i = i // 2
		else:
			i = 3 * i + 1
		if i == 1:
			break
	chain_lengths.append(len(sequence) + 1)

print(chain_lengths.index(max(chain_lengths)) + start)
