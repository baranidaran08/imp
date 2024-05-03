#while loop
i=0
while i<6:
    print(i)
    i=i+1

#break statement
i = 0
while i<6:
    print(i)
    if i == 3:
        break
    i=i+1

#continue statement
i = 0
while i<6:
    i=i+1
    if i==4:
       continue
    print(i)

#else with while
i=0
while i<6:
    i=i+1
    print(i)
else:
    print("all printed")
