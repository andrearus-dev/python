# variables - like a label for a value

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
#myName = input()
#print('Nice to meet you ' + myName)
print('The length of your name is:')
# print(len(myName))  # length of name

print('How old are you?')
#age = input()
# converting data types with str function
#print('You will be ' + str(int(age) + 1) + ' in a year.')

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
