# Q1: Take 3 numbers as input and print the greatest.
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
c = int(input("Enter another number:"))
if a > b and a > c:
    print(f"{a} is the greatest")
elif b > a and b > c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")

# ⚡ Fact: Use max(a, b, c) for a shortcut!


# Q2: Calculate percentage of 3 subjects given total marks.
out_of = int(input("Enter the out of marks:"))
marks1 = int(input("Enter marks of subject 1:"))
marks2 = int(input("Enter marks of subject 2:"))
marks3 = int(input("Enter marks of subject 3:"))

percent = (marks1 + marks2 + marks3) / (out_of * 3) * 100
print(f"Your percentage is {percent:.2f}%")

# ⚡ Fact: :.2f in f-string formats number to 2 decimal places.


# Q3: Detect spam comments based on certain phrases.
p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Click this"
p4 = "Subscribe this"
p5 = "Limited time offer"
comment = input("Enter your comment:")
if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment) or (p5 in comment)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# ⚡ Fact: `in` operator checks substring presence in strings.


# Q4: Check if username is at least 8 characters long.
username = input("Enter your username:")
cnt = len(username)
if cnt < 8:
    print("Username must be at least 8 characters long")
else:
    print("Username is valid")


# Q5: Check if a given name exists in a list.
l = ["Bhavika", "Chaitanya", "Bob", "Alice"]
name = input("Enter your name:")
if name in l:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")


# Q6: Print multiplication table of a given number.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number * i, end=" ")



# Q7: Print greetings for each name in a list.
l = ["Bhavika", "Chaitanya", "Bob", "Alice"]
for name in l:
    print(f"Hello, Good morning {name}")


# Q8: Check if a number is prime.
n1 = int(input("Enter a number:"))
boolean = True

if n1 > 1:
    for i in range(2, int((n1 / 2))):
        if n1 % i == 0:
            boolean = False
            break

if boolean:
    print(f"{n1} is a prime number")
else:
    print(f"{n1} is not a prime number")



# Q9: Print multiplication table in reverse order.
number = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(number * i, end=" ")


# Q10: Convert Celsius to Fahrenheit using a function.
def convert(celcius):
    farenheit = (celcius * 1.8) + 32
    return int(farenheit)

celcius = int(input("Enter temperature in celsius: "))
print(f"Temperature in farenhiet is {convert(celcius)} degrees")



# Q11: Find sum of natural numbers using recursion.
def sum(natural):
    if natural == 0:     # base case
        return 0
    s = natural + sum(natural - 1)
    return s

natural = int(input("Enter a natural number: "))
print(f"The sum of natural numbers up to {natural} is {sum(natural)}")

