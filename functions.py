# def addition(x,y):
#     print(x + y)

# addition(789,908)


# def diplay_message():
#     print("hello.....hi")

# diplay_message()



















###############################################



#################################################

# Write a Python function to multiply all the numbers in a list. 
# def my_function(list1):
#     sum=1
#     for x in list1:
#         sum=sum*x
#     print(sum)

# list1=[3,4,5,6]
# my_function(list1)

##################################################

# Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# def my_function(sample_list):
#     sum=1
#     for x in sample_list:
#         sum=sum*x
#     print(sum)

# sample_list=list((8,2,3,-1,7))
# my_function(sample_list)

######################################################

# Write a Python program to reverse a string. 
# Sample String : "1234abcd"
# Expected Output : “dcba4321"

# def my_function(string):
#     new_string=[]
#     for x in range(1,len(string)):
#         y = (string[len(string)-x])
#         new_string.append(y)
#         z="".join(new_string)
#     print('"'+z+'"')

# string ="1234abcd"
# my_function(string)

#########################################################

# Write a Python function to create and print a list where the values are the squares of numbers between
# 1 and 30 (both included). 

# def my_function(list1):
#     list2=[]
#     for x in range(1,list1):
#         y=x**2
#         list2.append(y)
#     print(list2)    

# n=int(input("enter a number"))
# list1=(n+1)
# my_function(list1)

###################################################

# Write a Python function that takes a list and returns a new list with distinct elements from the first list. 
# Unique List : [1, 2, 3, 4, 5]


# def my_function(Sample_Liat):
#     Unique_list=[]
#     for x in Sample_List:
#         if x not in Unique_list:
#             Unique_list.append(x)
#     print(f"Unique_list:{Unique_list}")
    
# Sample_List = [1,2,3,3,3,3,4,5]
# my_function(Sample_List)


###################################################

# Write a Python program to access a function inside a function.


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def items(x, y, function):
    return 5 * function(x, y)  

print(items(5, 2, add))
print(items(5,2,sub))




####################################################
















