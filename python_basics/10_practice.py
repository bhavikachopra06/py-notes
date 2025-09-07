# Q1: Write a program to take user input (name) and print a greeting message.
name = input("Enter your name:")
print(f"{name}, Good Afternoon!")


# Q2: Write a program to take user name & date and print a formatted letter.
user_name = input("Enter your name:")
date = input("Enter the date:")
print(f"Dear {user_name},\nYou are selected!\n{date}")


# Q3: Detect double spaces in a string.
s = "Hello,  my name is Bhavika"
if "  " in s:
    print("Double space found")
else:
    print("No double space found")


# Q4: Replace double spaces with single space.
s1 = "Hello,  my name is Bhavika"
print(s1.replace("  ", " "))


# Q5: Print a multi-line message using \n.
print("Dear Bhavika,\nThis python course is nice.\nThanks!")


# Q6: Store 3 fruit names entered by user into a list.
l = []
for i in range(3):
    fruit = input("Enter fruit name:")
    l.append(fruit)
print(l)


# Q7: Find the sum of numbers in a list.
l1 = [1, 2, 3, 4, 5]
print(sum(l1))


# Q8: Count the number of zeros in a tuple.
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))


# Q9: Create a Hindi-to-English dictionary and print meaning of a user-given word.
d = {
    "Paani": "Water",
    "Khaane": "Food",
    "Dost": "Friend",
    "Ruko": "Stop",
    "Garam": "Hot",
    "Thanda": "Cold",
    "Chota": "Small",
    "Bada": "Big"
}
word = input("Enter a Hindi word:")
print(d[word])


# Q10: Store unique numbers entered by user into a set.
my_set = set()
for i in range(8):
    num = int(input("Enter a number:"))
    my_set.add(num)
print(my_set)


# Q11: Show set behavior with int, float, and string.
my_set2 = set()
my_set2.add(20)      # int
my_set2.add(20.0)    # float (same as int in set)
my_set2.add("20")    # string (different)
print(my_set2)
print(len(my_set2))

# ⚡ Fact: 20 and 20.0 are treated as equal in sets.


# Q12: Create a dictionary of names & languages.
dict1 = {}
dict1["Bhavika"] = "C++"
dict1["Chaitanya"] = "Python"
dict1["Dharya"] = "Java"
dict1["Bhavika"] = "JavaScript"  # overwrites old value
print(dict1)

# ⚡ Fact: If duplicate keys exist, the latest value is kept.


# Q13: Can a set contain a list? Try it.
# st = {8,7,12,"Bhavika",[1,2]}  # ❌ ERROR (lists are mutable)
# print(st)

# ✅ Correct way: use tuple instead
st = {8, 7, 12, "Bhavika", (1, 2)}
print(st)

# ⚡ Fact: Sets can only hold immutable elements (no lists, dicts).
