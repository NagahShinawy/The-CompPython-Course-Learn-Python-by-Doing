# ############ ############  VARIABLES ############ ############ ###########
print("# ############ ############  VARIABLES ############ ############ ###########")

age = 21

print(f"Age: {age}")

age = 40  # var name = value
print(f"Age: {age}")

countries_visits = 60  # snake_case

# var name that never change [CONSTANTS]

MONTHS = 12

DAYS = 7

FACEBOOK = "facebook"
PI = 3.14

REJECTED = "Rejected"
PASSED = "Passed"
PENDING = "Pending"

#  ############ ############  NUMBERS ############ ############ ###########

print("# ############ ############  numbers ############ ############ ###########")
purchases_items = 4

price = 25

total = purchases_items * price

print(f"Total: {total}")

TAX = 0.15

tax = total * TAX

print(f"Tax: {tax}")

total += tax

print(f"Price After Taxs is {total}")

print(10 // 3)  # Floor division

print(10 % 3)  # reminder

result = 10 / 3
to_int = 10 // 3

decimal_place = result - to_int

print(f"Result: {result}")
print(f"To int: {to_int}")
print(f"Decimal Place: {decimal_place}")

duration = 40

months = duration // 30

remaining_days = duration % 30

print(f"All Duration: {duration}")
print(f"Months: {months}")
print(f"Days: {remaining_days}")


def is_even(number: int):
    return number % 2 == 0


def style_row(row_index: int):
    if is_even(row_index):
        print("Apply Black Style")
    else:
        print("Apply White Style")


print(is_even(22))  # True
print(is_even(20))  # True
print(is_even(33))  # False
print(is_even(9))  # False


#  ############ ############  STRINGS ############ ############ ###########

print("# ############ ############  STRINGS ############ ############ ###########")


username = "John"
adam = "Adam"


WELCOME_MSG = "Hello, "


def welcome(user: str):
    print(WELCOME_MSG + user)
    

welcome(username)
welcome(adam)

# Escape Characters

q = "What is your name ?"

print(q)

q = 'What\'s your name ?'
print(q)
q = "What's your name ?"


print(q)

# multiline string

name = "James"
age = 23
dob = "1998-09-10"

info = """
name:  {name}
age:   {age}
dob:   {dob}
"""

print(info.format(name=name, age=age, dob=dob))

# using f-string

items = 5
price = 140

order = f"You Ordered {items} items with price {price}$"

print(order)
order_id = "nas543534535"
phone = "+201270000000"
delivery_at = "2022-03-12"
order = f"Your Order with Id '{order_id}' has been shipped by '{delivery_at}'. we are contacting you at phone number '{phone}'"

print(order)

order_details = {
    "order_id": order_id,
    "delivery_at": delivery_at,
    "phone_number": phone
}

print(order.format(**order_details))