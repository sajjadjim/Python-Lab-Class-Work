list_print = [111,222,333,'jim',3.56,9.899]

for i in list_print:
    print(i)


print("The length of list :",len(list_print))  # length of the List
print(type(list_print))

print("Specefic print item :",list_print[0])
print("Specefic range items print :",list_print[2:5])

print("First to specific Lst print items :",list_print[ :3])
print("Specific point to Last print items :",list_print[2: ])

#Find the items exicts here :
if 11 in list_print :
    print("Yes !! it , stay here")

else:
    print("N0!!, its not exits here.")



#Tupple
list = (44,55,77,'jim',3.56)

for i in list_print:
    print(i)
