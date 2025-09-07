s = "i like chaitanya"  

print(s)  # prints the original string
print(s.upper())  # converts entire string to uppercase
print(s.lower())  # converts entire string to lowercase
print(s.capitalize())  # makes first letter uppercase, rest lowercase
print(s.replace("like","love").replace("chaitanya","chittu"))  # replaces words in the string
print(s.find("chaitanya"))  # finds starting index of substring (returns -1 if not found)
print(s.split())  # splits string into a list of words
print("-".join(["a","b","c"]))  # joins list elements with '-' in between
print(s.startswith("i"))  # checks if string starts with "i"
print(s.endswith("a"))  # checks if string ends with "a"
print(s.count('i'))  # counts how many times 'i' appears
print(s.index('c'))  # finds index of 'c' (error if not found)
print(len(s))  # gives total length of string
print(s.strip())  # removes spaces from start and end

# f-string usage (formatted strings)
name = "bhavika"
print(f"hello! my name is {name} and {s}")  # inserting variables inside string

# formatting numbers with f-string
x = 20
print(f"{x:<5}")  # left aligned in width of 5
print(f"{x:^5}")  # centered in width of 5
print(f"{name.upper()}")  # makes name uppercase
