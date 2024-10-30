# Starting value and ending value take from usear 
# starting number : 9 
# ending number : 2
# output : 9 8 7 6 5 4 3 2 


# a = int(input("Enter Starting number : "))
# b = int(input("Enter Ending number : "))

# for i in range(a, b - 1, -1):
#     print(i)

# output : 9 8 7 6 5 4 3 2


# while loop 

# a = int(input("Enter Starting number : "))
# b = int(input("Enter Ending number : "))

# i = a    # initialization
# while i >= b:  # condition
#     print(i)   # statement
#     i -= 1   # increment/decrement


# palindrome number
# user input => 1221   reversed 1221 => this is a palindrome number



# num = int(input("Enter the number :"))
# temp = num
# reversed_number = 0

# while num > 0:
#     rem = num % 10
#     reversed_number = (reversed_number * 10) + rem
#     num = num // 10

# if temp == reversed_number:
#     print("This is a palindrome number")
# else:   
#     print("This is not a palindrome number")
    


# Find first and last digit of number;  ex. 159643 -> first=1  , last=3

num = int(input("Enter the number :"))
first = num

while first >= 10:
    first = first // 10

last = num % 10

print("First digit is : ", first)
print("Last digit is : ", last)