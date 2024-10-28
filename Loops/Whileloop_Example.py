# print sum of first 10 natural number
# output : 55
# natural number : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# sum = 0
# for i in range(1, 11):
#     sum += i
# print("sum of Natural Numbers are :" ,sum)  


# Home work : print sum of first 10 natural number using while loop

# sum = 0
# i = 1
# while i <= 10:
#     sum += i
#     i += 1

# print("sum of Natural Numbers are :" ,sum)


# check number is prime or not. 
# 	prime -> 2 3 5 7
# 	not prime -> 4 6 9... using while loop


a = input("Enter a number : ")
a = int(a)

i = 2
while i < a:
    if a % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")