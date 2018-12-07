def remove_empty(list_with_data):
	while '' in list_with_data:
		list_with_data.remove('')
	return list_with_data

def open_file():
	with open('referat.txt') as f:
		text = f.read()
		print('Длина текста {} симв.'.format(len(text)))
		print ('Количество слов в тексте: {}'.format(
			sum([len(remove_empty(line.split(' '))) for line in remove_empty(text.split('\n'))]))
		)

if __name__ == '__main__':
	open_file()