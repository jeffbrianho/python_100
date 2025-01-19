# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = 0

while index < len(my_list):
    num = 0
    while num < len(my_list[index]):
        if my_list[index][num] % 2 == 0:
            print(my_list[index][num])
        
        num += 1
    
    index += 1