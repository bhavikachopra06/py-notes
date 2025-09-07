# while loop
i = 1
while i <= 5:
    print(i, end=" ")  # prints 1 to 5
    i += 1
print()

# for loop with list
my_list = ['a', 'b', 'c', 'd', 'e']
for i in my_list:
    print(i, end=" ")  # prints each element in list
print()

# for loop with string
s = "Bhavika"
for ch in s:
    print(ch, end=" ")  # prints each character in string
print()

# for loop with dictionary
my_dict = {
    "name": "Bhavika",
    "age": 20,
    "city": "Gurgaon"
}
for key in my_dict:
    print(key, ":", my_dict[key], end=" | ")  # prints key-value pairs
print()

# range with step
for i in range(1, 10, 2):  
    print(i, end=" ")  # prints 1,3,5,7,9
print()

# break example (stops loop when condition met)
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")  # prints 0 1 2
print()

# continue example (skips current iteration)
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")  # prints 0 1 2 4 (skips 3)
print()

# loop with else (runs if loop finishes normally)
for i in range(1, 6):
    print(i, end=" ")
else:
    print("Loop completed")  # prints after loop finishes
