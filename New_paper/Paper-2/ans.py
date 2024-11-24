# Question 2.1

# level = 'gcse'
# x = len(level)
# print(x)


# title = 'computer science' 
# level = 'gcse' 

# #  concatenating the variable

# x = title + level

# print(x)

"""
Write a Python program that allows a taxi company to calculate how much a 
taxi fare should be. 
 
The program should: 
• allow the user to enter the journey distance in kilometres (no validation 
is required) 
• allow the user to enter the number of passengers (no validation is 
required) 
• calculate the taxi fare by 
o charging £2 for every passenger regardless of the distance 
o charging a further £1.50 for every kilometre regardless of how 
many passengers there are 
• output the final taxi fare. 
 
You should use meaningful variable name(s), correct syntax and indentation 
in your answer. 
 
The answer grid below contains vertical lines to help you indent your code 
accurately. 
"""


# journey_distance = float(input("Enter the journey distance in kilometres: "))
# number_of_passengers = int(input("Enter the number of passengers: "))

# pasaenger_charge = 2 * number_of_passengers
# distance_charge = 1.50 * journey_distance

# total_fare = pasaenger_charge + distance_charge

# print("The total fare is: £", total_fare)



x = input("Enter the Password :")

if x == "secret":
    print("Welcome")
else :
    print("Not Welcome")