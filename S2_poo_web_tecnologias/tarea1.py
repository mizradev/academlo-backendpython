'''
Contador de palabras: actualizar el script anterior que lea un archivo de texto y 
retorne las 10 palabras más repetidas. 
Usando clases, métodos, instancias y lo previamente visto en clase.
'''

class Word:
	def __init__(self, fileName):
		self.fileName = fileName

	def get_ten_most_repeated_words(self):
		archivo = open(self.fileName+'.txt')
		counts = {}
		words = archivo.read().replace("," or "."," ").split(" ")
		
		for word in words:
			if len(word) >= 3: 
				counts[word] = counts.get(word, 0) + 1

		max_key = max(counts, key = counts.get)

		print(counts)
		print({"word": max_key, "count": counts[max_key]}) 

word = Word('text')
word.get_ten_most_repeated_words()