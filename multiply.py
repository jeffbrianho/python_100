def multiply(first_num, second_num):
    return first_num *  second_num

def get_num(prompt):
    return float(input(prompt))

first_num = get_num('Enter the first number ')
second_num = get_num('Enter the second number ')
product = first_num * second_num

print(f'{first_num} * {second_num} = {product}')