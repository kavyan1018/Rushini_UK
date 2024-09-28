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


# a = int(input("Enter a number: "))

# if a % 3 == 0 and a % 11 == 0:
#     print("The number is divisible by 3 and 11")
# else:
#     print("The Number is Not Divisible by 3 and 11")


"""
Write  a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer, calculate percentage and grade according to given conditions:

	If percentage >= 90% : Grade A
	If percentage >= 80% : Grade B
	If percentage >= 70% : Grade C
	If percentage >= 60% : Grade D
	If percentage >= 40% : Grade E
	If percentage < 40% : Grade F
"""

phy = float(input("Enter the Marks of Physics :"))
che = float(input("Enter the Marks of Chemistry :"))
Bio = float(input("Enter the Marks of Biology :"))
Math = float(input("Enter the Marks of Math :"))
Com = float(input("Enter the Marks of Computer :"))


sum = phy + che + Bio + Math + Com
percentage = (sum / 500) * 100

print("The sum of Total is :",sum)
print("The total persantage is :",percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80 and percentage < 90:
    print("Grade B")
elif percentage >= 70 and percentage < 80:
    print("Grade C")
elif percentage >= 70 and percentage < 60:
    print("Grade D")
elif percentage >= 60 and percentage < 70:
    print("Grade E")
elif percentage >= 50 and percentage <= 60:
    print("Garde F")
elif percentage >= 40 and percentage < 50:
    print("Grade G")
else :
    print("Your are Fail !")