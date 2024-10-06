# isalpha
# isdigit
# isalnum
# isspace
# isupper
# islower

# ---------------------------------------------------------------------------------------
"""
# 1...isalpha
# isalpha() method returns True if all the characters are alphabet letters (a-z).
# Syntax: str.isalpha()

# Example:

a = "hii rushini hwo are you"
print(a.isalpha())  # False because of spaces

a = "hiirushinihwoareyou"
print(a.isalpha())  # True
"""

# -------------------------------------------------------------------------------
"""
# 2...isdigit
# isdigit() method returns True if all the characters are digits between 0 - 9(0 1 2 3 4 5 6 7 8 9).
# Syntax: str.isdigit() 

# Example:

a = "3456 789"
print(a.isdigit())  # False because of spaces

a = "3456789"
print(a.isdigit())  # True

"""

# --------------------------------------------------------------------------------

"""
# 3...isalnum
# isalnum() method returns True if all the characters are alphanumeric(a-z, A-Z and 0-9).
# Syntax: str.isalnum()

if u enter any special character it will return False
if we entre any space it will return False

if u want to enter any numbers, alphabets, alphabets + numbers, it will return True

# Example:

# x = "hiirushinihwoareyou"
# print(x.isalnum()) 

# x = "hiirushinihwoareyou123"
# print(x.isalnum())

# x = "123" 
# print(x.isalnum())
"""


# --------------------------------------------------------------------------------

"""
# 4...isspace
# isspace() method returns True if all the characters are whitespaces(space).
# Syntax: str.isspace()
# Example:


# a = " Rushini how was the class "
# print(a.isspace())  # False

# a = " "
# print(a.isspace())  # True
"""


# --------------------------------------------------------------------------------

"""
# 5...isupper
# isupper() method returns True if all the characters are in uppercase.
# Syntax: str.isupper()
# Example:

# a = "kavyan"
# print(a.isupper()) # False

# b = "KAVYAN"
# print(b.isupper())  #True

c = "Kavyan"
print(c.isupper())  # False
"""


# --------------------------------------------------------------------------------

"""
# 6...islower
# islower() method returns True if all the characters are in lowercase.
# Syntax: str.islower()

# Example:

# v = "kavyan"
# print(v.islower()) # True

v = "KAVYAN"
print(v.islower())  #False

v = "Kavyan"
print(v.islower())  # False
"""