# x = 'San Francisco'
# z = 'Alcatraz Island'

# # concatenating this 2 strings

# print(x + z)



# z = "landmark"

# # POSITION finds
# print(z.find('t'))



# def calculate(width, length, height): 
#    if height == -1: 
#       return width * length 
#    else: 
#       return width * length * height 
 
# numOne = int(input("Enter width: ")) 
# numTwo = int(input("Enter length: ")) 
# numThree = int(input("Enter height, –1 to ignore: ")) 
 
# answer = calculate(numOne, numTwo, numThree) 
 
# if numThree == -1: 
#    print(f"Area {answer}") 
# else: 
#    print(f"Volume {answer}") 


# again = True
# while again == True:
#     a = int(input())
#     if a > 0:
#         counter = 0
#         while a > 0:
#             a = a // 3
#             counter += 1
#     else:
#         again = False
#     print(a)



# Question 7

# n = int(input("ENTER THE TOTAL NUMBER OF PERSONS :"))

# PRICE = 15
# DISCOUNT = 5

# TOTAL = n * PRICE

# if n >= 6:  
#     TOTAL -= DISCOUNT

# print(f"Total price is {TOTAL}")




names = ['Natalie', 'Alex', 'Roshana']
scores = [78, 81, 72, 27, 51, 54, 52, 55, 59]
count = 0


for i in range(3):  
    person = names[i]
    print(f"Student: {person}")  
    for j in range(3):  
        print(j + 1)  
        result = scores[i * 3 + j]  
        print(result)  
        count += 1


