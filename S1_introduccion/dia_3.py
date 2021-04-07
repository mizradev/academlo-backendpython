'''numbers = [9, 41, 12, 3, 74, 15]
suma = 0

def maximo(numbers):
	pivote = -1
	for num in numbers:
		if num > pivote:
			pivote = num
		

	return pivote



print("El valor maximo es: "+str( maximo(numbers) ) )
'''

try:
	nombreArchivo = input('Nombre del archivo: ')
	file = open(nombreArchivo)
except:
	print('digital correctamente el nombre del archivo')
	exit()

contador = 0
for lineas in file:
	if lineas.startswith('From:'):
		print(lineas)
		contador += 1

print(contador)


