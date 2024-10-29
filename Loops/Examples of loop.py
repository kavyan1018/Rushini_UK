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

a = int(input("Enter Starting number : "))
b = int(input("Enter Ending number : "))

i = a    # initialization
while i >= b:  # condition
    print(i)   # statement
    i -= 1   # increment/decrement