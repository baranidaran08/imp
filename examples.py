# Exercise 1: Print First 10 natural numbers using while loop
# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1

#Exercise 2: Calculate the sum of all numbers from 1 to a given number
num = int(input("enter a number"))
sum = 0
for i in range(num+1):
    sum = sum + i
print(sum)


# Exercise 3: Display numbers from a list using loop
# numbers = [1, 5, 10, 80, 14, 55, 20]
# for i in numbers:
#     print(i)

# Exercise 4: Count the total number of digits in a number
# number = (input("Enter a number: "))
# num_digits = len((number))
# print("it has",num_digits, "digits",)

#another way
# num = 0
# for x in number:
#     if x in number:
#         num=num+1
# print(num)


# Exercise 5: Print list in reverse order using a loop
# list1=["banana","red","orange"]

# for i in range(1,len(list1)):
#     print(list1[len(list1)-i])
    

# Exercise 6: Use else block to display a message “Done” after successful execution of for loop
# list1=["banana","red","orange"]
# for i in list1[::-1]:
#     print(i)
# else:
#     print("All fruits are printed")





# Exercise 8: Display Fibonacci series up to 10 terms
   
# n=int(input("enter a number"))
# a = 0
# b = 1
     
# if n < 0:
#     print("Incorrect input")
         
    
# elif n == 0:
#     print("your result is",a)
       

# elif n == 1:
#     print("your result is",b)
    
# else:
#     for i in range(2, n+1):
#         fib = a + b
#         a = b
#         b = fib
#     print(fib)
        


# Exercise 9: Find the factorial of a given number
# n = int(input("Enter a number: "))
# fact = 1

# if n < 0:
#     print("Factorial is not defined for negative numbers.")
# elif n == 0:
#     print("Factorial of 0 is 1.")
# else:
#     for i in range(1, n + 1):
#         fact = fact* i
#     print("Factorial of", n, "is", fact)


# #Exercise 10: Reverse a given integer number
# x=(13456)
# y =str(x)

# for i in y[::-1]:
#     print(i)



# Exercise 11: Use a loop to display elements from a given list present at odd index positions
# list1=["red","orange","banana","apple","grapes"]
# for i in range(1,len(list1),2):
#     print(list1[i])



# # Exercise 7: Write a program to display all prime numbers within a range



# start = int(input("Enter the starting number of the range: "))
# end = int(input("Enter the ending number of the range: "))

# for n in range(start,end+1):
#     if n == 1:
#         print(n,"is not prime ")
#     elif n == 2:
#         print(n,"it is prime number")

#     elif n==3:
#         print(n,"it is prime number")

#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 print(n,"It is not a prime")
#             else:
#                 print(n,"it is prime")
#             break




    
    



