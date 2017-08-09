import math
print("Welcome to calculator.py")
print("Select operation")


print("1 for factorial")
print("2 for addition")
print("3 for subtraction")
print("4 for division")
print("5 for exponent")
print("6 for multiplication")
print("7 for squareroot")
print("8 for cuberoot")
print("9 for cube")
print("10 for square")

operation = input("Please select an operation from the list above: ")


def factorial(n):
	n = int(input("Please enter a number: "))
	factorial = 1
	if n < 0:
		return 'inf'
	elif n == 0:
		return 1
	else:
		for i in range (1, n+1):
			factorial = factorial * i
		print (factorial)
	
	
	
def add(list1,list2):
	
	return map(lambda x,y:x+y, list1, list2)
	#print add()
	#add(a,b)

def subtract(list1,list2):
	
	return lambda x,y:x-y, list1,list2
	#print (ans)
	#subtract(a,b)
	
def divide(list1,list2):
	return map(lambda x, y: x/float(y) if y!= 0 else 'nan', list1, list2)
	
	
def exponent(a,b):
	
	return lambda a,b:a**b,a,b 
	#if first == 0 and second == 0:
	#	return 'ERROR'
	#if first == 0:
	#	return 0
	#if second == 0:
	#	return 1
	#else:
	#	return first ** second
	#print (ans)	
		#return first ** second	
	#exponent(a,b)

	
def multiplication(list1, list2):
	
	return map(lambda a,b:a * b, list1,list2)
	#print (ans)
	#multiplication(a,b)

	
def squareroot(mylist):
	
	return [(lambda a,b:ERROR if a < 0 else a**0.5, mylist)]
	
	
def cuberoot(mylist):
	
	return [(lambda x:x ** float(1/3.0) for x in mylist)]
	#if first < 0:
	#	return -(first) ** (1/3.0)
	#else:
	#	return first ** (1/3.0)
	#print (ans)
	#cuberoot(value)
	
	
def generate_cube(mylist):
	
	for x in mylist:
		yield x ** 3
	#return lambda x: x ** 3
	#print (ans)
	#cube(value)

	
def square(mylist):

	for x in mylist:
		yield x ** 2
	#return lambda x : x ** 2
	#print (ans)
	#square(value)

	
if operation == "1":
	factorial('n')
	
elif operation == "2":
	add('list1','list2')

elif operation == "3":
	subtract('a', 'b')
	
elif operation == "4":
	divide('a', 'b')
	
elif operation == "5":
	exponent('a', 'b')
	
elif operation == "6":
	multiplication('list1', 'list2')
	
elif operation == "7":
	squareroot('value')
	
elif operation == "8":
	cuberoot('value')
	
elif operation == "9":
	generate_cube('mylist')
	
elif operation == "10":
	square('mylist')

