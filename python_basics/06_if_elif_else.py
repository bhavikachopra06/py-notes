# if-elif-else ladder
age = int(input("Enter your age: "))

if age == 18:
    print("You are just an adult.")

if age < 0:
    print("Invalid age")  # handles negative input
elif age == 0:
    print("You are a newborn.")
elif age < 18:
    print("You are a minor.")  # age between 1 and 17
elif age >= 18 and age < 65:
    print("You are an adult.")  # 18 to 64
else:
    print("You are a senior citizen.")  # 65+

# shorthand if-else (ternary operator)
a = int(input("Enter your age: "))
print("Adult") if a >= 18 else print("Minor")

# logical operators in action
print(0 and 5)  # AND -> returns first falsy value (0)
print(1 and 5)  # AND -> returns last value if all are truthy (5)
print(1 or 5)   # OR -> returns first truthy value (1)
print(0 or 5)   # OR -> returns first truthy value (5)
print(not 0)    # NOT -> flips boolean (True)
print(not 1)    # NOT -> flips boolean (False)
print(not 5)    # NOT -> flips boolean (False)
