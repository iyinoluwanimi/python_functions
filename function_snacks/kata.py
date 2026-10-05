def is_even(number):
	if number % 2 == 0:
		return "true"
	else:
		return "false"
		
		
def is_prime_number(number):
	if number > 1:
		count = 0
		for numbers in range(1,number):
			if number % number == 0:
				count = count + 1
		if count == 1:
			return "true"
		else:
			return "false"
	else:
		return "false"
	
		
def subtract(first_number,second_number):
	if first_number < second_number:
		return second_number - first_number
	else:
		return first_number - second_number
		

def divide(first_number,second_number):
	return first_number / second_number

	
def factor_of(number):
	for numbers in range(1,number + 1):
		if number % numbers == 0:
			print(numbers, end = " ") 
	return ""


def is_square(number):
	square_root = number ** (1/2)
	if number / square_root == int(square_root):
		return "true"
	else:
		return "false"	

	
def is_palindrome(number):
	digit1 = number // 10000	
	digit2 = number // 1000 % 10
	digit3 = number // 100 % 10
	digit4 = number // 10 % 10 
	digit5 = number % 10
	
	if digit1 == digit5 and digit2 == digit4:
		return "true"
	else:
		return "false"


def factorial_of(number):
	product = 1
	for numbers in range(1,number + 1):
		product = product * numbers
	return product


def square_of(number):
	return number ** 2


print(is_even(1))
print(is_prime_number(27))
print(subtract(30,50))
print(divide(20,5))
print(factor_of(20))
print(is_square(25))
print(is_palindrome(54145))
print(factorial_of(5))
print(square_of(12))


