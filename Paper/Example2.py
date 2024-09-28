# orderTotal = float(input("Enter the order total: "))
# deliveryDistance = float(input("Enter the delivery distance: "))

# deliveryCost = 0.0
# messageOne = "Minimum spend not met"
# messageTwo = "Delivery not possible"

# if deliveryDistance <= 5 and orderTotal > 0.0:
#     if orderTotal > 50.0:
#         deliveryCost = 1.5
#         print("Delivery Cost : $1.50")
#     elif orderTotal > 25.0:
#         deliveryCost = (orderTotal / 10) * 2
#         print(f"Delivery Cost: {deliveryCost}")
#     else:
#         print(messageOne)
# else:
#     print(messageTwo)


# Two possible values: True or False.

# True: If deliveryDistance is less than or equal to 5. 
# False: If deliveryDistance is greater than 5.


# State the most suitable data type for the following variables used in Figure 3. 
 
#  Variable identifier                 Data type 
# deliveryCost                           float 
# messageOne                             string


# State one other common data type that you have not given in your answer to  Question 02.3. 
# int

# ------------------------------------------------------------------------------------------------------------

# Take input from user in numbers and print weekdays.(1- monday , 2- tuesday ..... 7- sunday)

# 1. Monday
# 2. Tuesday
# 3. Wednesday
# 4. Thursday
# 5. Friday 
# 6. Saturday
# 7. Sunday
"""

day = int(input("Enter a number between 1 and 7: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
"""


# ------------------------------------------------------------------------------------------------------------

# Write a program that takes a number from the user check the number is devide by 3 and 11 or not 


a = int(input("Enter a number: "))

if a % 3 == 0 and a % 11 == 0:
    print("The number is divisible by 3 and 11")
else:
    print("The Number is Not Divisible by 3 and 11")