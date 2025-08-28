#task roll the diice
#ask to roll the dice
#if user enters y
#     generate 2 random numbers
#     print them

a=input("Do you want to roll the dice? (y/n): ")
if a.lower() == 'y':
    import random
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You rolled a {dice1} and a {dice2}.")

elif a.lower() == 'n':
    print("You chose not to roll the dice.")

else:
    print("Invalid input. Please enter 'y' or 'n'.")

#task roll the dice


name=['naimish', 'sachin', 'naman','saurabh', 'santosh']
action=['run', 'walk', 'jump', 'swim', 'dance']
object=['ball', 'bat', 'stick', 'rope', 'kite']

while True:
    import random
    n1=random.choice(name)
    n2=random.choice(action)
    n3=random.choice(object)
    print(f"{n1} {n2} with a {n3}")
    
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break


#new project
a=input("Want to play a game? (y/n): ")
if True:
    
       
#randm numberr guess
import random
n = random.randint(1, 10)
while True:
    a = int(input("Guess a number between 1 and 10: "))
    if a < n:
        print("Too low! Try again.")
        continue
    elif a > n:
        print("Too high! Try again.")
        continue
    else:
        print("Congratulations! You've guessed the number!")
        break

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

#pasword manager
import os
import random
master_psswd=input("Enter a master password: ")
def add():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open('passwords.txt', 'a') as f:
        f.write(f"{username} | {password}\n")
    print("Password added successfully.")

def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords stored yet.")
    else:
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
            for line in passwords:
                print(line.strip())


while True:
    print("would you like to add or view passwords? (add/view/exit)")
    choice = input("Enter your choice: (add/view/exit) ").strip().lower()
    if choice == 'add':
        add()
    elif choice == 'view':
        view()
    elif choice == 'exit':
        print("Exiting the password manager.")
        break
    else:
        print("Invalid choice. Please try again.")



import math
print(type(math)) # Output: <class 'module'>
print(math.pi) 

my_string = "Coding is great."
id(my_string)  # Get the memory address of the string
my_string = my_string.replace("great", "awesome")
print(my_string)
# Output: Coding is awesome.
a,b=23,45
b%a
x=10
y=x
z=10
id(x)  # Memory address of x
id(z)  # Memory address of y
y is x
x=["a",1,12,3,4,"jack"]
for i in x:
    print(i, end=' hello ')


for i in range(4): #outer for loop
    for j in range(i + 1): #inner for loop
        print("*", end='')
    print()  # Move to the next line after each row

cart=[10,23,2000,100,213,178]

for i in cart:
    if i > 1000:
        print(f"Item {i} is too expensive, skipping.")
        continue
    print(f"Adding item {i} to the cart.")
else:
    print("All items added to the cart successfully.")

print("This is the \"end\" of the program.")
a="This is the 'end' of the program."
a[-33::]  
a[0:2]# Output: 'end' of the program.
x='naimish'
y="my name is naimish kumar and naimish is 30 year old"
for i in x[0:2]:
    print(i, end=' ')

y.index(x)
y.count(x)
y.replace(x, "sachin")
a=[1,2,3,4,5,6,7,8,9]
a=str(a)
a="hi i am naimish kumar"
a=a.split()
":".join(a)

a.title()  # Capitalizes the first letter of each word
a=[1,2,[3,4,5],6,7]
b=[]
for i in a:
    if isinstance(i, list):
        for j in i:
            b.append(j)
    else:
        b.append(i)
t=10,
type(t)
t=eval(input("Enter a tuple: "))
print(type(t))
b='naimish'
b[5]
t=12,23,12
a,b,c=t
{i for i in t if i > 10}
b='naimishkumar'
d={}
for x in b:
   d[x]=d.get(x, 0)+1
for k, v in d.items():
    print(f"{k}: {v}")
d={1:"hi",2:"hello",3:"how are you"}
d.get(8,"hja")  # Output: 'hi'
a=(1, 2, 3, 4, 5)
b=("a", "b", "c", "d", "e")
{i:j for i,j in zip(a, b)}

def div(a, b):
    return a / b

div(b=5, a=10)  # Output: 15

def pizza_order(size, *toppings):
    print(f"Size: {size}")
    print("Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    pizza_order("Large", "Pepperoni", "Mushrooms", "Olives")  # Example usage

def display_info(name, age, **lol):
    print(f"Name: {name}")
    print(f"Age: {age}")
    for key, value in lol.items():
        print(f"{key}: {value}")

display_info("Alice", 30, city="New York", occupation="Engineer")  # Example usage

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(8))  # Output: 120

#lambda function
square=lambda n: n * n

add=lambda a,b:a+b
add(5, 10)  # Output: 15

#filter function
n=[1, 2, 3, 4, 5, 6, 7, 8, 9]
a=lambda x: x % 2 == 0
a(2)  # Output: False

employees = [
    {"name": "Alice", "age": 30, "department": "HR"},
    {"name": "Bob", "age": 25, "department": "IT"},
    {"name": "Charlie", "age": 35, "department": "Finance"},
    {"name": "David", "age": 28, "department": "IT"}]

list(filter(lambda x: x["department"] == "IT", employees) ) # Output: [{'name': 'Bob', 'age': 25, 'department': 'IT'}, {'name': 'David', 'age': 28, 'department': 'IT'}]

#map function
n = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, n))
print(squared_numbers)  # Output: [1, 4, 9,

celsius = [0, 20, 37, 100]
list(map((lambda x: (x * 9/5) + 32),celsius))


#reduce function
sales = [100, 200, 300, 400, 500]
from functools import reduce
# total_sales =           
reduce(lambda x, y: x + y, sales)  # Output: 1500

#nested function
def outer_function():
    def inner_function():
        print(f"Inner function received:")
    print(f"Outer function received:")
    return inner_function

f=outer_function() 
f() # Example usage
 
  # Output: Inner function received: 5, Outer function received: 10, returns 15



  #class
class dog:
    '''A simple class representing a dog with attributes and methods.
    Attributes:
        name (str): The name of the dog.
        age (int): The age of the dog in years.
    Methods:
        bark(): Prints a message indicating the dog is barking.
        get_age(): Returns the age of the dog.
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self,c):
        self.c=c
        print(f"{self.name} says Woof! also it can {self.c}")


    def get_age(self):
        return self.age
    
dog.__doc__
help(dog)  # Display the class documentation and methods
dog().age

german_shepherd = dog("ger",5)# Create an instance of the dog class
german_shepherd.name= "German Shepherd"
german_shepherd.age = 5
german_shepherd.bark(c ="jask")  # Output: German Shepherd says Woof!
german_shepherd.get_age()  # Output: 5
german_shepherd.__dict__
german_shepherd.__init__("German Shepherd", 5)  # Reinitialize the instance

class only_method:
    def display(self):
        print(f"This is a method in the only_method class.")

only_method().display()  # Output: This is a method in the only_method class.

class test:
    a=10

    def display(self):
        self.a=20
        print(f"Value of a in display method: {self.a}")

    t=test()
    test.a
    t.display()  # Output: Value of a in display method: 20
    t.a


class Parent:
    def __init__(self, parent_data):
        self.parent_instance_variable = parent_data
        self.common_attribute = "Value from Parent"

class Child(Parent):
    def __init__(self, parent_data, child_data):
        # IMPORTANT: Call the parent's __init__ method
        # This initializes self.parent_instance_variable and self.common_attribute
        super().__init__(parent_data)
        
        self.child_instance_variable = child_data

    def display_variables(self):
        print(f"Parent Instance Variable: {self.parent_instance_variable}")
        print(f"Child Instance Variable: {self.child_instance_variable}")
        print(f"Common Attribute (from Parent): {self.common_attribute}")

# Create an instance of the Child class
my_child_object = Child("Data from Parent", "Data from Child")

# Access variables directly from the child object
print(f"Accessing parent_instance_variable from child object: {my_child_object.parent_instance_variable}")
print(f"Accessing child_instance_variable from child object: {my_child_object.child_instance_variable}")
print(f"Accessing common_attribute from child object: {my_child_object.common_attribute}")

# Call the method to display variables
my_child_object.display_variables()



#abstract class
from abc import ABC, abstractmethod
class Fruit(ABC):
    def taste(self):
        pass

a= Fruit()
a.taste()


from abc import ABC, abstractmethod
class Vegetable(ABC):
    @abstractmethod
    def taste(self):
        pass

a= Vegetable().taste()  # This will raise an error because Vegetable is an abstract class



from abc import ABC, abstractmethod

class Vegetable(ABC): #abstract class
    @abstractmethod
    def taste(self):
        pass

    def color(self):
        return "Vegetables can be of various colors."

class Carrot(Vegetable):
    def taste(self):
        return "Carrot tastes earthy and sweet."
    def color(self):
        return "Carrots are usually orange, but can also be purple, yellow, or white."

# Now you can create an instance of the concrete subclass
my_veg = Carrot()
print(my_veg.taste())
my_veg.color()  # Output: Vegetables can be of various colors.


from abc import *
class DBinterface(ABC): #interface class
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class MySQLDB(DBinterface):
    def connect(self):
        print("Connecting to MySQL database...")
    def disconnect(self):
        print("Disconnecting from MySQL database...")

class PostgreSQLDB(DBinterface):
    def connect(self):
        print("Connecting to PostgreSQL database...")   
    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

class MongoDB(DBinterface):
    def connect(self):
        print("Connecting to MongoDB database...")  
    def disconnect(self):
        print("Disconnecting from MongoDB database...")



# Example usage
db = MySQLDB()
db.connect()    


#encapsulation
class BankAccount:
    def __init__(self):
        # Private attributes
        self.__account_number = "123456789"  # Private attribute  
        self.__balance = 67321
        self._bank_name = "SBI"  # Protected attribute
        self.welcome_message = "Welcome to the Bank Account class!" #public attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")   
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def bank_info(self):
        print(f"Bank Name: {self._bank_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")
        print(self.welcome_message)

# Example usage
account = BankAccount()
account.bank_info()
account._bank_name # Access protected attribute (will work)
account.__account_number # Attempt to access private attribute (will not work)
account._BankAccount__account_number  # Access private attribute using name mangling

class BankAccount2(BankAccount):
    def __init__(self):
        super().__init__() # Call the parent class constructor
    def bank_info(self):
        super().bank_info()  # Call the parent class method

# Example usage
account2 = BankAccount2()
account2._bank_name
account2.__account_number = "987654321"  # Attempt to modify private attribute (will not work)
account2._bank_name = "HDFC" # Modify protected attribute (will work)
account2.bank_info()

#exception handling
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")

except :
    print(f"ValueError:. Please enter a valid number.")


#try with multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")  
    print(hfdvjdkvh)

except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}, Please enter a valid number.")
except NameError:
    print("NameError: An undefined variable was used.")
except:
    print("An unexpected error occurred.")
#finally block
finally:
    print("This block always executes, regardless of exceptions.")


#try except with else
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("ValueError: Please enter a valid number.")   
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
else:
    print("No exceptions occurred. The result was calculated successfully.")

#user defined exception
class TyrePunctureError(Exception):
    def __init__(self, message="Tyre puncture occurred!"):
        self.message = message  
        super().__init__(self.message)  

def check_tyre_condition(condition):
    if condition == "punctured":
        raise TyrePunctureError("The tyre is punctured, please fix it.")
    else:
        print("The tyre is in good condition.")

try:
    # check_tyre_condition("good")        
    check_tyre_condition("punctured")  # This will raise the custom exception

except TyrePunctureError as e:
    print(f"Custom Exception: {e.message}")
    
#file handling
import pathlib
pathlib.Path.cwd()  # Get the current working directory
import os
os.getcwd()  # Get the current working directory
with open('text_file.txt', 'w') as f:
    f.write("This is a test file.\n")
with open('text_file.txt', 'r') as f:
    content = f.read()
print(content)  # Output: This is a test file.


#regex
import re
pattern = r'\d{3}-\d{2}-\d{4}'
pattern ="[0-9]{3}-[0-9]{2}-[0-9]{4}"  # Matches a pattern like 123-45-6789
test_string = "My phone number is 123-45-5765."
match = re.search(pattern, test_string) 
if match:
    print(f"Match found: {match.group()}")  
else:
    print("No match found.")


#validating email
import re
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
email = "Mu name is naimish kumar and my email is nkb@gmail.com and other email is jkl@redffmail.org"
match = re.findall(email_pattern, email)
if match:
    print(f"Valid email addresses found: {match}")
else:
    print("No valid email addresses found.")

#extract dates
date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'  # Matches dates in the format DD/MM/YYYY
text = "My birthday is on 15/08/1995 and my friend's birthday is on 20/12/1990."
dates = re.findall(date_pattern, text)
if dates:
    print(f"Dates found: {dates}")  
else:
    print("No dates found.")


#decorators
def outer():
    print("This is the outer function.")
    def inner():
        print("This is the inner function.")
    print("Calling the inner function from outer.")
    inner()


f1=outer()  # Call the outer function
print(f1)  # Output: None, since outer() does not return anything

#function returning another function
def outer():
    print("This is the outer function.")
    def inner():
        print("This is the inner function.")
    print("Calling the inner function from outer.")
    return inner  # Return the inner function

f2 = outer()  # Call the outer function
f2()

#FUNCTION AS AN ARGUMENT
def send_email():
    print("Sending email..")

def notify(action):
    action()  # Call the action function

notify(send_email)  # Pass the send_email function as an argument

#decorators
def greet(name):
    print(f"Hello, {name} good morning.")


def decorator_function(greet):
    def inner_function(name):
        if name=="madan":  # Condition to check
            print("hello madan bad morning")
        else:
            greet(name)
    return inner_function

f=decorator_function(greet)
f("madan")  # Call the decorated function with a name

@decorator_function
def greet(name):
    print(f"Hello, {name} good morning.")
greet("naimish")  # Call the decorated function with a name


def divison(a,b):
    return a / b

def smart_division(func):
    def inner(a, b):
        if b == 0:
            return "Cannot divide by zero."
        else:
            return func(a, b)
    return inner
f=smart_division(divison) 
print(f(6,12)) # Decorate the divison function

@smart_division
def divison(a, b):
    return a / b    

print(divison(10, 2))  # Output: 5.0
print(divison(10, 0))  # Output: Cannot divide by zero. None

#decorator example
# The decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # This calls the original function
        print("Something is happening after the function is called.")
    return wrapper

# The original function we want to decorate
def say_hello():
    print("Hello!")

# Applying the decorator
say_hello = my_decorator(say_hello)
say_hello()


#decorator example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


#decorator chaining
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 1: After function call")
        return result
    return wrapper
def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 2: After function call")
        return result   
    return wrapper

@decorator1
@decorator2
def my_function():
    print("This is my function.")

my_function()  # Call the decorated function
# my_function = decorator1(decorator2(my_function))  # Manually apply decorators


#generators
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()  # Create a generator object
print(type(gen))  # Output: <class 'generator'>
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
for value in gen:  # This will not print anything since the generator is exhausted
    print(value)  # No output, as the generator is already exhausted
# print(next(gen))  # Raises StopIteration error    


#pattern printing
n=4
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print()  # Move to the next line after each row

#pattern printing-2 (increasing triangle)
for i in range(n): #0, 1, 2, 3
    for j in range(i+1): # 1, 2, 3, 4
        print("*", end="  ")
    print()  # Move to the next line after each row

#pattern printing-3 (decreasing triangle)
for i in range(n): #0, 1, 2, 3
    for j in range(i,n): #(0,4),(1,4),(2,4),(3,4)
        print("*", end="  ")
    print() 

#pattern printing-4 (right sided triangle)(decrasing space increasing star)
for i in range(n): #0, 1, 2, 3
    for j in range(i,n): #(0,4),(1,4),(2,4),(3,4)
        print(" ", end="  ")
    for j in range(i+1): # 1, 2, 3, 4
        print("*", end="  ")
    print() 

#left sided triangle (increasing space decreasing star)
for i in range(n): #0, 1, 2, 3
    for j in range(i+1): # 1, 2, 3, 4
        print(" ", end="  ")
    for j in range(i,n): #(0,4),(1,4),(2,4),(3,4)
        print("*", end="  ")
    print()

#pattern printing-5 (hILL pattern)
for i in range(n): #0, 1, 2, 3
    for j in range(i,n): #(0,4),(1,4),(2,4),(3,4)
        print(" ", end="  ")
    for j in range(i): # 1, 2, 3, 4
        print("*", end="  ")
    for j in range(i+1): # 1, 2, 3, 4
        print("*", end="  ")
    print() 

#reverse hill pattern
for i in range(n): #0, 1, 2, 3
    for j in range(i): # 1, 2, 3, 4
        print(" ", end="  ")
    for j in range(i+1,n): #(0,4),(1,4),(2,4),(3,4)
        print("*", end="  ")
    for j in range(i,n): # 1, 2, 3, 4
        print("*", end="  ")
    print()

#pattern printing-6 (diamond pattern)
for i in range(n): #0, 1, 2, 3
    for j in range(i,n): #(0,4),(1,4),(2,4),(3,4)
        print(" ", end="  ")
    for j in range(i): # 1, 2, 3, 4
        print("*", end="  ")
    for j in range(i+1): # 1, 2, 3, 4
        print("*", end="  ")
    print()
for i in range(n): #3, 2, 1, 0
    for j in range(i+1): # 1, 2, 3, 4
        print(" ", end="  ")
    for j in range(i,n-1): #(0,4),(1,4),(2,4),(3,4)
        print("*", end="  ")
    for j in range(i,n): # 1, 2, 3, 4
        print("*", end="  ")
    print()

#how to swap two numbers without using a third variable
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
a = a + b   
b = a - b
a = a - b
print(f"After swapping: a = {a}, b = {b}")  

#check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number to check if it's prime: "))

#method 2
num=13
count=0

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            count += 1
    if count == 0:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

#sum of elements in array
arr = [1, 2, 3, 4, 5]
sum(arr)  # Output: 15
        
#create a class to make a rectangle and find if the given point is inside the rectangle or not
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  # Bottom-left corner x-coordinate
        self.y1 = y1            
        self.x2 = x2  # Top-right corner x-coordinate
        self.y2 = y2
    def contains(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
    
# Example usage
rect = Rectangle(0, 0, 5, 5)
  # Output: <class '__main__.Rectangle'>
result = rect.contains(-1, 3)  # Check if the point (3, 3) is inside the rectangle
if result:
    print("The point is inside the rectangle.")     
else:
    print("The point is outside the rectangle.")


import matplotlib.pyplot as plt

# Create a figure and an axes object, which serves as your canvas
fig, ax = plt.subplots()

# You can now "draw" on the canvas by plotting data
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
 
# Set a title for the plot
ax.set_title("My Jupyter Canvas")

# Display the plot
plt.show()


class Paint:

    def __init__(self,buckets, color):
        self.buckets=buckets
        self.color=color
    def total_price(self):
        if self.color=='white':
            return self.buckets*1.99
        else:
            return self.buckets*2.19
        
class DiscountedPaint(Paint):

    def __init__(self, buckets, color):
        super().__init__(buckets, color)

    def discounted_price(self,discounted_percentage):
        return  super().total_price()-( super().total_price()*discounted_percentage*0.01)
    



class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == 'white':
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

class DiscountedPaint(Paint):
    def discounted_price(self, discounted_percentage):
        # Directly calling the parent class method
        # Note the explicit passing of 'self'
        original_price = Paint.total_price(self)
        return original_price - (original_price * discounted_percentage)

# Create a DiscountedPaint object
discounted_paint = DiscountedPaint(buckets=10, color='blue')
discount_rate = 0.20 # 20% discount

# Call the discounted_price method, which in turn calls the parent's total_price() method
final_price = discounted_paint.discounted_price(discount_rate)
print(f"Discounted blue paint price: ${final_price:.2f}")
 