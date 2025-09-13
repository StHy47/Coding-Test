word = []
for i in range(5):
	word.append(input())
result = ''

max_length = max(len(i) for i in word)

for col in range(max_length):
	for row in range(5):
		if col < len(word[row]):
			result += word[row][col]
            
print(result)