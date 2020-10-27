
# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換格式
def convert(lines):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for w in s[2:]:
				if w == '貼圖':
					allen_sticker_count += 1
				elif w == '圖片':
					allen_image_count += 1
				else:	
					allen_word_count += len(w)
		if name == 'Viki':
			for w in s[2:]:
				if w == '貼圖':
					viki_sticker_count += 1
				elif w == '圖片':
					viki_image_count += 1
				else:
					viki_word_count += len(w)
	print('Allen說了',allen_word_count,'個字')
	print('Allen傳了',allen_sticker_count,'個貼圖')
	print('Allen傳了',allen_image_count,'個圖片')
	print('Viki說了',viki_word_count,'個字')
	print('Viki傳了',viki_sticker_count,'個貼圖')
	print('Viki傳了',viki_image_count,'個圖片')

# 寫入檔案
def write_file(chat):
	with open('output.txt', 'w', encoding = 'utf-8') as f:
		for line in chat:
			f.write(line + '\n')

# 主程式
def main(filename):
	lines = read_file(filename)
	convert(lines)
	# write_file(chat)

# 程式進入點
filename = 'LINE-Viki.txt'
main(filename)