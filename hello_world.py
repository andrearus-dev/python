# variables - like a label for a value

from random import randint
import datetime
import math
import os  # os library
import os
message = "Hello Python World"
print(message)

message = "Hello python crash course world"
print(message)

# strings - using f-strings to put a variable into a string
# 2-3 personal message

first_name = "sarah"
message = f"Hello {first_name.title()}, would you like to learn some Python today?"
print(message)

# 2-4 name cases - using methods change letter

last_name = "russell"
lower_case = last_name.lower()
upper_case = last_name.upper()
title_method = last_name.title()

print(upper_case)

# 2-5 & 2-6 famous quotes - having quotation marks in a string

author_name = "albert einstein"
quote = '"You can’t blame gravity for falling in love."'
author_and_quote = f"{author_name.title()} once said {quote}"

print(author_and_quote)

# 2-7 stripping names - using strip method to remove whitespace in a string

persons_name = " diana "
persons_name = persons_name.lstrip()
persons_name = persons_name.rstrip()
# removes whitespace from each side (left and right)
persons_name = persons_name.strip()

print("\nDiana")

# 2-8 numbers - using math operators to give the same answer

print(5+3)
print(10-2)
print(4*2)
print(16/2)

# 2-9 - assigning a variable to a number, then putting that number in an f-string with a message

favourite_number = 8
message = f"My favourite number is {favourite_number}"
print(message)

# Chapter 3 introduction lists
# 3-1 storing names of friends in a list

names = ['sarah', 'glenn', 'vikki', 'marnee', 'jess']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[-1].title())  # using -1 instead of 4 to get the last value

# 3-2 greetings - message stays the same but the name of person changes

message = f"You are my dearest friend {names[0].title()}, and I love you very much"

print(message)

# 3-3 my own list

transportation = ['car', 'bike', 'motorcycle']

first_message = f"I would like to pass my driving test, so I could buy a {transportation[0]}"
second_message = f"but for now I will have to ride my {transportation[1]}."
third_message = f"Some day I will upgrade to a {transportation[-1]}."

print(first_message, second_message, third_message)


# input, len, str and int functions
# i commeneted out lines  of code where the input function was

print('What is your name?')
# myName = input()
# print('Nice to meet you ' + myName)
print('The length of your name is:')
# print(len(myName))  # length of name

print('How old are you?')
# age = input()
# converting data types with str function
# print('You will be ' + str(int(age) + 1) + ' in a year.')

# Lists - slicing

animals = ['dog', 'cat', 'tiger', 'lion', 'bear']

# slicing - starts at value 1, goes up to 4 but does not include 4 - slicing has two indexes
print(animals[1:4])

animals[1:3] = ['panther', 'zebra']
print(animals)   # can aso replace values with slicing

del animals[1]  # delete values
print(animals)

# in and not in operator - determines if value is or isn't in a list

true_or_false = 'howdy' in ['hello', 'alright', 'howdy', 'howyah']
print(true_or_false)


# list function - can convert value to list

list_of_letters = list('comical')
print(list_of_letters)

# TYPE CASTING - converting values

price = 3.95
widgets = 5
# to concatenate string and variable, use a comma
print("The price of the widget is", price)
print("We have " + str(widgets) + " in stock")

# constructing data types aka building lists

employees = ["Anna", "Bella", "Tom"]
employees.append("Lisa")

for employee in employees:
    print(employee)     # display code to show content of list

# logical operators

a = 3
b = 8
c = 9
d = 3

print(a == c and a != b)
print(a == b or a == d)
print(not a == c or a != d)

# arithmetic operators

a = 8
b = 3

print(a ** b)  # exponent - meaning A raised to the B power - 8 x 8 x 8 = 512
print(a % b)  # modulus, as in remainder: 8 / 3 = 2

# identity operator - do they have the same id?? - is or is not =  keywords

# containment - eg - does this variable contain this content

sales = [300, 3200, 2500, 4000]
quotes = "Turn could've, would've and should've into can, will, and do"

print(2500 in sales)
print("do" in quote)
print("did" in quote)

# flow control -  statements are IF ELSE

girl_name = "Alice"

if girl_name == "Alice":
    # code is in a block - indentation tells you where block begins and ends
    print("Hi Alice")
print("Your name is not Alice?")


# elif

boy_name = "Bob"
boy_age = 5

if boy_name == "Cynthia":
    print("You are not Bob.")
elif boy_age != 5:
    print("Sorry, no can do, you're not Bob")
elif boy_age >= 5:
    print("Welcome Bob")

# for loop - more concise

total = 0
for num in range(101):
    total = total + num
print(total)

for i in range(5):
    print("Jimmy Four Times " + str(i))

# RANGE FUNCTION
for i in range(12, 18):  # start and stop argument
    print('Getting the hang of this yet? ' + str(i))

for i in range(0, 8, 2):  # STEP ARGUMENT - can increment in two STEPS, or three if you put three at the end
    print('coding is fun' + str(i))

# elif statement and indentation

annualSales = 3000
region = 'North'
if annualSales >= 5000:
    print('Gold Customer')
elif annualSales >= 3000:
    print('Silver Customer')
    if region == 'North':
        print('Send snowboard')
    else:
        print('Send baseball bat')
elif annualSales >= 1000:
    print('Bronze Customer')
else:
    print('Up and coming customer')
print('Thank you for your business')
# this code will run regardless of result outcome because it doesn't belong in the block

monthlySales = 500
newCustomer = True

if monthlySales >= 1000:
    print('Premium shopper')
elif monthlySales >= 600:
    print('Loyal customer')
if monthlySales >= 500 and newCustomer:
    print('Welcome to your new addiction')
print('Enjoy spending your money')

# WHILE LOOP - commented out code with the input function so the next chunck of code can run

# capitalGuess = input("What is the capital of Latvia? ")
numberOfGuesses = 1

# while capitalGuess != "Dublin":
numberOfGuesses = numberOfGuesses + 1
if numberOfGuesses > 3:
    print("You guessed incorrectly 3 times. Game over.")
    # break - breaks the loop - exit
    # capitalGuess = input("Guess again. ")

if numberOfGuesses <= 3:
    print("You guessed it. Dublin is the capital of Ireland. It took you " +
          str(numberOfGuesses) + " to get that right")
#

# --- for loop - set to run a certain number of times

initialSalesGoal = 20000
multiplier = 100
offMonth = True

for monthlyGoal in range(1, 5):
    if monthlyGoal == 3 and offMonth:
        print("No goal for this month")
        continue  # keyword - skips past what the four loop was going to run

    monthlySalesGoal = initialSalesGoal + (monthlyGoal * 100)
    print("Your sales goal for month " +
          str(monthlyGoal) + " is " + str(monthlySalesGoal))

    for weeklyGoal in range(1, 5):  # nested loop
        print("Your goal for week " + str(weeklyGoal) +
              " is " + str(monthlySalesGoal/4))

print("Good luck with your goals.")

# PASS keyword - placeholder for condition or function

# conditional compound operators - and, or, not

# -----most important when working with files - to close them! - use with statement ---


# -- reading input from console and making sure it works


# formatted text for combining number and strings in the same sentence - f" {} "

# function - like mini program in the program - use def statement to define a new function


def hello(name):
    print("Hello " + name)


hello("Alice")
hello("Bob")


def plusOne(number):
    return number + 1


newNumber = plusOne(5)
print(newNumber)

# --- none value

# keyword arguments

print('Hello', end='')
print('World')

# FUNCTIONS - routines that we build so we don't have to repeat code


def subtotal(orderAmount, salesTax=0.8):  # you can also assign a value for the second argument
    subtotal = float(orderAmount) * (1 + float(salesTax))
    return subtotal


def orderMsg():
    print("Thank you for your order(s)")
    return


# firstOrderTotal = subtotal(300)
# secondOrderTotal = subtotal(400, .06)

# thirdOrderAmount = input("What was the order amount? ")
# thirdTax = input("Enter your sales tax rate")
# thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

# print("Your subtotal for the first order is %.2f" % firstOrderTotal)
# print("Your subtotal for the second order is %.2f" % secondOrderTotal)
# print("Your subtotal for the third order is %.2f" % thirdOrderTotal)
# orderMsg()


# === function


def fullName(firstName, lastName):
    print(f"{lastName}, {firstName}")
    print("Initials: " + firstName[0] + lastName[0])
    return


def personInfo():
    pass  # need to know where to get this info


fullName("Mighty", "Mouse")

# pass keyword - placeholder for something we plan to define later


# Basic exception handling

def div42by(divideBy):
    try:  # try and except statement
        return 42 / divideBy
    except:  # can use except without specifing the error and will catch all errors
        print("Error: You tried to divide by zero.")


print(div42by(2))
print(div42by(6))
# we get an error. computers don't know how to handle dividing by 0
print(div42by(0))
print(div42by(12))


pi = math.pi
upperBound = math.ceil(44.4)
lowerBound = math.floor(44.4)

print(pi)
print(upperBound)
print(lowerBound)

todayWithTime = datetime.datetime.today()
todayWithoutTime = datetime.date.today()
print(todayWithTime)
print(todayWithoutTime)

# formatting function
print("The current date is ", datetime.datetime.strftime(
    todayWithoutTime, "%m/%d/%Y"))
print("The current time is ", datetime.datetime.strftime(todayWithTime, "%H:%M:%S"))


# importing random library

for i in range(6):
    print(f"Random number {i} is {randint(1,10)}")


# exercise - to print the name in reverse

# firstName = input("What is your first name?")
# lastName = input("What is your last name?")

# print(f"{firstName[::-1]}{lastName[::-1]}")


# if-else statements exercise

# summarize membership operators in python

colours = ["pink", "red", "blue", "purple"]

if "grey" in colours:
    print("The colour pink exists in the list")

else:
    print("The colour you mentioned does not exist in the list")

# convert string to a list of characters

convert_string = "hello"
new_list = list(convert_string)

print(new_list)


# basic exercise - for loops

# print the cubes of all the elements in a list using a for loop

original_list = [1, 2, 3, 4, 5, 6]
cubes_list = []

for i in original_list:

    cubes_list.append(i ** 3)  # eg 2 x 2 x 2

print(cubes_list)

# combine lists into new list
car_list = [['Volts', 'BMW', 'Ferrari'], ['Honda' ' Toyota', 'Mazda']]
flattened_list = []

for cars_list in car_list:

    for car in cars_list:
        flattened_list.append(car)

print(flattened_list)

# range function

leap_year_range = range(2000, 2100, 4)
leap_year_list = list(leap_year_range)

print(leap_year_list)


# list comprehension

original_list_num = [2, 3, 6, 7, 8, 11, 12, 13, 17, 18]
cube_list = [x ** 3 for x in original_list_num if x % 3 == 0]

print(cube_list)

# while loop - loop until condition is satisfied - used when number of iterations is not known upfront

# for loop - iterated over sequence of values - known length - can be defined with range function


# MATH related built in functions

# min() - returns smallest item in iterable or smallest
# of two or more arguments

player1 = 10
player2 = 4

print(min(player1, player2))
print(min('Amy', 'Aaron', 'bob'))  # letters stored as numbers

# round()

pinches_salt = 2.3
print(round(pinches_salt))

number = 123.67856
print(round(number, 4))


# ** is the expond operator - to the power of


# .ceil() - rounds number up to nearest integer
# .floor() - rounds it down to nearest integer
# The strftime() method returns a string representing date and time using date, time or datetime object.


# OOP - python is an object oriented language - object
# a class is what creates an object - constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)


p1 = Person("Andrea", 26)
p1.myfunc()

# self parameter - reference to current instance of the class


# Lambada - can take any amount of arguments

def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


# creating class and object in python

class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# istantiate the Parrot class


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# accessing the class attributes

print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(blu.__class__.species))

# accessing the instance attributes

print("{} is {} years old.".format(blu.name, blu.age))
print("{} is {} years old").format(woo.name, woo.age)
