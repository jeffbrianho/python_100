names = ['Chris', 'Max', 'Karis', 'Victor'] # Original iterable collection
upper_names = [] # Storage for changed collection
# index = 0 # acts as a counter and a way to iterate through list

# while index < len(names): # using the length of the list as a counter and a way to iterate (while loop)
#     upper_name = names[index].upper() # create a variable to save changed value
#     upper_names.append(upper_name) # add saved variable to our storage collection 
#     index += 1 # use to iterate to next and address our counting while loop

# print(upper_names)

for name in names: # name is initialized here (for loop)
    # if name == 'Max':
    #     continue
    if name != 'Max':
        upper_name = name.upper() # still initialize upper_name to save variable to store cased value
        upper_names.append(upper_name) # append value to pre-loop empty list (upper_nanes)

print(upper_names)