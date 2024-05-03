# dict1={"name":"baleno","year":2020}
# dict2 = dict1["year"]
# print(type(dict1))

# dict1["colour"] = "red"
# print(dict1)



# thisdict = dict(name="honda",year=2020)
# print(thisdict)


# x = dict1.keys()
# print(x)
# y = dict1.values()
# print(y)


# for x,y in dict1.items():
#     print(x,y)

###################################################################################
#EXERCISES

# # Write a Python script to add a key to a dictionary. 

# # Sample Dictionary : {0: 10, 1: 20}
# # Expected Result : {0: 10, 1: 20, 2: 30}

# sample_dictionary={0:10,1:20}
# sample_dictionary[2] = 30
# print(sample_dictionary)

##########################################################

# # Write a Python script to check whether a given key already exists in a dictionary. 


# dict1={'a':1,'b':2,'c':3}
# key=input("enter a key")

# if key in dict1:
#     print("the given key is there")
# else:
#     print("the given key is not there")

#########################################################

# # Write a Python script to concatenate the following dictionaries to create a new one. 

# # Sample Dictionary : 
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

############################################################

#  Write a Python program to drop empty items from a given dictionary. 

# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


# d1={'c1': 'Red', 'c2': 'Green', 'c3': None}


# d2={}
# for k,v in d1.items():
#     if v is not None:
#         d2[k]=v
# print(d2)
    
###########################################################


# Write a Python program to combine two dictionary by adding values for common keys. 

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}


# for k,v in d1.items():
#     for k1,v1 in d2.items():
#         d1[k]= (v+v1)
# print(d1)

# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})




































































