
# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換格式
def convert(lines):
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
	return chat

# 寫入檔案
def write_file(chat):
	with open('output.txt', 'w', encoding = 'utf-8') as f:
		for line in chat:
			f.write(line + '\n')

# 主程式
def main(filename):
	lines = read_file(filename)
	chat = convert(lines)
	write_file(chat)

# 程式進入點
filename = 'input.txt'
main(filename)