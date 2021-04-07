num = 0
numbers = []

while True:
    num = input('Ingrese un numero: ')
    if num != 'done' and isinstance(int(num), int) == True:
        numbers.append(int(num))
    else:
        print("El valor no se puede convertir a entero, intente con un numero.")
        break
        exit()


average_value = sum(numbers) / len(numbers)

print("El promedio es: "+str(round(average_value, 2))) 
