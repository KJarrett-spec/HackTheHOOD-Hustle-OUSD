#Debugging Activity - Kwame Jarrett


#Code Snippet 1

# Incorrect:
x = 10
y = 0
result = x / y # Zero Division Error, fixed by changing y to 5
print("result: ", result)

# Code Snippet 2
# Incorrect:
numbers = [1, 2, 3, 4, 5]
for i in range (len(numbers)):
    print(numbers[i+1]) #Index Error, fixed by changing i+1 to i

# Code Snippet 3
#Incorrect:
def calculate_area(radius)
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius)) # Syntax Error, fixed by adding a colon at the end of the function definition line

# Code Snippet 4
# Incorrect:
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    

print(is_even(4))
print(is_even(7)) # Syntax Error, fixed by removing the extra indentation before the return statement

# Code Snippet 5
# Incorrect:
for i in range(5):
    print(i) # Syntax Error, fixed by removing the extra indentation before the return statement

# Code Snippet 6
# Incorrect:
def greet(name):
    return "Hello, " + name

print(greet("Alice")) # Syntax Error, fixed by adding a closing parenthesis at the end of the print statement

# Code Snippet 7
# Incorrect:
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
    print("Sum of numbers:", sum) # Syntax Error, fixed by removing the extra indentation before the print statement

# Code Snippet 8
# Incorrect:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n+1)
    
    
    print(factorial(5)) # Recursion Error, fixed by changing n+1 to n-1 in the recursive call

# Code Snippet 9
# Incorrect:
name = input("Enter your name: ")
if name == "Alice" or "Bob":
    print("Hello, " + name)
else:
    print("Hello, starnger!") # Logic Error, fixed by changing the condition to (name == "Alice" or name == "Bob")

# Code Snippet 10
# Incorrect:
def divide_numbers(x, y):
    result = x / y
    return result

num1 = 10
num2 = 0
print(divide_numbers(num1, num2)) # Zero Division Error, fixed by changing num2 to 2