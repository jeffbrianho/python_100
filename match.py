value = 5

# match value:
#     case 5:
#         print('Value is 5')
#     case 6:
#         print('Value is 6')
#     case _: # default case
#         print('Value is neither 5 nor 6')

match value:
    case 1|2|3|4:
        print('Value is less than 5')
    case 5|6:
        print('Value is 5 or 6')    
    case _:
        print('Value is NOT 1, 2, 3, 4, 5, or 6')

