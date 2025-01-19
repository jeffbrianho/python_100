# squares = []

# for number in range(5):
#     square = number * number
#     squares.append(square)

# print(squares)

# for comprehension

# squares = [ number * number for number in range(5) ]
# print(squares)

# multiples_of_six = [ number for number in range(20)
#                     if number % 6 == 0]
# print(multiples_of_six)
# print(multiples_of_six if len(multiples_of_six) == 4 else 'Long') #using a ternary expression

# even_squares = [ number * number for number in range(20)
#                 if number % 2 == 0]
# print(even_squares)

# cats_colors = {
#     'Tess':   'brown',
#     'Leo':    'orange',
#     'Fluffy': 'gray',
#     'Ben':    'black',
#     'Kat':    'orange',
# }

# name = {name.upper(): color.upper() for (name, color) in cats_colors.items()}
# print(name)

squares = {f'{number}-squared': number * number for number in range(10)}
import pprint
pprint.pprint(squares)