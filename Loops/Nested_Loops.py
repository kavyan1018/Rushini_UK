# Nested Loop in python 
# Nested loop is a loop inside a loop.

# Syntax:
# for i in range(1, 5):
#     for j in range(1, 5):
#           print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 1 4


# While loop:


# i = 1
# while i <= 4:
#     j = 1
#     while j <= 4:
#         print(i, j)
#         j += 1
#     i += 1


# pattern
# *
# **
# ***
# ****
# *****


for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
    