# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len([i for i in word if i in 'Аа']))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аоиеёэыуюя'
print(len([i for i in word if i in vowels + vowels.upper()]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
	print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words_in_sentence = sentence.split(' ')
print('%.3f' % (sum(len(word) for word in words_in_sentence)/len(words_in_sentence)))