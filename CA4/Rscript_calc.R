# Calculator program in R
#selecting an operation from the list below;

print("select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. for Square")
print("7. for cube")
print("8. for cuberoot")
print("9. for squareroot")
print("10. for factorial")

# The calculator functions

add <- function(x, y) {return(x+y)}

subtract <- function(x, y) {return(x-y)}

multiply <- function(x, y) {return(x*y)}

divide <- function(x, y) {return(x/y)}

exponent <- function(x, y) {return(x^y)}

square <- function(x) {return(x^2)}

cube <- function(x) {return(x^3)}

cuberoot <- function(x) {return(x^(1/3))}

squareroot <- function(x) {return(x^(1/2))}

Factorial <- function(num1) {
  if (num1 > 1)
    return(num1 * factorial(num1-1))
  else
    return("Infinity") 
}


# Taking input from user...
choice = as.integer(readline(prompt="Please enter an operation: "))

num1 = as.integer(readline(prompt="Enter first number: "))
num2 = as.integer(readline(prompt="Enter second number: "))

# Printing out the result...
operator <- switch(choice, "+","-","*","/","^","^","^","^")
result <- switch(choice, add(num1, num2), subtract(num1,num2), multiply(num1,num2), divide(num1,num2), exponent(num1,num2), square(num1), cube(num1), cuberoot(num1), squareroot(num1), factorial(num1))

print(paste("the answer is: ", result))

# tests to check the functions

add(1,2)
subtract(5,2)
multiply(2,5)
divide(10,2)
exponent(2,3)
square(4)
cube(3)
cuberoot(27)
squareroot(16)
Factorial(5)