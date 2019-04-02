#!/usr/bin/env python3

people = []

class Person:

	def __init__(self, name, income):
		self._name = name
		self._income = income

		self.products = {}

	def add_product():
		product = str(input("Enter product name: "))
		cost = float(input("Enter product cost ($): "))

		products[product] = price

	def return_total_cost():
		pass


def main():
	
	start_menu()

	while making_people == True:
		generate_person()
		
		while adding_items == True:
		print("For ")
		
		try:
			pass

		except:
			print("Error: Invalid entry format. Make sure cost is a number, e.g. '3.50'.")

	display_totals()



def start_menu():
	print("### Monthly Budget Calculator. ###\n\n")
	expected people = 


def display_totals():
	for each_person in people:
		print("Name: ", each_person._name, ", Monthly income: $", each_person._income)
		print("Items: ", each_person.products)

def generate_person():
	try:
		person_name = str(input("Enter the first person's name: "))
		person_income = float(input("Enter their monthly income ($)"))

		# Generate a new person with the above values.
		person_instance = Person(person_name, person_income)

		# Add them to the list of people.
		people.append(person_instance)

	except:
		print("Input Error: Must input a name and a number value.")
	

if __name__ == '__main__':
	main()