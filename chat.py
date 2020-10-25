
lines = []
with open('input.txt', 'r', encoding = "utf-8") as f:
	for line in f:
		lines.append(line.strip().strip('\ufeff'))

flag = 0
chat = []
for line in lines:
	if line == 'Allen':
		flag = 1
		continue
	elif line == 'Tom':
		flag = 2 
		continue
	if flag == 1:
		chat.append( 'Allen：' + line )
	if flag == 2:
		chat.append( 'Tom：' + line )
print(chat)

with open('output.txt', 'w', encoding = 'utf-8') as f:
	for line in chat:
		f.write(line + '\n')



