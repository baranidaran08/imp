# Copy a list and demonstrate the difference between a shallow copy and a deep copy.
# Check if all elements in a list are the same.
# Rotate a list to the right by 3 positions.
# Split a list into two lists, one containing the first half and the other containing the second half.


mylist = [1,2,3,4,5,6,7,8,9,10]

mylist.append(11)

mylist.insert(0,0)

mylist.remove(5)

mylist.pop(3)

first_element = mylist[0]
last_element = mylist[-1]
# print(first_element)
# print(last_element)


sub_list = mylist[2:6]
# print(sub_list)

negative = mylist[-2]
# print(negative)

reverse = mylist[::-1]
# print(reverse)

# Create a new list that contains every second element from the original list.
mylist1 = [1,2,3,4,5,6,7,8,9,10]
new_list = mylist1[1::2]
# print(new_list)

list_comprehension = [x**2 for x in mylist1]
# print(list_comprehension)


# Create a new list that only contains the even numbers from an existing list.
evennumber_list = []
for x in mylist1:
    if x%2==0 :
        evennumber_list.append(x)
# print(evennumber_list)

evennumber_list = [x for x in mylist1 if x%2==0]
# print(evennumber_list)




# print(mylist)


# Concatenate two lists [1, 2, 3] and [4, 5, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
# print(list1)


# Check if the number 7 is in the list.
if 7 in mylist1:
    print("yes")
else:
    print("no")


# Sort the list in ascending order.
mylist1.sort()
# print(mylist1)    

# Sort the list in descending order.
# mylist1.sort(reverse=True)
# print(mylist1)

# Find the index of the first occurrence of the number 3 in the list.
index_of_3 = mylist1.index(3)
# print(index_of_3)



# Remove duplicates from a list while preserving the order.
mylist2 = [1,2,2,3,4,4,4,5,5,6,7,8,9,9,9]
unique_list = []
for x in mylist2:
    if x not in unique_list:
        unique_list.append(x)
# print(unique_list)


# Iterate over a list and print each element.
# for x in mylist1:
    # print(x)

# Use enumerate() to iterate over a list and print the index and element.

# for index,element in enumerate(mylist1):
    # print(index,element)




# Use map() to create a new list with the squares of all elements in an existing list.

def square(x):
    return x ** 2

my_list = [1, 2, 3, 4, 5]

squared_list = list(map(square, my_list))
# squared_numbers = list(map(lambda x: x ** 2, my_list))
# print("List with squares of elements:", squared_list)




# Given a nested list [[1, 2], [3, 4], [5, 6]], access the element 4.
nested_list = [[1, 2], [3, 4], [5, 6]]

new_list1 = nested_list[1][1]
# print(new_list1)




# Flatten a nested list [[1, 2], [3, 4], [5, 6]] into a single list [1, 2, 3, 4, 5, 6].
single_list =  []

for x in nested_list :
    single_list.extend(x)
# print(single_list)




# Combine two lists [1, 2, 3] and [4, 5, 6] into a list of tuples [(1, 4), (2, 5), (3, 6)].
tuple_list = [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]
# print(tuple_list)




# Use the zip() function to combine two lists into a list of tuples.
tuple_list2 = list((zip(list1,list2)))
# print(tuple_list2)



# Use filter() to create a new list that only contains elements greater than 5.
filtered_list = list(filter(lambda x: x > 5, mylist1))

# print("Filtered list:", filtered_list)





# Find the maximum and minimum values in a list.
#we can also use max() and min()function
my_list3 = [10, 5, 20, 8, 15]

maximum_value = my_list3[0]
minimum_value = my_list3[0]


for x in my_list3:
    if x > maximum_value:
        maximum_value = x
    if x < minimum_value:
        minimum_value = x

# print("Maximum value:", maximum_value)
# print("Minimum value:", minimum_value)





# Given a list of integers, create a new list with each element incremented by 1.
incremented_list = [x+1 for x in my_list3]
# print(incremented_list)



# Find the second largest number in a list.
mylist1.sort(reverse=True)
print(mylist1[1])

