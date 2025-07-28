#debug 1
try:
    x = 10
    y = 0

    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("try dividing by a number that isnt 0")

#debug 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

#debug 3
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))
#debug 4
def is_even(number):
    if number % 2 == 0:
       return True
    else:
       return False
 
print(is_even(4))
print(is_even(7))

#debug 5
for i in range(5):
   print(i)

#debug 6
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

#debug 7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

#debug 8

def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))
#debug 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello," + name)
else:
   print("Hello, stranger!")



try:
    def divide_numbers(x, y):
       result = x / y
       return result

    num1 = 10
    num2 = 0
    print(divide_numbers(num1, num2))
except ZeroDivisionError:
   print("you cant divide by zero")
