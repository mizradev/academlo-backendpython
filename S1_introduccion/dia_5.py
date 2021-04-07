
words = []
counts = {}
'''
def countByKeyboardInput():
	while True:
		word = input('Ingrese una palabra: ')
		
		if word != 'stop':
			words.append(word)
		else:
			break

	for word in words:
		counts[word] = counts.get(word, 0) + 1

	print(counts)


def countByFile():
	fileName = input('Ingrese el nombre del archivo con extencion: ')
	archivo = open(fileName)
	words = archivo.read().split(" ")
	
	for word in words:
		counts[word] = counts.get(word, 0) + 1

	print(counts)
'''

def maxWordRepeat():
	archivo = open('text.txt')
	words = archivo.read().replace("," or "."," ").split(" ")
	
	for word in words:
		if len(word) >= 3: 
			counts[word] = counts.get(word, 0) + 1

	max_key = max(counts, key = counts.get)

	print({"word": max_key, "count": counts[max_key]})














