# lower TO UPPER CASE WITHOUT USING UPPER FUNCTION

name = input("Enter your name: ")
upper = ""

# amit

for i in name:
    if ord(i) >= 97 and ord(i) <= 122:
        upper = upper + chr(ord(i)-32)

print(upper)

x = 65
print(chr(x)) # A

x = "A"
print(ord(x))