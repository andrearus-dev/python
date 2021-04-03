# variables - like a label for a value

message = "Hello Python World"
print(message)

message = "Hello python crash course world"
print(message)

# strings
# 2-3 personal message

first_name = "sarah"
message = f"Hello {first_name.title()}, would you like to learn some Python today?"
print(message)

# 2-4 name cases

last_name = "russell"
lower_case = last_name.lower()
upper_case = last_name.upper()
title_method = last_name.title()

print(upper_case)

# 2-5 & 2-6 famous quotes

author_name = "albert einstein"
quote = '"You can’t blame gravity for falling in love."'
author_and_quote = f"{author_name.title()} once said {quote}"

print(author_and_quote)

# 2-7 stripping names

persons_name = " diana "
persons_name = persons_name.lstrip()
persons_name = persons_name.rstrip()
# removes whitespace from each side (left and right)
persons_name = persons_name.strip()

print("\nDiana")

# 2-8 numbers

print(5+3)
print(10-2)
print(4*2)
print(16/2)

# 2-9

favourite_number = 8
message = f"My favourite number is {favourite_number}"
print(message)
