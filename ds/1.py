# Understand the concept of data structures in python
# 1. Array
# 2. records


# Array in python
# Array is a collection of items stored at contiguous memory locations.
# The idea is to store multiple items of the same type together.
# This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).
#   Array can be handled in python by a module named array. They can be useful when we have to manipulate only a specific data type values.
#   A user can treat lists as arrays. However, user cannot constraint the type of elements stored in a list. If you create arrays using the array module, all elements of the array must be of the same type.

# memory location of the first element of the array (generally denoted by the name of the array).

# An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array)



# memory alocation
# First index
#  |                       |--> Elements(at index 8) 
#  0  1  2  3  4  5  6  7  8  9
#                             |   --> indices
#                           Last index

# array length = 10


# Example 1: Create an array and display its elements
'''
import array as arr

a = arr.array('i',[1,2,3])

print("First element:", a[0])
print("Second element:", a[1])
print("Third element:", a[2])

'''


# take input from user and display the array elements

'''
import array as arr

a = arr.array('i',[])
n = int(input("Enter the length of the array:"))

for i in range(n):
    x = int(input("Enter the next value:"))
    a.append(x)

print(a)

'''


# take input 2 numerbs from user do addition and display the result

import array as arr

numbers = arr.array('f', [0, 0])

numbers[0] = float(input("Enter the first number: "))
numbers[1] = float(input("Enter the second number: "))

result = numbers[0] + numbers[1]

print("The sum is:", result)


# subtration , multiplication, division