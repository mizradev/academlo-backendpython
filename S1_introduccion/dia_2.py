# condicionales


# calculo de sueldo
default_hour = 40
hours = 0
payByHour = 0

def calc_salary(hours, payByHour):
	if hours > default_hour:
		hours_more = hours - default_hour
		value_extra = hours_more * ((payByHour * 0.5) + payByHour)
		finalValue = {'value': (payByHour * hours) + value_extra, 'extra': True}
	else:
		finalValue = {'value': payByHour * hours, 'extra': False}

	return finalValue

#entrada de datos
try:
	hours_input = int(input('Cantidad de horas trabajadas: '))
	payByHour_input = float(input('Valor por hora de trabajo: '))

	result = calc_salary(hours_input, payByHour_input)

	if result["extra"] == True :
		#mensaje del sueldo calculado
		print("Su sueldo es de: "+str(result["value"])+" valor extra aplicado")
	else:
		print("Su sueldo es de: "+str(result["value"]))
except:
	print("Error: Ingresa valores numericos,")
	exit()