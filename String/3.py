# lower TO UPPER CASE WITHOUT USING UPPER FUNCTION
"""
name = input("Enter your name: ")
upper = ""

# amit

for i in name:
    if ord(i) >= 97 and ord(i) <= 122:
        # "" = "" + char (97) - 32  kavyan
        upper = upper + chr(ord(i)-32)

print(upper)

x = 65
print(chr(x)) # A

x = "A"
print(ord(x))

"""


# k = 107  - 32 =>    75
# a = 97   - 32 =>    65
# v = 118  - 32 =>    86
# y = 121  - 32 =>    89 
# a = 97   - 32 =>    65
# n = 110  - 32 =>    78


# UPPER TO LOWER CASE WITHOUT USING LOWER FUNCTION
name = input("Enter your name: ")
lower = ""

for i in name:
    if ord(i) >= 65 and ord(i) <= 90:
        # "" = "" + char (97) - 32  kavyan
        lower = lower + chr(ord(i) + 32)

print(lower)