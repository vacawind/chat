
lines = []
with open('input.txt', 'r', encoding = "utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())

person = None
chat = []
for line in lines:
	if line == 'Allen':
		person = 'Allen'
		continue
	elif line == 'Tom':
		person = 'Tom' 
		continue
	chat.append( person + '：' + line )
print(chat)

with open('output.txt', 'w', encoding = 'utf-8') as f:
	for line in chat:
		f.write(line + '\n')



