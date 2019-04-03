#!/usr/bin/env python3

people = []

class Person:

	def __init__(self, name, income):
		self._name = name
		self._income = income

		self.products = {}

	def add_product():
		try:
			product = str(input("Enter product name: "))
			cost = float(input("Enter product cost ($): "))

			products[product] = price

		except:
			print("Error: Invalid entry format. Make sure cost is a number, e.g. '3.50'.")

	def return_total_cost():
		pass


def main():
	
	start_menu()

	# User enters people to be considered in the calculation.
	while making_people == True:
	
		try:
			check = str(input("Add a person to the calculation? (y/n)"))


			if check == 'y' or 'Y':
				generate_person()

			else:
				break

		except:
			print("Error: Please enter 'y' or 'n'.")


	# User enters items and prices.	
	while adding_items == True:

		for person in people:

		
		

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