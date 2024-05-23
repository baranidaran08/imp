# Explain what happens if you try to modify the third item in the tuple t = (1, 2, 3, 4, 5) to 10 with a code snippet.
# Return the sum of all elements in a tuple of numbers.
# Calculate the total number of items in the tuple t = (1, (2, 3, 4), 5, (6, 7)).
# Return a new tuple containing only unique elements from two input tuples.

# Create a tuple with values (10, 20, 30, 40, 50) and print the second item.
mytuple = (10, 20, 30, 40, 50)
x = mytuple[1]
# print(x)


# Print the last three items of the tuple t = (5, 10, 15, 20, 25, 30) using slicing.
t = (5, 10, 15, 20, 25, 30)
y = t[-3:]
# print(y)

# Write a function that takes a tuple and returns its length.
def myfunction(leng):
    return len(leng)

leng = (5, 10, 15, 20, 25, 30)
# print(myfunction(leng))


# Concatenate the tuples t1 = (1, 2, 3) and t2 = (4, 5, 6) to form a new tuple.
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 +t2
# print(t3)


# Print the second item of the second nested tuple in t = (1, (2, 3), 4, (5, 6, 7)).
t4 = (1, (2, 3), 4, (5, 6, 7))
second_item = t4[3][1]
# print(second_item)


# Unpack the tuple t = ('John', 'Doe', 25, 'Engineer') into four variables and print them.
t5 = ('John', 'Doe', 25, 'Engineer')

first_name ,last_name ,age ,role = t5

# print(first_name)
# print(last_name)
# print(age)
# print(role)




# Check if the value 20 exists in the tuple t = (10, 20, 30, 40, 50).
# if 20 in t:
#     print("yes")
# else:
#     print("no")



# Find the index of the value 3 in the tuple t = (1, 2, 3, 4, 5).

f = t3.index(3)
# print(f)


# Convert the tuple t = ('a', 'b', 'c', 'd') into a string.
t6 = ('a', 'b', 'c', 'd')
convert = ''.join(t6)
# print(convert)




# Create a tuple with one item, 50, and print its type to confirm it's a tuple.
t7 = (50,)
# print(type(t7))




# Return the maximum and minimum values in a tuple of integers.

max_value = mytuple[0]
min_value = mytuple[0]

for num in mytuple:
    if  num > max_value:
        max_value = num
    if  num < min_value:
        min_value = num

# print(max_value)
# print(min_value)


# Print each tuple in the list list_of_tuples = [(1, 2), (3, 4), (5, 6)].
list_of_tuples = [(1, 2), (3, 4), (5, 6)]

# for x in list_of_tuples:
#     print(x)


#Convert a list into a tuple.
list_of_tupless = [1, 2, 3, 4, 5, 6]

converting = tuple(list_of_tupless)
# print(converting)


# Reverse the tuple t = (1, 2, 3, 4, 5).
rever = t3[::-1]
# print(rever)


# Convert the tuple t = (1, 2, 3, 4, 5) into a list.
t9 = (1, 2, 3, 4, 5)
list1 = list(t9)
# print(list1)




new_tuple =()
for x in t9:
    if x%2==0:
        new_tuple += (x,)

print(new_tuple)