from datetime import datetime

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.email = name.lower()+'@gmail.com'

    def get_birthday(self):
        current_year = int(datetime.now().year)
        birthday_year = current_year - self.age
        print(f'The year of birthday is {birthday_year}')

    def get_info(self):
        print(f'Personal Data: \nName: {self.name}\nAge: {self.age}\nemail: {self.email}')

persona = Person('jorge',26)
persona.get_info()
persona.get_birthday()

print("\n\n")

class Machine:
    def __init__(self, bank):
        self.bank = bank
        self.balance = 10000
        self.history = []

    def get_money(self, amount):
        if(amount <= self.balance):
            result = self.balance - amount
            self.history.append({"debit": amount, "balance": result})
            print(f'Transaction successfull by ${amount}, the summary of the transaction is: {self.history[-1]}')
        else:
            print("The amount is greater than the cashier's balance.")


    def get_history(self):
        print(f'{self.bank} bank transaction history')
        for transaction in self.history:
            print(transaction)

cajero = Machine('BAC Credomatic')
cajero.get_money(200)
cajero.get_money(500)
cajero.get_money(5000)
cajero.get_history()

'''

class Vehiculo:
    def __init__(self, llanta, color):
        self.llanta = llanta
        self.color = color

    def encender(self):
        print('Vehiculo encendido')


class Coche(Vehiculo):
    def __init__(self, llanta, color, marca):
        super().__init__(llanta, color)
        self.marca = marca

class Moto(Vehicle):
    def __init__(self, llanta, color, marca):
        super().__init__(llanta, color)
        self.marca = marca






















